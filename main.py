from fastapi import FastAPI
from typing import Optional
from scraper.scraper import Scraper
from scraper.storage import JSONStorageStrategy
from scraper.notification import ConsoleNotificationStrategy

app = FastAPI()

@app.get("/scrape")
def scrape(limit_pages: Optional[int] = None, proxy: Optional[str] = None):
    storage_strategy = JSONStorageStrategy(output_dir='data')
    notification_strategy = ConsoleNotificationStrategy()
    scraper = Scraper(storage_strategy, notification_strategy)
    scraper.scrape(limit_pages=limit_pages, proxy=proxy)
    return {"status": "Scraping completed"}
