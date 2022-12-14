from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    Function to get the main page
    """
    return render(request, 'contact.html')


def contact_view(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            messages.success(request, 'Thank you for your message.\
                 We will contact you soon.')
            try:
                send_mail(subject, message, from_email, ["office@remember.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")

    return render(request, "contact/contact.html", {"form": form})


def success_view(request):
    """
    A view to render the success page once the information has been captured
    """
    return render(request, 'contact/success.html')
