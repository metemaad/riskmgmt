"""riskmgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from main_module import views
from django.conf.urls import url


urlpatterns = [
    path('about/', views.AboutView.as_view(),name='about'),
    path('home/', views.HomeView.as_view(),name='home'),
    path('dash/', views.DashboardView.as_view(),name='dash'),

    path('heat_map/', views.HeatMapView.as_view(),name='heat_map'),
    path('riskcategory_map/', views.RiskCategoryMapView.as_view(),name='riskcategory_map'),

    #api_urls
    path('risk_data/', views.risk_data,name='risk_data'),
    path('riskcategory_map_data/', views.riskcategory_map_data,name='riskcategory_map_data'),


    path('', views.RiskListView.as_view(), name='risk_list'),
    path('riskdrafts', views.DraftRiskListView.as_view(), name='risk_draft_list'),
    url(r'^risk/(?P<pk>[-\w]+)/$', views.RiskDetailView.as_view(),name="risk_detail"),
    path('risk_add/', views.RiskCreateView.as_view(),name="risk_add"),
    url(r'^risk/update/(?P<pk>[-\w]+)/$', views.RiskUpdateView.as_view(),name="risk_update"),
    url(r'^risk/del/(?P<pk>[-\w]+)/$', views.RiskDeleteView.as_view(),name="risk_del"),

    path('riskcategory_list', views.RiskCategoryListView.as_view(), name='riskcategory_list'),
    url(r'^riskcategory/(?P<pk>[-\w]+)/$', views.RiskCategoryDetailView.as_view(),name="riskcategory_detail"),
    path('riskcategory_add/', views.RiskCategoryCreateView.as_view(),name="riskcategory_add"),
    url(r'^riskcategory/update/(?P<pk>[-\w]+)/$', views.RiskCategoryUpdateView.as_view(),name="riskcategory_update"),
    url(r'^riskcategory/del/(?P<pk>[-\w]+)/$', views.RiskCategoryDeleteView.as_view(),name="riskcategory_del"),


    path('issue_list', views.IssueListView.as_view(), name='issue_list'),
    url(r'^issue/(?P<pk>[-\w]+)/$', views.IssueDetailView.as_view(),name="issue_detail"),
    path('issue_add/', views.IssueCreateView.as_view(),name="issue_add"),
    url(r'^issue/update/(?P<pk>[-\w]+)/$', views.IssueUpdateView.as_view(),name="issue_update"),
    url(r'^issue/del/(?P<pk>[-\w]+)/$', views.IssueDeleteView.as_view(),name="issue_del"),

]
