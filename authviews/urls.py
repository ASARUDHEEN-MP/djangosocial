from django.urls import path
from .views import TestView,newcheck

urlpatterns = [
    path('start/', TestView.as_view(), name="testview"),
    path('test1/', newcheck.as_view(), name="testone"),
    # other URL patterns
]
