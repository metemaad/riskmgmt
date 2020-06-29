from django.contrib import admin


# Register your models here.
from main_module.models import (Risk,Document,RiskCategory,
                                Organization,RiskResiduals,
                                Issue,UserProfileInfo)
admin.site.register(Risk)
admin.site.register(RiskCategory)
admin.site.register(Organization)
admin.site.register(Document)
admin.site.register(RiskResiduals)
admin.site.register(Issue)
admin.site.register(UserProfileInfo)
