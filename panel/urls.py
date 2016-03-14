# -*- coding: utf-8 -*-


from django.conf.urls import url


from .views import HomePanelView


urlpatterns = [
	url(r'^$', HomePanelView.as_view(), name='index'),
]