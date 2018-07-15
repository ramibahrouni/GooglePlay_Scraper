# -*- coding: utf-8 -*-

# Scrapy settings for gplaycrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'app'

SPIDER_MODULES = ['scraping.spiders']
NEWSPIDER_MODULE = 'scraping.spiders'
#AJAXCRAWL_ENABLED = True
#FEED_FORMAT = 'csv'
#FEED_URI = 'Contacts.csv'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Rami Bahrouni (+https://bitbucket.org/rio05/g_play_scraper)'
ITEM_PIPELINES = {
    'scraping.pipelines.GPlayPipeline': 400,
    'scraping.pipelines.MongoPipeline': 300,
}
MONGO_URI = 'mongodb://root:20254641root@ds018308.mlab.com:18308/gplayapps'
MONGO_DATABASE = 'gplayapps'

REACTOR_THREADPOOL_MAXSIZE = 20
# LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
##RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 60
##REDIRECT_ENABLED = False
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
