from django.http import HttpResponse
from django.template import loader
from .models import Section, Content


def home(request):
    sec = Section.objects.order_by('published_date')[:3]
    con = Content.objects.order_by('published_date')[:3]
    template = loader.get_template('home/index.html')
    # output = ', '.join([q.title for q in sec])
    context = {
        'Section': sec,
        'Content': con,
    }
    return HttpResponse(template.render(context, request))
