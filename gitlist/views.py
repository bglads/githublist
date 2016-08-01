from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from list_issues import get_issues
import json

def index(request):
    return render(request, 'issues.html')


def issues(request):
    url=request.POST.get("url")
    return HttpResponse(json.dumps(get_issues(url)),content_type='application/json')
