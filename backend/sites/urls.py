

from django.urls import path
from sites.views import (
    SiteListAPIView,
    AnalyzeAPIView,
    StatisticsAPIView
)
from sites.views import get_site_by_id


#I have implemented both the approaches...

urlpatterns = [
    path('get_all_sites', SiteListAPIView.as_view()), # class based routes
    path('get_sites_by_id', get_site_by_id),  #fucntion based routes
    path('analyze', AnalyzeAPIView.as_view()),
    path('statistics', StatisticsAPIView.as_view()),
]
