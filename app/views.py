from django.shortcuts import render

# Create your views here.
def jinjaprinting(request):
    d={'name':'kavya','age':22,'male':'female'}
    return render(request,'jinjaprinting.html',context=d)
