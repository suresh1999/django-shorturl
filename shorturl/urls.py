from django.urls import path
from .views import *

app_name = "short_urls"
urlpatterns = [
    path('shorturl/generate/', GenerateURL.as_view()),
    path('longurl/', CheckURL.as_view()),
    path('shorturls/generate/', GenerateURLS.as_view()),
    path('longurls/', CheckURLS.as_view())
]