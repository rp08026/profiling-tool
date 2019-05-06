from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.TimeSeriesView.as_view(), name="index")
]

urlpatterns = format_suffix_patterns(urlpatterns)
