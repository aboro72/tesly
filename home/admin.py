from django.contrib import admin
from .models import Section, Content

'''
# <--- Ursprünglich -->
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ContentAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Content
        fields = '__all__'


class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm

'''
admin.site.register(Content)
admin.site.register(Section)