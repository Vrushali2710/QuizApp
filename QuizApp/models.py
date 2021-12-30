import random
from django.db import models
from django.core.files import File

import uuid,os

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True ,default=uuid.uuid4,editable=False)
    created_at =models.DateField(auto_now_add=True)
    updated_at =models.TimeField(auto_now_add=True)

    class Meta:
        abstract =True

class Course(BaseModel):
    course_name = models.CharField(max_length=100)
    schedul_date =models.DateField(null="True",blank="True")

    def __str__(self)->str:
        return self.course_name

class Question(BaseModel):
    course = models.ForeignKey(Course,related_name='course', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks =models.IntegerField(default=1)
    image=models.ImageField(upload_to = 'quiz/images', default = ' ')
    def __str__(self) -> str:
        return self.question
   
    def get_answers(self):
        answer_objs =list(Answer.objects.filter(question =self))
        random.shuffle(answer_objs)
        data = []
        for answer_obj in answer_objs:
            data.append({
                'answer':answer_obj.answer,
                'is_correct':answer_obj.is_correct
            })
        return data
class Answer(BaseModel):
    question =models.ForeignKey(Question,related_name='question_answer',on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct =models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.answer
    
   
