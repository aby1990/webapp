from django.contrib import messages
from django.shortcuts import render
from openlabs.forms import DetailsForm
from openlabs.models import Details


def portfolio(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            check_email = Details.objects.filter(email=email)
            if check_email:
                messages.error(request,"Email is already exist please enter another one.")
            else:
                form.save()
                messages.success(request,"Information save.")
        else:
            messages.error(request,"Encountered error. Cannot save data.")
    return render(request, 'portfolio.html', {'form': DetailsForm()}) 
