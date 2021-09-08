from django.contrib import admin
from django import forms
from .models import Section, Content
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
'''
# <--- Ursprünglich -->

admin.site.register(Content)
'''


class ContentAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Content
        fields = '__all__'


class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm


admin.site.register(Content, ContentAdmin)
admin.site.register(Section)