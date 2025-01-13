from django.shortcuts import render
from portfolio_app.models import Project

# Homepage view
def home(request):
    return render(request, 'portfolio_app/home.html')

# Projects page view
def projects(request):
    all_projects = Project.objects.all()  # Retrieve all projects from the database
    return render(request, 'portfolio_app/projects.html', {'projects': all_projects})

# Contact page view
def contact(request):
    return render(request, 'portfolio_app/contact.html')
