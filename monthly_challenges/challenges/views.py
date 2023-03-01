from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

challenges_text = {
    'january': "Drink no alcohol for the entire month",
    'february': "Learn Python for at least 30 minutes a day",
    'march': "Eat no meat for the entire month",
    'april': "Try cooking a new recipe each week",
    'may': "Learn Django for at least 30 minutes a day",
    'june': "Learn Django for at least 30 minutes a day",
    'july': "Learn Django for at least 30 minutes a day",
    'august': "Learn Django for at least 30 minutes a day",
    'september': None,
    'october': "Learn Django for at least 30 minutes a day",
    'november': "Learn Django for at least 30 minutes a day",
    'december': "Have a very merry Christmas!"  ,
}


def index(request):
    months = list(challenges_text.keys())

    return render(request, 'challenges/index.html', {
        'months': months,
    })


def monthly_challenge_by_num(request, month):
    try:
        redirect_month = list(challenges_text.keys())[month-1]
    except IndexError:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = challenges_text[month]
        return render(request, "challenges/challenge.html", {
            'month': month,
            'text': challenge_text,
        })
    except KeyError:
        raise Http404()

