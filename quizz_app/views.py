from django.shortcuts import render,redirect
from django.contrib.auth .decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from quizz_app.models import *

@login_required
def home(request):
    objects_list = Section_test.objects.all().order_by('-id')
    return render(request,'quizz_app/index.html',{'objects_list':objects_list})

@login_required
def quizz(request,id):
    context = {}
    context['section_test'] = Section_test.objects.get(id=id)
    context['quizz'] = Questions.objects.filter(section_id=context['section_test'])
    page = request.GET.get('page', 1)
    paginator = Paginator(context['quizz'], 1)
    try:
        context['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        context['object_list'] = paginator.page(1)
    except EmptyPage:
        context['object_list'] = paginator.page(paginator.num_pages)
    return render(request,'quizz_app/quizz.html',context)