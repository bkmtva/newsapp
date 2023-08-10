from datetime import datetime
from typing import Dict, Any
from django.shortcuts import render
from .models import New, Category


def index(request):
    today = datetime.now()
    categories = Category.objects.all()
    region_category = Category.objects.get(name="Региональные новости")
    region_news = New.objects.filter(category=region_category).order_by("-pub_date")
    news = New.objects.all().order_by("-pub_date")[:17]
    today_news = New.objects.filter(pub_date__date=today.date())
    scandal_news = New.objects.filter(is_scandal=True).order_by("-pub_date")

    context: Dict[str, Any] = {
        "categories": categories,
        "news": news,
        "region_news": region_news,
        "scandal_news": scandal_news,
    }
    return render(request, "news/index.html", context)
