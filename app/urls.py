# -*- coding: utf-8 -*-


from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


from authentications.views import log_in, log_out, to_home, ProfileTemplateView
from calls.views import CallInputIVRView


router = routers.DefaultRouter()


urlpatterns = [
	# rutas api rest
	url(r'^api/', include(router.urls)),
	url(r'^api-token/', obtain_auth_token),
	url(r'^api/call-input/', CallInputIVRView.as_view()),

	url(r'^panel/', include('panel.urls', namespace='panel')),
	# autenticaciones
	url(r'^$', to_home, name='home'),
	url(r'^login/', log_in, name='login'),
	url(r'^logout/', log_out, name='logout'),
	url(r'^profile/', ProfileTemplateView.as_view(), name='profile'),
	# ruta admin
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    	'document_root': settings.MEDIA_ROOT,
	}),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    	'document_root': settings.STATIC_ROOT,
	}),
]
