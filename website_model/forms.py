from django import forms
from website_model.models import Member,ordr,Groop
from django.forms import ModelForm



class ord_form(ModelForm):
    class Meta():
        model=ordr
        fields=('__all__')
class grp_form(ModelForm):
    class Meta():
       model=Groop
       exclude=['Members']

class Membr_form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Member
        exclude=['Ingroup']
