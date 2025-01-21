from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def home(request):
    notes = Note.objects.all()

    return render(request, 'notes/home.html', {'notes':notes })

def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # Redirect to the list of notes (adjust URL name as needed)
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})

def specific(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, 'notes/specific_note.html', {'note': note})