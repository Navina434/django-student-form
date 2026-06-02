from django.shortcuts import render
from .forms import StudentForm

def student_form(request):

    success = False

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()     
            success = True

            form = StudentForm()

    else:
        form = StudentForm()

    return render(
        request,
        'student_form.html',
        {
            'form': form,
            'success': success
        }
    )
