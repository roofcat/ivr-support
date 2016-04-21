# -*- coding: utf-8 -*-


from django.conf.urls import url


from .views import CallDetailView
from .views import DynamicSearchPanelView
from .views import HomePanelView

urlpatterns = [
	url(r'^$', HomePanelView.as_view(), name='index'),
	url(r'^call-detail/$', CallDetailView.as_view(), name='call-detail'),
	url(r'^search/(?P<date_from>\d+)/(?P<date_to>\d+)/$', DynamicSearchPanelView.as_view(), name='search'),
]
