from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()
    wordic={}
    for word in wordcount:
        if word in wordic:
            wordic[word] += 1
        else:
            wordic[word] = 1
    # wordic = wordic.items()
    wordic = sorted(wordic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordcount), 'wordic':wordic})

def about(request):
    return render(request, 'about.html')
