from django.urls import path

from .views import HomePageView, GameConsoleView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('gameconsole', GameConsoleView.as_view(), name='gameconsole')
]