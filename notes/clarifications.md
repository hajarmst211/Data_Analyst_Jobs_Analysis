# columns explanation:

| Column Name            | Description / Purpose                                                                |
|------------------------|--------------------------------------------------------------------------------------|
| job_link               | Unique identifier / URL of the job posting.                                           |
| last_processed_time    | Timestamp when the posting was last processed / scraped.                             |
| last_status            | Status field indicating completion or state of processing.                            |
| got_summary            | Flag (Y/N) — whether a summary was successfully extracted.                            |
| got_ner                | Flag — whether named‑entity recognition (NER) was applied / succeeded.                |
| is_being_worked        | Flag — whether the posting is currently being processed.                              |
| job_title              | Title of the job (e.g. “Data Scientist”, “Machine Learning Engineer”).                |
| company                | Employer / company name posting the job.                                              |
| job_location           | Location string of the job posting (e.g. city, state, region).                        |
| first_seen             | Date when the posting was first observed / scraped.                                   |
| search_city            | City used for the search query — may differ or be derived from job_location.          |
| id_country             | Coded value representing country (likely foreign key to a country table).             |
| search_position        | The search term / position used when scraping (may help indicate search context).     |
| id_level               | Coded value representing job-level / seniority (foreign key to a job-level table).    |
| job_type               | Employment arrangement: full-time, part-time, contract, internship, etc.              |
