from django.views.generic.base import View
from django.shortcuts import render

class AboutUs(View):
  def get(self, request, *args, **kwargs):
      return render(request, "base.html")

class Success(View):
  def get(self, request, *args, **kwargs):
      return render(request, "google_app/final.html")
