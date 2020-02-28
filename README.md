# Data Extraction
### Extract copyright information from the given urls
Extracted data will be stored in PostgreSQL 

For environment variables create '.env' file in the project root and keep them there, see env
-example.md

#### to run spider use the following command:
```
scrapy crawl dates -a csv_path={path_to_urls_csv}
``` 