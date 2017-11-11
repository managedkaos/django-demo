from django.shortcuts import render

# Create your views here.
def bare(request):
    return render(request, 'bare/index.html')

