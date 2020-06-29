from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from main_module.models import Risk,RiskCategory
from django.http import JsonResponse

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
