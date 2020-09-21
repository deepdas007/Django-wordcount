from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fullText = request.GET['fulltext']
    word_count = fullText.split()
    word_repeat = {}

    for words in word_count:
        if words in word_repeat:
            word_repeat[words] += 1

        else:
            word_repeat[words] = 1

    sortedWords = sorted(word_repeat.items(), key=operator.itemgetter(1))

    return render(request, 'count.html', {'fulltext': fullText, 'tot_wrds': len(word_count), 'sortedWords': sortedWords})


def about(request):
    return render(request, 'about.html')
