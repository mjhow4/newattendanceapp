from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Case
from .forms import CaseForm

# Create your views here.
def list_cases(request):
    cases = Case.objects.all()
    return render(request, "attend\list_cases.html",
                  {"cases": cases})

def delete_pages(request, pk):
    album = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        page.delete()
        return redirect(to='list_pages')

    return render(request, "pages/delete_pages.html",
                  {"page": page})                  