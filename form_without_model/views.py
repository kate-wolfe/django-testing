from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from .forms import SetupForm


def setup_form_view(request):
    if request.method == "POST":
        form = SetupForm(request.POST)
        if form.is_valid():
            print("primitive:", form.cleaned_data["primitive"])
            print("path:", form.cleaned_data["map_path"])

            return HttpResponseRedirect("/")
        else:
            form = SetupForm()
        return render(request, "setup.html", {"form": form})
    else:
        form = SetupForm()
        return render(request, "setup.html", {"form": form})
