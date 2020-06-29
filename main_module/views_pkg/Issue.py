from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from main_module.forms import (IssueForm)
from django.urls import reverse,reverse_lazy
from main_module.models import Issue

class IssueListView(LoginRequiredMixin,ListView):
    login_url ='/login/'
    context_object_name = "IssueList"
    paginate_by = 100
    model = Issue
    def get_queryset(self):
        return Issue.objects.all()

class  IssueCreateView(LoginRequiredMixin,CreateView):
    login_url ='/login/'
    redirect_field_name = 'main_module/issue_detail.html'
    form_class = IssueForm
    model = Issue

class IssueUpdateView(LoginRequiredMixin,UpdateView):
    login_url ='/login/'
    redirect_field_name = 'main_module/issue_detail.html'
    form_class = IssueForm
    model = Issue
class  IssueDeleteView(LoginRequiredMixin,DeleteView):
    login_url ='/login/'
    model = Issue
    success_url =reverse_lazy('issue_list')
class IssueDetailView(LoginRequiredMixin,DetailView):
    login_url ='/login/'
    model = Issue

    context_object_name = "Issue_detail"
    template_name='main_module/issue_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
