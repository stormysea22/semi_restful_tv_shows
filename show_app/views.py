from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.contrib import messages
from .models import Show

# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "shows" : Show.objects.all()
    }
    return render(request, "shows.html", context)

def new_show(request):

    return render(request, "shows_new.html")

def show_create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/shows/new")
    else:
        show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description'],
        )
        return redirect(f"/shows/{show.id}")

def show_display(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id)
    }
    return render(request, "show_display.html", context)

def show_update(request, show_id):
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(f"/shows/{show_id}/edit")
        else:
            show = Show.objects.filter(pk=show_id).update(
                title = request.POST['title'],
                network = request.POST['network'],
                release_date = request.POST['release_date'],
                description = request.POST['description'],
            )
            return redirect(f"/shows/{show_id}")

def show_edit(request, show_id):
    show = Show.objects.get(id=show_id)
    show.release_date = show.release_date.strftime('%Y-%m-%d')
    context = {
        "show" : show
    }
    return render(request, "shows_edit.html", context)

def show_delete(request, show_id):
    show = Show.objects.get(id=show_id).delete()
    return redirect("/shows")