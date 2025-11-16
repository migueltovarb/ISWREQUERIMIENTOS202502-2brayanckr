from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import vehiculo
from .forms import VehicleForm

def create_view(request):
    context = {}
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context['form'] = form
    return render(request, "create_view.html", context)

def list_view(request):
    context = {}
    context["dataset"] = vehiculo.objects.all()
    return render(request, "list_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(vehiculo, id=id)
    form = VehicleForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context['form'] = form
    return render(request, "update_view.html", context)