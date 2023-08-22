from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import FileResponse
import datetime

# Create your views here.
def landing(request):
    return render(request, 'dashboard/landing.html')


