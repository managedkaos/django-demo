from django.shortcuts import render

# Create your views here.
def bootstrap_template(request):
    return render(request, 'bootstrap_template/index.html')

