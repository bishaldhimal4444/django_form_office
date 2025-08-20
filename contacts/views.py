# from django.shortcuts import render

# # Create your views here.


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! We received your message.")
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_list(request):
    contacts = Contact.objects.order_by('-created_at')
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})
