# -*- coding: utf-8 -*-

# Scrapy settings for date_scrapper project
import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))

BOT_NAME = 'date_scrapper'

SPIDER_MODULES = ['date_scrapper.spiders']
NEWSPIDER_MODULE = 'date_scrapper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Enable or disable spider middlewares
SPIDER_MIDDLEWARES = {
    'date_scrapper.middlewares.DateScrapperSpiderMiddleware': 543,
}

# Configure item pipelines
ITEM_PIPELINES = {
    'date_scrapper.pipelines.DateScrapperPipeline': 300,
}

# CUSTOM SETTINGS
HTTPERROR_ALLOW_ALL = True

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': os.environ.get('DBUSERNAME'),
    'password': os.environ.get('DBPASSWORD'),
    'database': os.environ.get('DATABASE')
}

LOG_LEVEL = "INFO"
LOG_ENABLED = False
LOG_FORMAT = '%(filename)s | %(lineno)d | %(funcName)s | %(asctime)s | %(levelname)s: %(message)s'
DOWNLOAD_TIMEOUT = 5
RETRY_ENABLED = False
LOG_FILE = 'date_scrapper.log'
