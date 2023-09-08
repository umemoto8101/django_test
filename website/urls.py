from django.urls import path

from .views import IndexView, ContactView, AboutView

urlpatterns = [
    path('', IndexView.as_view()),
    path('contact/', ContactView.as_view()),
    path('about/', AboutView.as_view()),
]
