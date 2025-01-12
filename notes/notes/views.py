from . import render

def home(request):
    if request.method == 'POST':
        return render(request, 'notes/home.html')
    return render(request, 'notes/home.html')