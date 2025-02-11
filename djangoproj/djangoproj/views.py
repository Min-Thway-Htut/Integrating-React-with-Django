from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# re_path(r"",views.index,name="index")