from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from .models import Article


def signup_view(request):
    if request.method == 'POST':
        # check the form validation
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            # appName:approute name
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
