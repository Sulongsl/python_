from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse


# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]  # 根据时间倒序从数据库获取了5条数据
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)


def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)  #
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")
	print("****" * 10)
	return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
# 	response = "You're looking at the results of question %s."
# 	return HttpResponse(response % question_id)


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# 发生choice未找到异常时，重新返回表单页面，并给出提示信息
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id): # 处理结果函数
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})
