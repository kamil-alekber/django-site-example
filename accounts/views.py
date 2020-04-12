from django.shortcuts import render
# from .models import Article


def signup_view(request):
    return render(request, 'accounts/signup.html')
