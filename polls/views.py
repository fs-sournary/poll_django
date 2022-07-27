from typing import Union
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from polls.models import Question


def index(request) -> HttpResponse:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(
        request=request,
        template_name='polls/index.html',
        context={'latest_question_list': latest_question_list},
    )


def detail(request, question_id: int) -> Union[HttpResponse, Exception]:
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request=request,
        template_name='polls/detail.html',
        context={'question': question},
    )


def results(request, question_id: int) -> HttpResponse:
    return HttpResponse(
        f"You're looking at the results of question {question_id}")


def vote(request, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}")
