from django.http import JsonResponse
from django.shortcuts import render
from .utils import get_hot_post, get_new_post, get_top_post, get_redditor_by_username

# Create your views here.
def hello_reddit(request):
    return JsonResponse({"reddit": "hello there"})


def get_post(request):
    if request.GET:
        sub = request.GET.get("sub")
        category = "top"
        res = get_top_post(sub)
        if request.GET.get("category"):
            category = request.GET.get("category")
            if category == "new":
                res = get_new_post(sub)
            elif category == "hot":
                res = get_hot_post(sub)
            else:
                JsonResponse({"response": "incorrect inputs"})
        return JsonResponse(res.to_dict())
    return JsonResponse({"get_post": "insufficient inputs"})


def get_redditor(request):
    if request.GET:
        username = request.GET.get("username")
        redditor = get_redditor_by_username(username)
        return JsonResponse(redditor.to_dict())
    return JsonResponse({"get_post": "insufficient inputs"})
