# coding: utf-8

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'index.html', {})


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'profile.html', {})

@login_required
def ssh(request):
    autenticao = request.user.social_auth.get()
    # return (dir(request.auth))

