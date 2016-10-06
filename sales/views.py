from django.shortcuts import render
from django.views import View


class Home(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass
