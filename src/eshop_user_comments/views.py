from django.shortcuts import render
from eshop_setting.models import SiteSetting
from .forms import ContactForm
from .models import UserComment
from django.contrib import messages


# Create your views here.


def contact_us(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        full_name = form.cleaned_data.get('full_name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        UserComment.objects.create(full_name=full_name, email=email, subject=subject, message=message)
        messages.success(request, 'نظر شما با موفقیت ثبت شد')
        form = ContactForm()
    success_message = messages.get_messages(request)
    information = SiteSetting.objects.last()
    context = {
        'information': information,
        'contact_form' : form,
        'message' : success_message
    }
    return render(request, 'contact_us/contact_us.html', context)
