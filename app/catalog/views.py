import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#require login to function based view
from django.contrib.auth.decorators import login_required, permission_required
#require login to class based view
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.models import Incident, Ngo
#from catalog.forms import RenewBookForm


def index(request):
    """
    View function for home page of site.
    """

    # Generate counts of some of the main objects 
    num_incidents = Incident.objects.all().count()
    num_ngos = Ngo.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_incidents': num_incidents,
        'num_ngos': num_ngos,
    }

    return render(request, 'catalog/index.html', context=context)

#@login_required
#@permission_required('catalog.can_mark_returned', raise_exception=True)
#def renew_book_librarian(request, pk):
#    book_instance = get_object_or_404(BookInstance, pk=pk)
#
#    # If this is a POST request then process the Form data
#    if request.method == 'POST':
#
#        # Create a form instance and populate it with data from the request (binding):
#        form = RenewBookForm(request.POST)
#
#        # Check if the form is valid:
#        if form.is_valid():
#            # Process the data in form.cleaned_data as required (here we just write it to the model due_back field).
#            book_instance.due_back = form.cleaned_data['renewal_date']
#            book_instance.save()
#
#            # Redirect to a new URL:
#            return HttpResponseRedirect(reverse('borrowed-books'))
#    # If this is a GET (or any other method) create the default form
#    else: 
#        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
#
#    context = {
#        'form': form,
#        'book_instance': book_instance,
#    }
#
#    return render(request, 'catalog/book_renew_librarian.html', context)


class IncidentListView(generic.ListView):
    model = Incident
    context_object_name = 'incident_list'
    queryset = Incident.objects.all()
    template_name = "catalog/incident_list.html"
    paginate_by = 10


class IncidentDetailView(generic.DetailView):
    model = Incident
    template_name = "catalog/incident_detail.html"


class NgoListView(generic.ListView):
    model = Ngo
    context_object_name = 'ngo_list'
    queryset = Ngo.objects.all()
    template_name = "catalog/ngo_list.html"
    paginate_by = 10


class NgoDetailView(generic.DetailView):
    """
    Generic class-based detail view for an author.
    """
    model = Ngo
    template_name = "catalog/ngo_detail.html"


#class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
#    """
#    Generic class-based view listing books on loan to current user
#    """
#    model = BookInstance
#    template_name = "catalog/bookinstance_list_borrowed_user.html"
#    paginate_by = 10
#
#    def get_queryset(self):
#        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
    

#class LoanedBooksListView(PermissionRequiredMixin, generic.ListView):
#    model = BookInstance
#    permission_required = 'catalog.can_mark_returned'
#    template_name = "catalog/bookinstance_list_borrowed.html"
#
#    def get_queryset(self):
#        return BookInstance.objects.filter(status__exact='o').order_by('due_back')
#
#"""
#For this kind of Class Based View the Django expects a Template name with a certain pattern
#Ex: for a BookCreateView it expects a template as 'book_form.html' or 'MODEL_form.html
#For a BookDeleteView it expects a template as 'book_confirm_delete.html' or 'MODEL_confirm_delete.html'
#It dispenses you set a 'template_name' in this view case. If you don't follow the pattern you shoud to point a 'template_name'
#"""


class NgoCreate(CreateView):
    model = Ngo
    fields = ['name', 'email', 'description', 'whatsapp', 'city', 'ur']

class NgoUpdate(UpdateView):
    model = Ngo
    fields = ['name', 'email', 'description', 'whatsapp', 'city', 'ur']  # '__all__'  Not recomended (Potential security issue if more fields added)

class NgoDelete(PermissionRequiredMixin ,DeleteView):
    model = Ngo
    success_url = reverse_lazy('ngos')

class IncidentCreateView(CreateView):
    model = Incident
    fields = ['title', 'ngo', 'description', 'value']

class IncidentUpdateView(UpdateView):
    model = Incident
    fields = '__all__' 

class IncidentDeleteView(DeleteView):
    model = Incident
    success_url = reverse_lazy('incidents')


