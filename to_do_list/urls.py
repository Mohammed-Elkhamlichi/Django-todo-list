"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# my importings:
from django.contrib import admin
from django.urls import path, include
from .views import (
    to_do_list,
    update_to_do_list,
    delete_to_do_list,
)

# my routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', to_do_list, name="to_do_list"),
    path('update/<int:id>/<str:title>/', update_to_do_list, name="update"),
    path('delete/<int:id>/<str:title>/', delete_to_do_list, name="delete"),
]
