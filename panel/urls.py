# -*- coding: utf-8 -*-


from django.conf.urls import url


from .views import HomePanelView
from .views import SearchPanelView


urlpatterns = [
	url(r'^$', HomePanelView.as_view(), name='index'),
	url(r'^search/$', SearchPanelView.as_view(), name='search'),
]