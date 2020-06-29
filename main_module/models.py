from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.
class Organization(models.Model):
    name= models.CharField(max_length=1024)
    ris_appetite= models.TextField(blank=True)
    ris_tolerance= models.TextField(blank=True)
    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio=models.URLField(blank=True)
    picture=models.ImageField(upload_to="profile_pics",blank=True)
    organization = models.ForeignKey(Organization,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class RiskCategory(models.Model):
    category_title = models.CharField(max_length=1024)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE)
    level=models.IntegerField(default=0)
    description = models.TextField(blank=True)
    hierarcy=models.CharField(default='',blank=True, max_length=1024)

    type_of_category_dic =(
        ("0", "Pure Risk"),
        ("1", "Speculative Risk"),

    )
    type_of_category = models.CharField(default=0,max_length=1, choices=type_of_category_dic)
    color=models.CharField(max_length=10,default='#FFFFFF', blank=True,null=True)


    def get_parent_color(self):
        a=self.hierarcy.split('-')
        if len(a)<=1 :
            return self.color
        else:

            return RiskCategory.objects.filter(hierarcy__exact=a[0])[0].color
    def save(self, *args, **kwargs):
        super(RiskCategory, self).save(*args, **kwargs)
        if str(self.parent) == "None":
            self.level=0
            self.hierarcy=str(self.pk)
        else:
            self.level=self.parent.level+1
            self.hierarcy=str(self.parent.pk)+"-"+str(self.pk)
        super(RiskCategory, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('riskcategory_detail',kwargs={'pk':self.pk})
    def __str__(self):
        if self.type_of_category == "0":
            e='P'
        else:
            e='S'

        if str(self.parent) == "None":
            s=''
        else:
            s=str(self.parent)+": "
        return s+str(self.category_title)#+"("+e+")"

class Risk(models.Model):
    title = models.CharField(max_length=1024)
    category = models.ForeignKey(RiskCategory,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    user_register = models.ForeignKey(User,on_delete=models.CASCADE)
    create_date = models.DateField(default=timezone.now)
    impact = models.IntegerField(default=0)
    likelihood = models.IntegerField(default=0)

    #Criticality: a product of the risk priority number elements
    #of consequence and occurance used to determine the relative
    #risk of a failure mode and effects analysis item
    criticality = models.IntegerField(blank=True,null=True)

    #rate the severity of the effect of the failure
    #consequence = models.IntegerField(blank=True,null=True)
    #rate the likelihood that a failure will occur (failure rate)
    #occurance = models.IntegerField(blank=True,null=True)
    #rate the likelihood that the failure will not be detected before it reaches the customer
    #detection = models.IntegerField(blank=True,null=True)

    is_active = models.BooleanField(default=False)
    def update_criticality(self):
        self.criticality = self.impact * self.likelihood
        self.save()
    def apprived_documents(self):
        return self.risk_documents.filter(is_active=True)
    def get_absolute_url(self):
        return reverse('risk_detail',kwargs={'pk':self.pk})
    def activate_risk(self):
        self.is_active=True
        self.save()
    def __str__(self):
        return self.title

class RiskResiduals(models.Model):
    risk = models.ForeignKey(Risk,on_delete=models.CASCADE,related_name='source_risk')
    resulted_risk = models.ForeignKey(Risk,on_delete=models.CASCADE,related_name='result_risk')
    def __str__(self):
        return self.risk.title+"->"+self.resulted_risk.title
# define class for Issues, Incidents, Losses, actions, IssueLog, IncidentLog, Losslog
class Issue(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    issue = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE)
    level=models.IntegerField(default=0)
    hierarcy=models.CharField(default='',blank=True, max_length=1024)
    def get_absolute_url(self):
        return reverse('issue_detail',kwargs={'pk':self.pk})
    def save(self, *args, **kwargs):
        if str(self.issue) == "None":
            self.level=0
            self.hierarcy='0'
        else:
            self.level=self.issue.level+1
            self.hierarcy=self.issue.hierarcy+"-"+str(self.level)
        super(Issue, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
# class IssueRegister(models.Model):
#     issue = models.ForeignKey(Issue,on_delete=models.CASCADE,related_name='issue_register_rel')
#     occurance_date = models.DateTimeField()
#     description = models.TextField(blank=True)
#     def __str__(self):
#         return self.title
# class Incident(models.Model):
#     title = models.CharField(max_length=1024)
#     description = models.TextField(blank=True)
#     def __str__(self):
#         return self.title
# class IncidentIssues(models.Model):
#     incident = models.ForeignKey(Incident,on_delete=models.CASCADE,related_name='cause_incident')
#     issue = models.ForeignKey(Issue,on_delete=models.CASCADE,related_name='source_issue')
#     def __str__(self):
#         return self.issue.title+"->"+self.incident.title
# class Loss(models.Model):
#     title = models.CharField(max_length=1024)
#     description = models.TextField(blank=True)
#     def __str__(self):
#         return self.title
# class LossIncident(models.Model):
#     loss = models.ForeignKey(Loss,on_delete=models.CASCADE,related_name='cause_loss')
#     incident = models.ForeignKey(Incident,on_delete=models.CASCADE,related_name='source_incident')
#     def __str__(self):
#         return self.incident.title+"->"+self.loss.title

class Document(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    upload_date = models.DateField(default=timezone.now)
    file_type =(
        ("P", "PDF File"),
        ("D", "Document File Doc"),
        ("x", "Excel File XLS"),
    )
    type = models.CharField(max_length=1, choices=file_type)
    uploader_user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    file=models.FileField(upload_to="documents_files",blank=True)
    risk = models.ForeignKey(Risk,related_name="risk_documents",on_delete=models.CASCADE)

    is_active=models.BooleanField(default=False)

    def activate_document(self):
        self.is_active=True
        self.save()

    def get_absolute_url(self):
        return reverse('risk_list')
    def __str__(self):
        return str(self.type)+":"+self.title
