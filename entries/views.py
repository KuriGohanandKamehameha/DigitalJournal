from django.shortcuts import render
from .models import Entry


# Create your views here.
def home(request):
    entries = Entry.objects.all().order_by('-date')
    return render(request, 'entries/home.html', {'entries': entries})
