from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sps')
    else:
        form = ContactForm()

    return render(request, 'c_app/contact_form.html', {'form': form})


def sps_view(request):
    form = ContactMessage.objects.all()
    return render(request, 'c_app/sps.html',{'form': form})