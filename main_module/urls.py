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
from main_module.views_pkg import (IndexView,AboutView,
                                   HomeView,DashboardView,
                                   HeatMapView,Risk,RiskCategory,
                                   Risk,Issue)
from main_module.views_pkg.apis import (risk_data,riskcategory_map_data)

from django.conf.urls import url


urlpatterns = [
    #api_urls
    path('risk_data/', risk_data.risk_data,name='risk_data'),
    path('riskcategory_map_data/', riskcategory_map_data.riskcategory_map_data,name='riskcategory_map_data'),

    path('about/', AboutView.AboutView.as_view(),name='about'),
    #path('home/', HomeView.HomeView.as_view(),name='dash'),
    path('indexv/', IndexView.IndexView.as_view(),name='indexv'),
    path('home/', DashboardView.DashboardView.as_view(),name='home'),
    path('', DashboardView.DashboardView.as_view(),name='home'),
    path('heat_map/', HeatMapView.HeatMapView.as_view(),name='heat_map'),
    #path('', IndexView.IndexView.as_view(), name='welcomepage'),



    #Risk
    path('risk_list', DashboardView.DashboardView.as_view(),name='risk_list'),
    path('riskdrafts', Risk.DraftRiskListView.as_view(), name='risk_draft_list'),
    url(r'^risk/(?P<pk>[-\w]+)/$', Risk.RiskDetailView.as_view(),name="risk_detail"),
    path('risk_add/', Risk.RiskCreateView.as_view(),name="risk_add"),
    url(r'^risk/update/(?P<pk>[-\w]+)/$', Risk.RiskUpdateView.as_view(),name="risk_update"),
    url(r'^risk/del/(?P<pk>[-\w]+)/$', Risk.RiskDeleteView.as_view(),name="risk_del"),
    #RiskCategory
    path('riskcategory_map/', RiskCategory.RiskCategoryMapView.as_view(),name='riskcategory_map'),
    path('riskcategory_list', RiskCategory.RiskCategoryListView.as_view(), name='riskcategory_list'),
    url(r'^riskcategory/(?P<pk>[-\w]+)/$', RiskCategory.RiskCategoryDetailView.as_view(),name="riskcategory_detail"),
    path('riskcategory_add/', RiskCategory.RiskCategoryCreateView.as_view(),name="riskcategory_add"),
    url(r'^riskcategory/update/(?P<pk>[-\w]+)/$', RiskCategory.RiskCategoryUpdateView.as_view(),name="riskcategory_update"),
    url(r'^riskcategory/del/(?P<pk>[-\w]+)/$', RiskCategory.RiskCategoryDeleteView.as_view(),name="riskcategory_del"),
    #Issue
    path('issue_list', Issue.IssueListView.as_view(), name='issue_list'),
    url(r'^issue/(?P<pk>[-\w]+)/$', Issue.IssueDetailView.as_view(),name="issue_detail"),
    path('issue_add/', Issue.IssueCreateView.as_view(),name="issue_add"),
    url(r'^issue/update/(?P<pk>[-\w]+)/$', Issue.IssueUpdateView.as_view(),name="issue_update"),
    url(r'^issue/del/(?P<pk>[-\w]+)/$', Issue.IssueDeleteView.as_view(),name="issue_del"),

]
