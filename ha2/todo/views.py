from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from .models import List
from .forms import ListForm
from django.contrib import messages


# Create your views here.
def impressum(request):
    return render(request, 'impressum.html')


def howto(request):
    return render(request, 'howto.html')


class UpdateView(generic.UpdateView):
    model = List
    form_class = ListForm
    template_name = 'list_update.html'


def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            print(all_items)
            messages.success(request, ('Item added'))
            return render(request, 'table.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, "table.html", {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    return redirect('index')
