from django.shortcuts import render
import os

# Create your views here.
def index(request):
    return render(request, "index.html", {"firebase_api_key": os.environ.get("FIREBASE_API_KEY")})
