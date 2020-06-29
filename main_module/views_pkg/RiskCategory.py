from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from main_module.forms import (RiskCategoryForm)
from main_module.models import RiskCategory,Risk

class RiskCategoryMapView(LoginRequiredMixin,TemplateView):
    login_url ='/login/'
    template_name = 'riskcategory_map.html'
    # def get_context_data(self, **kwargs):
    #     context = super(RiskCategoryMapView, self).get_context_data(**kwargs)
    #     context['RiskList'] = Risk.objects.filter(is_active=True)
    #     print(context['RiskList'])
    #     a=RiskCategory.objects.all()
    #     hh=[]
    #     for i in a:
    #         print(i)
    #         hh.append(i)
    #     print(hh)
    #     context['catList'] = hh
    #     return context


class RiskCategoryListView(LoginRequiredMixin,ListView):
    login_url ='/login/'
    context_object_name = "RiskCategoryList"
    paginate_by = 100
    model = RiskCategory
    def get_queryset(self):
        return RiskCategory.objects.all()

class  RiskCategoryCreateView(LoginRequiredMixin,CreateView):
    login_url ='/login/'
    redirect_field_name = 'main_module/riskcategory_detail.html'
    form_class = RiskCategoryForm
    model = RiskCategory

class RiskCategoryUpdateView(LoginRequiredMixin,UpdateView):
    login_url ='/login/'
    redirect_field_name = 'main_module/riskcategory_detail.html'
    form_class = RiskCategoryForm
    model = RiskCategory
class  RiskCategoryDeleteView(LoginRequiredMixin,DeleteView):
    login_url ='/login/'
    model = RiskCategory
    success_url =reverse_lazy('riskcategory_list')
class RiskCategoryDetailView(LoginRequiredMixin,DetailView):
    login_url ='/login/'
    model = RiskCategory

    context_object_name = "riskcategory_detail"
    template_name='main_module/riskcategory_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
