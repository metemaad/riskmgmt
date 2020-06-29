from main_module.models import RiskCategory
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse








@login_required()
def get_auto_complete_description(request):
    description = str(request.POST.get('description', None))
    data = RiskCategory.objects.filter(category_title__icontains=description)[:10]
    res = []
    for d in data:
        res.append(d.category_title)
    return JsonResponse({'description': res})
