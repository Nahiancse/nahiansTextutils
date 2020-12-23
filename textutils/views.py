#this file is made by nahian

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def analyze(request):


    txt=request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    cntchars= request.POST.get('cntchars', 'off')
    rmvnewline= request.POST.get('rmvnewline', 'off')
    allcaps= request.POST.get('allcaps', 'off')

    if removepunc=='on':
        punctuations= '''@#$%&,./""''{}()[]!-'''
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed=analyzed+char

        params= {'purpose' : 'Removed Punctuations', 'analyzed_text':analyzed}
        txt=analyzed


    if allcaps=='on':
        analyzed=''
        for char in txt:
            analyzed+=char.upper()
        params = {'purpose': 'changed to upper case', 'analyzed_text': analyzed}
        txt = analyzed
        # return render(request, 'analyze.html', params)



    if cntchars=='on':

        c=len(txt)
        params = {'purpose': 'removing new line', 'analyzed_text': f'number of character in your text is {c}'}

    if rmvnewline=='on':

        analyzed=''
        for char in txt:
            analyzed+=char.rstrip('\n')
        params = {'purpose': 'removing new line', 'analyzed_text': analyzed}
        txt = analyzed
        # return render(request, 'analyze.html', params)

    if removepunc!='on' and cntchars!='on' and rmvnewline!='on' and allcaps!='on':
        return HttpResponse('please select any operation and try again')


    return render(request, 'analyze.html', params)

