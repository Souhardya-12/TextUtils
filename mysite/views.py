from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
"""
def index(request):
    f = open("C:/Users/Admin/cwhdjp1/mysite/mysite/yes.txt",'r')
    c = f.read()
    return HttpResponse(c+'''<br><a href="http://127.0.0.1:8000/reader">reader's place</a><br><a href="http://127.0.0.1:8000/writer">writer's place</a>''')


def about(request):
    return render(request, 'about.html')
    #return HttpResponse('''<h1>You are in Writer</h1><br><a href="/">Homepage</a>''')

def reader(request):
    dtext = request.GET.get('text', 'default')
    print(dtext)
    return HttpResponse('''<h1>You are in reader</h1><br><a href="/">Homepage</a>''')
"""
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    dtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    nlremove = request.POST.get('nlremove', 'off')
    esremove = request.POST.get('esremove', 'off')
    ccount = request.POST.get('ccount', 'off')
    stext = dtext
    analyzed = ""
    analyzed1 = ""
    analyzed2 = ""
    analyzed3= ""
    i = 0
    x = 0
    if removepunc == "on":
        punc = '''!()-[];,}{:'<>/."\?@#$%^&*_~'''
        for char in dtext:
            if char not in punc:
                analyzed = analyzed+char
        dtext = analyzed
    
    if capitalize=="on":
        for char in dtext:
            analyzed1 = analyzed1+char.upper()
        dtext = analyzed1
    
    if nlremove=="on":
        for char in dtext:
            if char is not "\n" and char is not "\r":
                analyzed2 = analyzed2+char
            dtext = analyzed2

    if esremove=="on":
        for i, char in enumerate(dtext):
            if not(dtext[i]==" " and dtext[i+1]==" "):
                analyzed3 = analyzed3+char
    
    if ccount=="on":
        for char in stext:
            i+=1
        x = str(i)

    paramas = {
        'removepunc': removepunc,
        'capitalize': capitalize,
        'nlremove': nlremove,
        'esremove': esremove,
        'ccount': ccount,
        'analyzed': analyzed,
        'analyzed1': analyzed1,
        'analyzed2': analyzed2,
        'analyzed3': analyzed3,
        'x': x,
    }

    return render(request, 'analyze.html', paramas)