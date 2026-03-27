import os
from django.shortcuts import render


def index(request):
    context = {
        "firebase_api_key": os.environ.get("FIREBASE_API_KEY", ""),
    }
    return render(request, "index.html", context)
