from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse


def contact(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']

            print(name, email )
            return HttpResponse(f"Hello {name}. Welcome to Learn Share IT")
    form = UserForm()
    return render(request, 'form.html', {'form':form})