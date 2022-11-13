from django.urls import path

# from . import views
from .views import (
    CompanyView,
)

urlpatterns = [
    path('api', CompanyView.as_view()),
    # path('', views.index, name='index'),
]