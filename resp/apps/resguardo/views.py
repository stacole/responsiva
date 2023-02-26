from django.shortcuts import render
from .forms import ResguardosForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
    else:
        form = ResguardosForm()
    context = {
        'form': form,
    }
    return render(request, "resguardo/home.html", context)

def responsivas(request):
    return render(request, "resguardo/responsivas.html")