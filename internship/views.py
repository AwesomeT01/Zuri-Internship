from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
        
    context = {'form': form}

    return render(request, 'internship/base.html', context )