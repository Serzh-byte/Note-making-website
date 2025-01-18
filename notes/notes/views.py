from django.shortcuts import render

def home(request):
    topics = ['Machine Learning', 'Statistics', 'Data Science', 'AI']
    texts = ['Intro to Machine Learning', 'Basics of Statistics', 'Overview of Data Science', 'AI Trends']

    # Zipping topics and texts to make them a list of tuples or dictionaries
    topics_texts = zip(topics, texts)  # Creating pairs of topic and text

    return render(request, 'notes/home.html', {'topics_texts': topics_texts})
