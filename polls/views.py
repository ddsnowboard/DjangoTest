from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question, Choice
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	return render(request, "polls/index.html", {'latest_question_list':Question.objects.order_by("-pub_date")[:5]})
def detail(request, question_id):
	q = get_object_or_404(Question, pk=question_id)
	return render(request, "polls/details.html", {'question': q})	
def results(request, question_id):
	q = Question.objects.get(pk=question_id)
	return render(request, 'polls/results.html', {'question': q})
def vote(request, question_id):
	q = get_object_or_404(Question, pk=question_id)
	try:
		choice = q.choice_set.get(pk=request.POST['choice'])
	except (IndexError, Choice.DoesNotExist):
		return render(request, "polls/details.html", {'error_message':"You didn't pick a choice", 'question':q})
	else:
		choice.votes += 1
		choice.save()
		return HttpResponseRedirect(reverse("polls:results", args=(q.id,)))
		
