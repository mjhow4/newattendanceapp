from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Case
from .forms import CaseForm, CreateUserForm

# Create your views here.

def registerPage(request):
       # if request.user.is_authenticated:
        #     return redirect('index')
        # else:
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user) 

            return redirect('login')

    context = {'form':form}
    return render(request, "attend/registerPage.html", context)

def loginPage(request):
        # if request.user.is_authenticated:
        #     return redirect('index')
        # else:

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'Username OR password is incorrect')
        

    context = {}
    return render(request, "attend/loginPage.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def list_cases(request):
    cases = Case.objects.all()
    return render(request, "attend\list_cases.html",
                  {"cases": cases})

@login_required(login_url='login')
def lista_cases(request):
    cases = Case.objects.all()
    return render(request, "attend\lista_cases.html",
                  {"cases": cases})

def listp_cases(request):
    cases = Case.objects.all()
    return render(request, "attend\listp_cases.html",
                  {"cases": cases})

def index(request):
    return render(request, "attend\index.html",)

def signup(request):
    return render(request, "attend\signup.html",)

def submit(request):
    return render(request, "attend\submit.html",)

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
            return redirect(to='submit')

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


 
