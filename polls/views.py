from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404

def index(request): 
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})

def results(request, question_id):
    get_question = get_object_or_404(Question, pk=question_id)
    list_result = get_question.choice_set.all()
    return render(request, "polls/results.html", {'question': get_question, 'choices': list_result})

# def vote(request, question_id):
#     question = get_object_or_404(Question, )
#     return HttpResponse("You're voting on question %s." % question_id)
