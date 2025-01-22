from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def home(request):
    notes = Note.objects.all()

    return render(request, 'notes/home.html', {'notes':notes })

def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST) #creates a form instance
        if form.is_valid():
            form.save() # saves the form in the db
            return redirect('home') 
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})

def specific(request, id):
    note = get_object_or_404(Note, id=id) #gets the SPECIFIC note, using the id
    return render(request, 'notes/specific_note.html', {'note': note}) 

def delete_note(request, id):
    if request.method == "POST":
        note = get_object_or_404(Note, id=id)
        note.delete()
        return redirect('home')
    return render(request, 'notes/delete_note.html', {'note_id': id})

def edit_note(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save() 
            return redirect('home')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/edit_note.html', {'form': form, 'note': note}) 