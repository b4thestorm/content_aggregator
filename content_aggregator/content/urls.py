from django.urls import path
from content.views import ContentView

urlpatterns = [
    path('', ContentView.as_view()),
]