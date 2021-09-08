from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Section(models.Model):
    '''
    Definiert das Model Section
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, help_text='Eine kurze Überschrift')
    text = models.TextField(max_length=200, help_text='Kurze knackige Beschreibung')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Content(models.Model):
    '''
    Der Haupttext bereich wird hier definiert
    RichTextUploadingField bindet den CKeditor ein
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=160, help_text='Hier eine Überschrift')
    text = RichTextUploadingField(help_text='p class="lead mb-0"  einfügen im Textbereich')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


