from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NoteForm
from .models import new_note

# Create your views here.
def index(request):
  notes = new_note.objects.all()
  context = {
    'notes' : notes,
  }
  return render(request, 'my_app/index.html', context)

def about(request):
  context = {}
  return render(request, 'my_app/about.html', context)

def add_note(request):
  if request.method == 'POST':
    form = NoteForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  else:
    form = NoteForm()
  return render(request, 'my_app/add_note.html', {'form' : form} )