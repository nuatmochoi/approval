from django import forms
from .models import document,tag_str,TagModel


class TagForm(forms.Form):
    #id=forms.IntegerField(label='id')
    string1 = forms.CharField(label='requester',max_length=30)
    string2 = forms.CharField(label='approver', max_length=30)
    string3 = forms.CharField(label='date', max_length=30)
    string4 = forms.CharField(label='document name', max_length=30)
    string5 = forms.CharField(label='string5', max_length=30)
    string6 = forms.CharField(label='string6', max_length=30)
    string7 = forms.CharField(label='string7', max_length=30)
    string8 = forms.CharField(label='string8', max_length=30)
    string9 = forms.CharField(label='string9', max_length=30)


class UploadDocumentForm(forms.Form):
    file = forms.FileField()
    string_mail=forms.CharField(label='string_mail',max_length=1000)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = document
        fields = ('title','description', 'document')

class TagStrForm(forms.ModelForm):
    class Meta:
        model = tag_str
        fields= {'name',}

class TagForm_temp(forms.ModelForm):
    class Meta:
        model = TagModel
        fields = '__all__'

