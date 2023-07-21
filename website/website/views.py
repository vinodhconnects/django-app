from django.shortcuts import render

  
# create a function 
def home_view(request): 

    return render(request,'whome.html', context={'appname':'ABC inc'})