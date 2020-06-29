from django import forms
from django.contrib.auth.models import User
from main_module.models import (Risk,Document,
                                RiskCategory,Issue,
                                UserProfileInfo)
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User

        fields=('username','email','password')

class ProfileUserInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio','picture')

class IssueForm(forms.ModelForm):
    class Meta():
        model = Issue
        fields=('title','issue',
                'description')



        widgets = {
            'title':forms.TextInput(attrs={'class':"form-control mr-sm-2",'placeholder':'Enter the title of risk category.'}),
            'issue':forms.Select(attrs={'class':"form-control mr-sm-2"}),
            'description':forms.Textarea(attrs={'class':'form-control editable medium-editor-textarea postcontent'}),
            #'level':forms.TextInput(attrs={'class':"form-control mr-sm-2"}),
            #'hierarcy':forms.TextInput(attrs={'class':"form-control mr-sm-2"}),
            #'color':forms.TextInput(attrs={'class':"form-control mr-sm-2"}),
            #'type_of_category':forms.Select(attrs={'class':"form-control mr-sm-2"}),

        }
class RiskCategoryForm(forms.ModelForm):
    class Meta():
        model = RiskCategory
        fields=('category_title','parent',
                'description','type_of_category','color')
        widgets = {
            'category_title':forms.TextInput(attrs={'class':"form-control mr-sm-2",'placeholder':'Enter the title of risk category.'}),
            'parent':forms.Select(attrs={'class':"form-control mr-sm-2"}),
            'description':forms.Textarea(attrs={'class':'form-control editable medium-editor-textarea postcontent'}),
            #'level':forms.TextInput(attrs={'class':"form-control mr-sm-2"}),
            #'hierarcy':forms.TextInput(attrs={'class':"form-control mr-sm-2"}),
            'color':forms.TextInput(attrs={'class':"form-control mr-sm-2"}),
            'type_of_category':forms.Select(attrs={'class':"form-control mr-sm-2"}),

        }



class RiskForm(forms.ModelForm):
    class Meta():
        model = Risk
        fields=('title','description','category','user_register','create_date','impact','likelihood',
                #'criticality',
                'is_active')

        widgets = {
            'title':forms.TextInput(attrs={'class':"form-control mr-sm-2",'placeholder':'Enter the title of risk.'}),
            'description':forms.Textarea(attrs={
                'class':"textarea",'id':"description", 'placeholder':"Place some text here",
                'style':'"width: 100%; height: 400px; font-size: 14px; line-height: 18px;border: 1px solid #dddddd; padding: 10px;"'}),
            'create_date': forms.TextInput(attrs={'class':"form-control datetimepicker-input",'id':'reservationdate',
                                                   'data-target':'reservationdate','data-toggle':"datetimepicker",
                                                   'data-target':"#reservationdate"}),
            'impact':forms.TextInput(attrs={'id':"range_5", 'name':"range_5", 'value':"0;10",
                'class':"form-control mr-sm-2"}),
            'likelihood':forms.TextInput(attrs={'id':"range_4", 'name':"range_4", 'value':"0;10",
                'class':"form-control mr-sm-2"}),
            #'criticality':forms.TextInput(attrs={'class':"form-control mr-sm-2"}),
            'user_register':forms.Select(attrs={'class':"form-control mr-sm-2"}),
            'category':forms.Select(attrs={'style':'"width: 100%;"',
                'class':"form-control mr-sm-2 select2"}),
            'is_active':forms.CheckboxInput(attrs={'id':"customSwitch1",
                'class':"form-control mr-sm-2"}),
        }
class DocumentForm(forms.ModelForm):
    class Meta():
        model = Document
        fields=('title','description')
