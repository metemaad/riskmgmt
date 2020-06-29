from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView)
from main_module.models import RiskCategory,Risk

class HeatMapView(LoginRequiredMixin,TemplateView):
    login_url ='/login/'
    template_name = 'heat_map.html'
    def get_context_data(self, **kwargs):
        context = super(HeatMapView, self).get_context_data(**kwargs)
        context['RiskList'] = Risk.objects.filter(is_active=True)
        print(context['RiskList'])
        a=RiskCategory.objects.all()
        hh=[]
        for i in a:
            print(i)
            hh.append(i)
        print(hh)
        context['catList'] = hh
        return context
