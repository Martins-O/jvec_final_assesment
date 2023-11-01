from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import NewsItem


def latest_news(request):
    # Initialize queryset
    news_items = NewsItem.objects.all()

    # Filtering by item type
    item_type = request.GET.get('item_type')
    if item_type:
        news_items = news_items.filter(item_type=item_type)

    # Text search
    search_query = request.GET.get('search')
    if search_query:
        news_items = news_items.filter(Q(title__icontains=search_query))

    # Pagination
    page = request.GET.get('page')
    items_per_page = 10  # Number of items to display per page
    paginator = Paginator(news_items, items_per_page)

    try:
        news_items = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        news_items = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page
        news_items = paginator.page(paginator.num_pages)

    return render(request, 'news/latest_news.html', {'news_items': news_items})
