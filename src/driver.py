from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy as np
import pickle


#log into linked in
def login(driver, username, password):
    url = "https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    driver.get(url)
    
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("login__form_action_container").click()

#redirects driver to the query link
def search(driver):
  time.sleep(5)
  driver.get("https://www.linkedin.com/jobs/search/?keywords=data%20science")

#grabs results fetched
def get_n_results(driver):
  time.sleep(10)
  results_div = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/header/div[1]/small")
  n_string = results_div.text
  n = int(n_string.split()[0].replace(',',""))
  return n 

#Finds job ul div
def get_jobs(driver):
  ul_div = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul")
  return ul_div

#Scrolls to properly load page
def scroll_down(driver):
  for i in np.linspace(0,1,10):
    time.sleep(2)
    driver.execute_script(f"window.scrollTo(0,document.body.scrollHeight*{i})")
def get_job_urls(jobs,driver,job_urls = {}):
  i = 1
  #Collects job urls,location role cand company 
  #the final result updates the input dictionary and appends a key value pair with the format
  #    url:{'company':company,'location':location,'role':role}d m
  while True: 
    try:
      WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{i}]')))
      url = jobs.find_element_by_xpath(f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{i}]/div/div/div[1]/div[2]/div[1]/a').get_attribute("href")
      role = jobs.find_element_by_xpath(f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{i}]/div/div/div[1]/div[2]/div[1]/a').text
      company = jobs.find_element_by_xpath(f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{i}]/div/div/div[1]/div[2]/div[1]/a').text
      location = driver.find_element_by_xpath(f'/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{i}]/div/div/div[1]/div[2]/div[3]/ul/li').text
      job_urls.update({url:{'company':company,'location':location,'role':role}})
      i+=1
    except:
      return job_urls

def load_next_page(driver):
  #loads next page for url retrival
  curr= driver.find_element_by_xpath('//*[@aria-current="true"]').text
  next = driver.find_element_by_xpath(f'//*[@aria-label="Page {int(curr)+1}"]')
  next.click()

def get_description(driver,job_dict,good):

  fail = []
  #Iterate through the url list to scrape the descriptions
  for url in list(job_dict.keys()):
    if url not in good:
      try:
        driver.get(url)
        time.sleep(3)
        if driver.current_url != url:
          print(f'failed at {url}')
          #remove borken urls
          job_dict.pop(url)
        #scrape
        driver.find_element_by_xpath('//*[@aria-label="Click to see more description"]').click()
        description = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[1]/div[1]/div/div[2]/article/div').text
        job_dict.get(url).update({"description":description})
        good.append(url)
        return job_dict
      except:
        #keep going if there is a random error in which a div did not load properly but check where we failed
        print(f"fail {job_dict.get(url)}")
        fail.append(url)
  
  
#Run theough the entire process of fetch in urls logining in and grabing job descriptions
def main(driver):
    username = input("enter your user name: \n")
    password = input("Enter the password: \n")
    login(driver, username, password)
    search(driver)
    n = get_n_results(driver)
    job_dict ={}
    #iterate through the amount of pages given
    for i in range(40):
        jobs = get_jobs(driver)
        scroll_down(driver)
        get_job_urls(jobs,driver,job_urls = job_dict)
        load_next_page(driver)
    good=[]
    get_description(driver,job_dict,good)

    return get_description(driver,job_dict,good)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    main(driver)