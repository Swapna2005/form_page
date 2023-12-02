from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from .models import MovieModel
from .forms import MovieForm

# def members(request):
    
#     movie_data = {[ 
                
#             {
#                 'title': 'pulimurugan',
#                 'year': 2018,
#                 'success': False
#             },
#             {
#                 'title': 'titanic',
#                 'year': 2005,
#                 'summary': 'story of underworld',
#                 'success': False
#             },
#             {
#                 'title': 'love in the air',
#                 'year': 2003,
#                 'summary': 'story of tiger',
#                 'success': False
#             },
#             {
#                 'title': 'together',
#                 'year': 2019,
#                 'summary': 'story of tiger',
#                 'success': False
#             }
#         ]
#     }
    
#     template = loader.get_template("hello.html")
#     return HttpResponse(template.render(movie_data, request))

# def home_view(request):
#     context = {}
#     form = SignupForm(request.POST or None, request.FILES or None)    
#     if form.is_valid():
#         form.save()
#     context['form']= form
#     return  render(request,"hello.html",context) 
    
def text_view(request):
    context = {}
    form = MovieForm(request.POST or None, request.FILES or None)    
    if form.is_valid():
        form.save()
    context['form']= form
    return  render(request,"hey.html",context) 