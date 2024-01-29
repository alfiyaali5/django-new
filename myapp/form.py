from django import forms
from .models import Bookstore

class MemberForm(forms.ModelForm):
    class Meta:
     model =Bookstore
     fields =['bookname','description','price','available','image']


 