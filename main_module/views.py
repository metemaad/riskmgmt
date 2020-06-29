from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from main_module.models import Risk,RiskCategory,Issue
from main_module.forms import (RiskForm,RiskCategoryForm,
                               IssueForm,UserForm,ProfileUserInfoForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


@login_required
@api_view()
def risk_data(request):
    queryset = Risk.objects.filter(is_active=True).values()
    l=[]
    lp={}
    for i in RiskCategory.objects.filter(level=0).values():
        l.append(i['id'])
        lp[i['id']]=i['category_title']
    return JsonResponse({"risks": list(queryset),"cat":l,"cat2":lp})

@login_required
@api_view()
def riskcategory_map_data(request):
    def get_childs(arg=None):
        res1={}
        if arg==None:
            res1['name']="Risk Classification"
            res1['parent']="null"
        else:
            arg_obj=RiskCategory.objects.filter(id__exact=arg).values()
            res1['name']=arg_obj[0]['category_title']
            arg_obj=RiskCategory.objects.filter(id__exact=arg_obj[0]['parent_id']).values()
            if len(arg_obj)==0:
                res1['parent']="Risk Classification"
            else:
                res1['parent']=arg_obj[0]['category_title']

        children=[]
        for _ in RiskCategory.objects.filter(parent__exact=arg).values():
            children.append(get_childs(_['id']))
        if len(children)>0:
            res1["children"]=children
        return res1
    queryset=get_childs()
    return JsonResponse(queryset)




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            #if user.is_active():
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
            #else:
            #    return HttpResponse("account is not active")
        else:
            print("login failed.....")
            return HttpResponse("Invalid login")
    else:
        return render(request,'registeration/login.html',{})

def register(request):
    registered = False

    if request.method == "POST":
        user_form=UserForm(data=request.POST)
        profile_form=ProfileUserInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=ProfileUserInfoForm()

    return render(request,'registeration/registeration.html',context={
    'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered,
    })

class IndexView(TemplateView):
    template_name = 'index.html'
from django.contrib.auth.models import User
from main_module.models import UserProfileInfo
class DashboardView(TemplateView):
    template_name = 'base_dash.html'#'index_dashboard.html'
    def get_context_data(self, **kwargs):
        try:
            context = super(DashboardView, self).get_context_data(**kwargs)
            current_user = User.objects.filter(username__exact=self.request.user)[0]

            current_user_profile=UserProfileInfo.objects.all()[0]#.filter(user_id__exact=current_user.pk)[0]

            context['user'] = current_user
            context['user_profile_image'] = current_user_profile.picture.url
        except :
            context['user'] = 'error'
            context['user_profile_image'] = ''

        #a=RiskCategory.objects.all()
        #hh=[]
        #for i in a:
    ##        print(i)
        #    hh.append(i)
        #print(hh)
        #context['catList'] = hh
        return context

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

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
######   Issue view Classes

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
######   Risk Category View Classes
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

######   Risk View Classes
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

@login_required()
def get_auto_complete_description(request):
    description = str(request.POST.get('description', None))
    data = RiskCategory.objects.filter(category_title__icontains=description)[:10]
    res = []
    for d in data:
        res.append(d.category_title)
    return JsonResponse({'description': res})
