from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template import loader
from .forms import ContactForm
from .models import Section, Content


def home(request):
    '''
    :param request:
    :return:
    :Section.object.order sorts the entries by publication date:
    :Content.object.order sorts the entries as mentioned above
    '''
    sec = Section.objects.order_by('published_date')[:3]
    con = Content.objects.order_by('published_date')[:3]
    template = loader.get_template('home/index.html')
    # output = ', '.join([q.title for q in sec])
    context = {
        'Section': sec,
        'Content': con,
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home:home")

    form = ContactForm()
    return render(request, "home/contact.html", {'form': form})