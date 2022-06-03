from django.shortcuts import render, HttpResponse, redirect
from home.models import *
from home.forms import NoteForm, NoteModelForm
from home.models import Note
from django.contrib import messages

# Create your views here.
def homepage(request):
    user = request.user
    notes = []
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=user)
    context = {
        'notes': notes,
    }
    return render(request, 'home/index.html', context)


def add_note(request):
    if request.method == 'POST':
        form = NoteModelForm(request.POST)

        if form.is_valid():
            user = request.user
            heading = form.cleaned_data.get('heading')
            tags = form.cleaned_data.get('tags')
            content = form.cleaned_data.get('content')

            note = Note(
                user=user,
                heading=heading,
                tags=tags,
                content=content,
            )
            note.save()
            messages.success(request, f"Successfully created note : {note.heading}")
            return redirect(homepage)

    else:
        form = NoteModelForm()

    return render(request, 'home/add_note.html', {'form': form})


def edit_note(request, note_id):
    if not note_id:
        return redirect(homepage)
    note, created = Note.objects.get_or_create(id=note_id)
    if created:
        note.delete()
        return redirect(homepage)
    if request.method == 'POST':
        form = NoteModelForm(request.POST, instance=note)

        if form.is_valid():
            # user = request.user
            # heading = form.cleaned_data.get('heading')
            # tags = form.cleaned_data.get('tags')
            # content = form.cleaned_data.get('content')
            #
            # new_note = Note(
            #     user=user,
            #     heading=heading,
            #     tags=tags,
            #     content=content,
            # )
            # new_note.save()
            # Note.objects.filter(id=note_id).delete()
            form.save()
            messages.info(request, f"Successfully updated note: {note.heading}")
            return redirect(homepage)

    else:
        form = NoteModelForm(instance=note)

    return render(request, 'home/edit_note.html', {'form': form, 'note_id': note_id})


def delete_note(request, note_id=None):
    if not note_id:
        return redirect(homepage)

    note = Note.objects.get(id=note_id)
    note.delete()

    messages.warning(request, "Successfully deleted note")

    return redirect(homepage)


def search_tags(request):
    if request.method == 'POST':
        key = request.POST.get('tag')
        if key == "":
            return redirect(homepage)

    return redirect
