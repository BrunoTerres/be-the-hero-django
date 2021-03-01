from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views import generic


from hero.models import Ngo

def index(request):
    return render(request, 'hero/home.html')

def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "hero/upload.html")


class NgoListView(generic.ListView):
    model = Ngo
    context_object_name = 'ngo_list'
    queryset = Ngo.objects.all()
    template_name = "hero/ngo_list.html"


class NgoDetailView(generic.DetailView):
    model = Ngo
    template_name = 'hero/ngo_detail.html'

class NgoCreate(CreateView):
    model = Ngo
    fields = '__all__'


class NgoUpdate(UpdateView):
    model = Ngo
    fields = '__all__'

class NgoDelete(DeleteView):
    model = Ngo
    success_url = reverse_lazy('ngo_list')