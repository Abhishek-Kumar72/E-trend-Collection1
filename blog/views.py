from django.shortcuts import render
from blog.models import Post    
#posts=[
#{    
 #   'author':'Alok',
 #   'title':'blog post 1',
 #   'content':'potography is very easy nowadays...',
 #   'data_posted':'october 28,2012'
 #   },
 #   {
 #   'author':'harish',
 #   'title':'blog post 2',
#  'content':'politics is very good for student...',
#    'data_posted':'october 29,2012'  
#    },
#    {
#    'author':'Alok',
#    'title':'blog post 1',
#    'content':'potography is very easy nowadays...',
#    'data_posted':'october 28,2012'
#    }

#]

def index(request):
    context={'p':Post.objects.all(),'user':'navnit'}
    return render(request,"blog/home.html",context)

def about(request):
    return render(request,"blog/about.html",{'title':'about'})
