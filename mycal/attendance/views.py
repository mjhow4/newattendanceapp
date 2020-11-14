from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Case
from .forms import CaseForm

# Create your views here.
def list_cases(request):
    cases = Case.objects.all()
    return render(request, "attend\list_cases.html",
                  {"cases": cases})

def lista_cases(request):
    cases = Case.objects.all()
    return render(request, "attend\lista_cases.html",
                  {"cases": cases})

def index(request):
    return render(request, "attend\index.html",)

def signup(request):
    return render(request, "attend\signup.html",)

# def edita_case(request):
#     return render(request, "attend\edita_case.html",)

def contact(request):
    return render(request, "attend\contact.html",)
        

def add_case(request):
    if request.method == 'GET':
        form = CaseForm()
    else:
        form = CaseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_cases')

    return render(request, "attend/add_case.html", {"form": form})

def edit_case(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'GET':
        form = CaseForm(instance=case)
    else:
        form = CaseForm(data=request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect(to='list_cases')

    return render(request, "attend/edit_case.html", {
        "form": form,
        "case": case,
    })

def edita_case(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'GET':
        form = CaseForm(instance=case)
    else:
        form = CaseForm(data=request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect(to='lista_cases')

    return render(request, "attend/edita_case.html", {
        "form": form,
        "case": case,
    })


def delete_case(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'POST':
        case.delete()
        return redirect(to='list_cases')

    return render(request, "attend/delete_case.html",
                  {"case": case})   


 