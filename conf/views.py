from django.shortcuts import render

def main_page(request):
    return render(request, 'main_page.html')

def prior_knowledge(request):
    return render(request, 'prior_knowledge.html')