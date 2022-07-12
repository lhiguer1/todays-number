"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from . import views


year_pattern = r'(?P<year>20[2-9]\d)' # 2000-2100 exclusive
month_pattern = r'(?P<month>0[\d]|1[0-2])' # 01-12
day_pattern = r'(?P<day>3[01]|0\d|[12]\d)' # 01-31
date_pattern = r'^(?:{}/(?:{}/(?:{}/)?)?)?$'.format(year_pattern, month_pattern, day_pattern)

urlpatterns = [
    # Create
    path('add/', views.NumberCreateView.as_view(), name='add-number'),

    # Read
    re_path(date_pattern, views.NumberListView.as_view(), name='number-list'),

    # Update
    path('update/<int:pk>', views.NumberUpdateView.as_view(), name='update-number'),

    # Delete
    path('delete/<int:pk>', views.NumberDestroyView.as_view(), name='delete-number'),
]
