"""
SimpleDjangoServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from SimpleDjangoServer import views as viewsPage

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', viewsPage.IndexPage.as_view()),
    path('About/',viewsPage.AboutPage.as_view()),
    path('Contact/', viewsPage.ContactPage.as_view()),
    path('Payment/', viewsPage.PaymentPage.as_view()),
    path('Tracking/', viewsPage.TrackingPage.as_view()),
    path('Tracking/User/', viewsPage.UserTrackingPage.as_view()),
    path('Tracking/OrderCode/', viewsPage.OrderCodeTrackingPage.as_view()),
    path('GetOrder/', viewsPage.GetOrderPage.as_view()),
    path('Order/', viewsPage.OrderModelType_DATA),
    path('Order/Model/', viewsPage.OrderModelName_DATA),
    path('Order/Search/', viewsPage.SearchOrder),
    path('Tracking/Track/User/', viewsPage.UserTracking_Page),
    path('Tracking/Track/Code/', viewsPage.CodeTracking_Page)
]
