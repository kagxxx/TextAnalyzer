from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')


    # check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    # which checkbox is marked
    if removepunc=="on":
        punctuations = '''!()_{}[]:;'"\,<>.?/@#$%^&*-~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'removed punctuation', 'analyzed_text': analyzed}
        djtext = analyzed



    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (spaceremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        params = {'purpose': 'remove space', 'analyzed_text': analyzed}
        djtext = analyzed


    if (extraspaceremover == "on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index+1] == " "):
                    analyzed = analyzed + char
            params = {'purpose': 'remove extra space', 'analyzed_text': analyzed}
            djtext = analyzed

    if(charactercounter == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            analyzed = index
        params = {'purpose': 'count total number of character', 'analyzed_text': analyzed}


    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and spaceremover!="on" and extraspaceremover!="on" and charactercounter!="on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)

