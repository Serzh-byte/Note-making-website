from django.shortcuts import render

def home(request):
    topics = ['Machine Learning', 'Statistics', 'Data Science', 'AI']
    if request.method == 'POST':
        return render(request, 'notes/home.html', {'topics':topics})
    return render(request, 'notes/home.html', {'topics':topics})