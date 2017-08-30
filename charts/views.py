from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from collections import Counter
from tokens.models import Token, Date
from vocabs.models import SkosConcept, SkosConceptScheme

DATA = {"status": "ok",
        "query": "api:graph",
        "timestamp": "2016-07-21T09:56:36.803Z",
        "items": "7",
        "title": "LASK4EVER",
        "subtitle": "This is just a test to check if everythin works as expected.",
        "legendx": "Club",
        "legendy": "# of Victories",
        "measuredObject": "Victories",
        "ymin": -10,
        "payload": [
            ["LASK", 10],
            ["Real Madrid", 4],
            ["Rapid Wien", 0],
            ["Blau Weiß Linz", -10]
        ]
        }

DATA_PIECHART = {
    "items": "2",
    "title": "LASK4EVER",
    "subtitle": "This is just a test.",
    "measuredObject": "# of Victories",
    "payload": [
        ["LASK", 9], ["Blau Weiß Linz", 1]
    ]
}


def linecharts_view(request):
    context = {"test": "test"}
    return render(request, 'charts/line_charts.html', context)


def barcharts_view(request):
    context = {"test": "test"}
    return render(request, 'charts/bar_charts.html', context)


def piecharts_view(request):
    context = {"test": "test"}
    return render(request, 'charts/pie_charts.html', context)


def test_json(request):
    data = DATA
    return JsonResponse(data)


def test_json_pie(request):
    data = DATA_PIECHART
    return JsonResponse(data)


def tokens_per_genre(request):
    payload = []
    scheme = SkosConceptScheme.objects.get(dc_title='ecce-genre')
    genres = SkosConcept.objects.filter(scheme=scheme)
    for x in genres:
        amount = len(Token.objects.filter(text_source__genre=x))
        payload.append([x.pref_label, amount])

    data = {
        "items": Token.objects.all().count(),
        "title": "Tokens per genres",
        "subtitle": "Tokens per genre",
        "legendx": "Genres",
        "legendy": "# of Tokens",
        "measuredObject": "Tokens",
        "ymin": 0,
        "payload": payload
    }

    return JsonResponse(data)


def tokens_per_genre_static(request):
    data = {"measuredObject": "Tokens", "legendy": "# of Tokens", "title": "Tokens per genres", "payload": [["LETTERS_PRIV", 2260], ["FICTION", 3324], ["EDUC_TREATISE", 2237], ["LETTERS_NON-PRIV", 1335], ["BIBLE", 11060], ["SCIENCE_OTHER", 1708], ["PHILOSOPHY", 3289], ["HISTORY", 24427], ["BIOGRAPHY_OTHER", 1178], ["SCIENCE_MEDICINE", 783], ["RULE", 3888], ["RELIG_TREATISE", 46654], ["HANDBOOK_ASTRO", 913], ["SERMON", 18577], ["PHILOSOPHY/FICTION", 2152], ["BIOGRAPHY_LIFE_OF_SAINT", 3687], ["RELIG_TRREATISE", 1895], ["HANDBOOK_MEDICINE", 1002], ["HOMILY", 13500], ["ROMANCE", 8541], ["TRAVELOGUE", 7425], ["HOMILY_POETRY", 5509], ["HANDBOOK_OTHER", 3152], ["DIARY_PRIV", 2396], ["PROCEEDINGS_TRIAL", 2223], ["DRAMA_COMEDY", 1869], ["BIOGRAPHY_AUTO", 644], ["LAW", 1753]], "items": 177400, "ymin": 0, "subtitle": "Tokens per genre", "legendx": "Genres"}
    return JsonResponse(data)


def tokens_per_semicentury(request):
    payload = []
    payload_line = []
    dates = set([x.semicentury for x in Date.objects.all()])
    for x in sorted(dates):
        amount = len(Token.objects.filter(text_source__mean_date__semicentury=x))
        payload.append(["{}".format(x), amount])
        payload_line.append(amount)

    data = {
        "items": len(Token.objects.all()),
        "title": "Tokens per semicentury",
        "subtitle": "Tokens per semicentury",
        "legendx": "Semicentury",
        "legendy": "# of Tokens",
        "categories": sorted(dates),
        "measuredObject": "Tokens",
        "ymin": 0,
        "payload": payload,
        "payload_line": payload_line
    }

    return JsonResponse(data)


def tokens_per_decade(request):
    payload = []
    payload_line = []
    dates = set([x.decade for x in Date.objects.all()])
    for x in sorted(dates):
        amount = len(Token.objects.filter(text_source__mean_date__decade=x))
        payload.append(["{}".format(x), amount])
        payload_line.append(amount)

    data = {
        "items": len(Token.objects.all()),
        "title": "Tokens per decade",
        "subtitle": "Tokens per decade",
        "legendx": "Decade",
        "legendy": "# of Tokens",
        "categories": sorted(dates),
        "measuredObject": "Tokens",
        "ymin": 0,
        "payload": payload,
        "payload_line": payload_line
    }

    return JsonResponse(data)


def tokens_per_dates(request):
    payload = []
    payload_line = []
    dates = set([x.dates for x in Date.objects.all()])
    for x in sorted(dates):
        amount = len(Token.objects.filter(text_source__mean_date__dates=x))
        payload.append(["{}".format(x), amount])
        payload_line.append(amount)

    data = {
        "items": len(Token.objects.all()),
        "title": "Tokens per years",
        "subtitle": "Tokens per years",
        "legendx": "Year",
        "legendy": "# of Tokens",
        "categories": sorted(dates),
        "measuredObject": "Tokens",
        "ymin": 0,
        "payload": payload,
        "payload_line": payload_line
    }

    return JsonResponse(data)
