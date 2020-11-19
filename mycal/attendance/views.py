from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Case
from .forms import CaseForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users

# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            title = form.cleaned_data.get('first_name')
            messages.success(request, 'Account was created for ' + username) 
            if title == 'Defense Attorney':
                group = Group.objects.get(name="Defense Attorney")
                user.groups.add(group)
            elif title == 'District Attorney':
                group = Group.objects.get(name="Court Official")
                user.groups.add(group)
            elif title == 'Court Clerk':
                group = Group.objects.get(name="Court Official")
                user.groups.add(group)
            
            return redirect('login')

    context = {'form':form}
    return render(request, "attend/registerPage.html", context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('hub')

        else:
            messages.info(request, 'Username OR password is incorrect')
        

    context = {}
    return render(request, "attend/loginPage.html", context)

def userPage(request):
    context = {}
    return render(request, 'attend/user.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'Court Official'])
def list_cases(request):
    cases = Case.objects.all()
    return render(request, "attend\list_cases.html",
                  {"cases": cases})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'Defense Attorney'])
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

def pal(request):
    return render(request, "attend\pal.html",)

def hub(request):
    return render(request, "attend\hub.html",)       

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


    


 