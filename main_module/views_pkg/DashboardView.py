from django.views.generic import TemplateView
from django.contrib.auth.models import User
from main_module.models import UserProfileInfo
from main_module.models import Risk,RiskCategory

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
