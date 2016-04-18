# -*- coding: utf-8 -*-


from django.conf.urls import url


from .views import HomePanelView
from .views import DynamicSearchPanelView

urlpatterns = [
	url(r'^$', HomePanelView.as_view(), name='index'),
	url(r'^search/(?P<date_from>\d+)/(?P<date_to>\d+)/$', DynamicSearchPanelView.as_view(), name='search'),
]
