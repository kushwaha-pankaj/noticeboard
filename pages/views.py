from django.shortcuts import render
from django.views import View
from pages.models import About, Slider

class HomeView(View):
    def get(self, request, *args, **kwargs):
        sliders = Slider.objects.all()
        abouts = About.objects.all()
        context = {
            'sliders': sliders,
            'abouts': abouts,
        }
        return render(request, 'frontend/index.html', context)
