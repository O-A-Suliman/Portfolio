from django.shortcuts import render

def index(request):
    """الصفحة الرئيسية - نبذة عني مع صورة شخصية"""
    context = {}
    return render(request, "Marketer/index.html", context)

def education(request):
    """صفحة التعليم والشهادات"""
    context = {}
    return render(request, "Marketer/education.html", context)

def projects(request):
    """صفحة المشاريع"""
    context = {}
    return render(request, "Marketer/projects.html", context)

def certificates1(request):
    """صفحة الشهادات 1"""
    context = {}
    return render(request, "Marketer/certificates1.html", context)

def certificates2(request):
    """صفحة الشهادات 2"""
    context = {}
    return render(request, "Marketer/certificates2.html", context)
