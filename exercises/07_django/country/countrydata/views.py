from django.http import Http404, HttpResponse
import json

from .models import Continent, Country


def continent_json(request, continent_code):
    """ Write your answer in 7.2 here. """
    try:
        continent = Continent.objects.get(code=continent_code).countries.all()
    except Continent.DoesNotExist:
        raise Http404("Continent not found")
    jsonRes = json.dumps({x.code: x.name for x in continent})
    callback = request.GET.get('callback', '')
    if callback == "":
        return HttpResponse(jsonRes, content_type="application/json")
    else:
        return HttpResponse('%s(%s)' % (callback, jsonRes), content_type="application/json")


def country_json(request, continent_code, country_code):
    """ Write your answer in 7.2 here. """

    try:
        continent = Continent.objects.get(code=continent_code)
        try:
            country = Country.objects.get(code=country_code,continent_id=continent.id)

        except Country.DoesNotExist:
            raise Http404("Country not found")
    except Continent.DoesNotExist:
        raise Http404("Continet not found")
    jsonRes = json.dumps({"area": country.area, "population": country.population, "capital": country.capital})
    callback = request.GET.get('callback', '')
    if callback == "":
        return HttpResponse(jsonRes, content_type="application/json")
    else:
        return HttpResponse('%s(%s)' % (callback, jsonRes), content_type="application/json")
