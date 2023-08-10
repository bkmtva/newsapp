from datetime import timedelta, datetime
from typing import Dict
from django.utils import timezone
from django.shortcuts import render
from .models import New, Category


def index(request):
    today = datetime.now()
    categories = Category.objects.all()
    today_news = New.objects.filter(pub_date__date=today.date())
    twentyfour_hours_ago = timezone.now() - timedelta(hours=24)
    news = New.objects.filter(pub_date__gte=twentyfour_hours_ago).order_by("-pub_date")[
        :17
    ]
    region_category = Category.objects.get(name="Региональные новости")
    region_news = New.objects.filter(category=region_category)

    context: Dict[str, Any] = {
        "categories": categories,
        "today": today,
        "news": news,
        "region_news": region_news,
        "today_news": today_news,
    }
    print(region_news)
    return render(request, "news/index.html", context)
