from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import View

from .models import MenuItem


class MenuView(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug', None)
        try:
            title = MenuItem.objects.get(slug=slug).title
        except ObjectDoesNotExist:
            title = 'Главная'
        context = {'menu_name': slug, 'title': title}
        return render(request, 'index.html', context)
