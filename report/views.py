from django.shortcuts import render
from django.views import View


class Home(View):
    template_name = 'report/report.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass
