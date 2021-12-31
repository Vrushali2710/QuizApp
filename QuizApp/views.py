from django.shortcuts import redirect, render
from .models import *
from django.http import JsonResponse,HttpResponse
import random

# Create your views here.

def home(request):
    courses = Course.objects.all()
    context = {"courses":courses}

       
   
    if request.GET.get('course'):

        return redirect(f"/quiz/?course={request.GET.get('course')}")
    return render(request,'home.html',context)
def quiz(request):
    context ={'course':request.GET.get('course')}

    return render(request,'quiz.html',context)
def get_quiz(request):
    try:
        question_objs =Question.objects.all()
       
    
        if request.GET.get('course'):
           
            question_objs = question_objs.filter(course__course_name__icontains=request.GET.get('course'))
        question_objs = list(question_objs)
      
        data =[]
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                "uid":question_obj.uid,
                "course":question_obj.course.course_name,
                "question":question_obj.question,
                "marks":question_obj.marks,
                "image":question_obj.image.url,
                "answers":question_obj.get_answers(),
             })
        payload ={'status':True,'data':data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
        return HttpResponse("something went wrong")
