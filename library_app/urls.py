"""
URL configuration for library_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('api_data/', APIData, name='apidata'),
    path('members/', Members, name='members'),
    path('transaction/', Transactions, name='transaction'),
    path('SearchBooks/', SearchBooks, name='SearchBooks'),
    path('BookEdit/', BookEdit, name='BookEdit'),
    path('BookDelete/', BookDelete, name='BookDelete'),
    path('EditTransactions/', EditTransactions, name='EditTransactions'),
    path('TransactionDelete/', TransactionDelete, name='TransactionDelete'),
]
