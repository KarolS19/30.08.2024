BOT_NAME = 'quotes_scraper'
SPIDER_MODULES = ['quotes_scraper.spiders']
NEWSPIDER_MODULE = 'quotes_scraper.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'quotes_scraper.pipelines.QuotesPipeline': 300,
}

FEEDS = {
    'quotes.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': None,
        'indent': 4,
    },
    'authors.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': None,
        'indent': 4,
    },
}
