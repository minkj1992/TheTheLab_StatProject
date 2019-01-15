from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')
def about(request):
    return render(request, 'wordcount/about.html')
def count(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dict = {}

    for word in text:
        if word in word_dict: word_dict[word] +=1 
        else: word_dict[word] = 1

    return render(request, 'wordcount/count.html', {'fulltext': text, 'total':len(words), 'dict': word_dict.items()})

def index(request):
    return render(request,'wordcount/index.html')

def elements(request):
    return render(request,'wordcount/elements.html')
