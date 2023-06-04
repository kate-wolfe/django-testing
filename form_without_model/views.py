from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from .forms import SetupForm
from .traverse import traverse, loadJSON, newPath


def setup_form_view(request):
    if request.method == "POST":
        form = SetupForm(request.POST)
        if form.is_valid():
            # print("primitive:", form.cleaned_data["primitive"])
            # print("path:", form.cleaned_data["map_path"])
            global obj
            newObj = newPath(obj, request.POST)
            obj, objType = traverse(newObj)
            return render(
                request,
                "setup.html",
                {"form": form, "obj": obj, "objType": objType},
            )
        else:
            form = SetupForm()
        return render(
            request, "setup.html", {"form": form, "obj": obj, "objType": objType}
        )
    else:
        form = SetupForm()
        item = loadJSON()
        obj, objType = traverse(item)
        return render(
            request, "setup.html", {"form": form, "obj": obj, "objType": objType}
        )
