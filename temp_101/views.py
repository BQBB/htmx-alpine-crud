from http.client import HTTPResponse
import json
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from temp_101.forms import BlogForm
from temp_101.models import Blog


def index(request):
    print(Blog.objects.all().values('id', 'title', 'description'))
    return render(request, 'temp_101/index.html', {
        'blogs': Blog.objects.all()
    })


def blog_create(request):
    josn_body = json.loads(request.body)
    if not josn_body['title'] or not josn_body['description']:
        return JsonResponse({'status': 400, 'message': 'title or description is empty!'})
    blog = Blog.objects.create(title=josn_body['title'], description=josn_body['description'])
    if blog:
        return JsonResponse({'status': 201, 'message': 'blog created successfully!'})
    return JsonResponse({'status': 400, 'message': 'blog not created!'})


def blog_view(request, id):
    blog = Blog.objects.get(id=id)
    blog_form = BlogForm(request.POST or None, instance=blog)
    if request.method == 'POST' and blog_form.is_valid():
        blog_form.save()
        messages.success(request, 'blog updated successfully!')
        return redirect('index')

    return render(request, 'temp_101/blog_update.html', {
        'form': blog_form
    })


def blog_delete(request, id):
    try:
        blog = Blog.objects.get(id=id)
        blog.delete()
        return JsonResponse({'status': 204, 'message': 'blog deleted successfully!'})
    except:
        return JsonResponse({'status': 400, 'message': 'blog not deleted!'})

def blog_update(request, id):
    blog = Blog.objects.filter(id=id)
    json_body = json.loads(request.body)
    if blog:
        if not json_body['title'] or not json_body['description']:
            return JsonResponse({'status': 400, 'message': 'title or description is empty!'})
        blog.update(title=json_body['title'] , description=json_body['description'])
        return JsonResponse({'status': 200, 'message': 'blog updated successfully!'})
    return JsonResponse({'status': 400, 'message': 'blog not updated!'})

def blog_render(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'temp_101/partials/blog.html', {
        'blog': blog
    })


def blog_render_all(request):
    blogs = Blog.objects.all().values('id', 'title', 'description')
    return JsonResponse(list(blogs), safe=False)


def blog_partial_create(request):
    title = request.POST.get('title')
    desc = request.POST.get('description')
    blog = Blog(
        title=title,
        description=desc
    )

    blog.save()
    return render(request, 'temp_101/partials/blog.html', {
        'blog': blog
    })


# def blog_partial_aupdate(request, id):
#     print(request.POST)
#     blog = Blog.objects.get(id=id)
#     title = request.POST.get('title')
#     desc = request.POST.get('description')
#     blog.title = title
#     blog.description = desc
#     blog.save()
#     return render(request, 'temp_101/partials/blog.html', {
#         'blog': blog
#     })
#
#
# def blog_partial_bupdate(request, id):
#     blog = Blog.objects.get(id=id)
#     return render(request, 'temp_101/partials/blog_update.html', {
#         'blog': blog
#     })


def blog_partial_delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return HttpResponse('')


def blog_partial_delete_all(request):
    inputs = request.POST.getlist('id')
    Blog.objects.filter(id__in=inputs).delete()
    response = HttpResponse('')
    response['HX-Redirect'] = reverse('index')
    return response
