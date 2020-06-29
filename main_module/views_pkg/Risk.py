from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from main_module.forms import (RiskForm)
from main_module.models import RiskCategory,Risk

class RiskListView(LoginRequiredMixin,ListView):
    login_url ='/login/'
    context_object_name = "RiskList"
    paginate_by = 10
    model = Risk
    def get_queryset(self):
        return Risk.objects.filter(is_active=True).order_by('-create_date')
class DraftRiskListView(LoginRequiredMixin,ListView):
    login_url ='/login/'
    redirect_field_name = 'main_module/risk_detail.html'
    model = Risk
    def get_queryset(self):
        return Risk.objects.filter(is_active=False).order_by('-create_date')

class RiskDetailView(LoginRequiredMixin,DetailView):
    login_url ='/login/'
    model = Risk

    context_object_name = "risk_detail"
    template_name='main_module/risk_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        #context['welcomePages'] = WelcomePage.objects.filter(active__exact=True)[0]
        #context['pagesList'] = Pages.objects.filter(active__exact=True).order_by('order')
        return context

class  RiskCreateView(LoginRequiredMixin,CreateView):
    login_url ='/login/'
    redirect_field_name = 'main_module/risk_detail.html'
    form_class = RiskForm
    model = Risk

class RiskUpdateView(LoginRequiredMixin,UpdateView):
    login_url ='/login/'
    redirect_field_name = 'main_module/risk_detail.html'
    form_class = RiskForm
    model = Risk
class  RiskDeleteView(LoginRequiredMixin,DeleteView):
    model = Risk
    success_url =reverse_lazy('risk_list')
