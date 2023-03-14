from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("<h1><center>file system</center></h1>")
