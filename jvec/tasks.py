# tasks.py (inside one of your Django apps)

from celery import shared_task
from .models import NewsItem
from datetime import timedelta
import requests


@shared_task
def sync_news_to_db():
    # Define your logic to fetch and sync news items here
    # You can use the 'requests' library to fetch data from an external source

    # Example: Fetch the latest 100 items from the Hacker News API
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item_data in data[:100]:
            # Create or update NewsItem objects in your database
            NewsItem.objects.update_or_create(
                item_id=item_data['id'],
                defaults={
                    'title': item_data['title'],
                    'url': item_data['url'],
                    'created_at': item_data['created_at'],
                    'item_type': item_data['item_type'],
                    'score': item_data['score'],
                }
            )
