from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''Hello Sir <a href=" https://www.google.com/"> Google</a>''')


def removepunc(request):
    djtext = request.POST.get('text', 'defaultdata')
    djremovepunc = request.POST.get('removepunc', 'off')
    extraspace = request.POST.get('extraspaceremove', 'off')
    newline = request.POST.get('newlineremove', 'off')
    capital = request.POST.get('capitalize', 'off')
    countchar = request.POST.get('charcount', 'off')
    analized = " "
    punc_list = '''!()[]{}-;:\,/<>.'"?#@$&^%*_~'''
    if djremovepunc == "on":
        for char in djtext:
            if char not in punc_list:
                analized = analized + char

        djtext = analized
        analized = ""

    if extraspace == 'on':
        for ind, char in enumerate(djtext.strip()):
            if djtext[ind] == " " and djtext[ind + 1] == " ":
                pass
            else:
                analized = analized + char

        djtext = analized
        analized = ""

    if newline == 'on':
        for char in djtext:
            if char != "\n" and char != '\r':
                analized = analized + char
        djtext = analized
        analized = ""

    if capital == 'on':

        for char in djtext:
            analized = analized + char.upper()

        djtext = analized

    if countchar == 'on':
        counter = 0
        linecount = 0
        for char in djtext:
            if char == '\n':
                linecount += 1
            elif char == " ":
                pass
            else:
                counter += 1

        counter -= linecount
        analized = "Total Number of character: " + str(counter)
        djtext = djtext + "\n" + analized

    params = {"purpose": "Remove Punctutaions", "analized_text": djtext}
    return render(request, 'analize.html', params)
