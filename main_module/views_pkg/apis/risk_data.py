from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from main_module.models import Risk,RiskCategory
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
