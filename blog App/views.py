from django.shortcuts import render
from django.http import HttpResponse

# Import Models

# Counts
from django.db.models import Count

# Create your views here.
##############################################

def index(request):

    title = "Blog"

    context = {
        "title":title,
    }
    return render(request, 'blog/index.html', context)

##############################################