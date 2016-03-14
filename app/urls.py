# -*- coding: utf-8 -*-


from django.conf.urls import include, url
from django.contrib import admin


from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


from calls.views import CallInputIVRView


router = routers.DefaultRouter()


urlpatterns = [
	# rutas api rest
	url(r'^api/', include(router.urls)),
	url(r'^api-token/', obtain_auth_token),
	url(r'^api/call-input/', CallInputIVRView.as_view()),
	# ruta admin
    url(r'^admin/', admin.site.urls),
]
