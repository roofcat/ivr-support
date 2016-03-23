# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.views.generic import TemplateView


from authentications.views import LoginRequiredMixin


class HomePanelView(LoginRequiredMixin, TemplateView):
	template_name = 'panel/index.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class SearchPanelView(LoginRequiredMixin, TemplateView):
	template_name = 'panel/search.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)
