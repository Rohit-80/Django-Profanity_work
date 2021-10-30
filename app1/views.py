from django.shortcuts import render
from django.http import HttpResponse
from requests_html import HTMLSession
from better_profanity import profanity
from .forms import*

def Home(request):
	if request.method == "POST":
		form = InputForm(request.POST)
		if form.is_valid():
			url = form.cleaned_data["link"]
			session = HTMLSession()
			req = session.get(url)
			post = req.html.find('.post-body', first=True)
			filter_data = profanity.censor(post.text)
			print(filter_data)

			context = {
				"form": form,
				"filter_data": filter_data,
			}
			return render(request, 'app1/home.html', context)
	else:
	    form = InputForm()

	context = {
	    'form': form,
	}
	return render(request, 'app1/home.html', context)