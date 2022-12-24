import json
from django.middleware.csrf import get_token

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from temp_101.models import Blog


def index(request):
    return render(request, 'temp_101/index.html')

@require_http_methods(['GET'])
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


@require_http_methods(['GET'])
def getBlogs(request):
    try:
        a = Blog.objects.values('id', 'title', 'description')
        return JsonResponse(json.dumps(list(a)), safe=False)
    except:
        return HttpResponse(status=401)


@require_http_methods(['POST'])
def blog_create(request):
    try:
        data = json.loads(request.body)
        Blog.objects.create(title=data['title'], description=data['description']).save()
        a = Blog.objects.values().last()
        return JsonResponse(json.dumps(a), safe=False)
    except:
        return HttpResponse(status=405)

@require_http_methods(['PUT'])
def blog_update(request, id):
    try:
        blog = Blog.objects.get(id=id)
        data = json.loads(request.body)
        title = data['title']
        description = data['description']
        blog.title = title
        blog.description = description
        blog.save()
        return HttpResponse(status=204)
    except:
        return HttpResponse(status=405)

@require_http_methods(['DELETE'])
def blog_delete(request, id):
    try:
        blog = Blog.objects.get(id=id)
        blog.delete()
        messages.success(request, 'blog deleted successfully!')
        return HttpResponse(status=204)
    except:
        return HttpResponse(status=405)
