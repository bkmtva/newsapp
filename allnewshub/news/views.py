from django.shortcuts import render

from django.http import HttpResponse
from .models import New, Category
from django.utils import timezone
from datetime import timedelta


def index(request):
    categories = Category.objects.all()

    twentyfour_hours_ago = timezone.now() - timedelta(hours=24)
    news = New.objects.filter(pub_date__gte=twentyfour_hours_ago).order_by("-pub_date")[
        :17
    ]
    region_category = Category.objects.get(name="Региональные новости")
    region_news = New.objects.filter(category=region_category)
    context = {"categories": categories, "news": news, "region_news": region_news}
    print(region_news)
    return render(request, "news/index.html", context)
