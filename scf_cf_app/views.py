from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['name'] = form.cleaned_data.get('name')
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'form.html', {'form' : form})

def success(request):
    name = request.session.get('name')
    return render(request, 'success.html', {'name' : name})