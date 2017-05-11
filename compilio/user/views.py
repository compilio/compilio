from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from registration.forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('login'))

    else:
        form = RegistrationForm()

    return render(request, 'user/register.html', {'form': form})
