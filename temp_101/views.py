from http.client import HTTPResponse
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict as MTD
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from temp_101.forms import BlogForm
from temp_101.models import Blog


def index(request):
    print(Blog.objects.all().values('id', 'title', 'description'))
    return render(request, 'temp_101/index.html', {
        'blogs': Blog.objects.all()
    })


# def blog_create(request):
#     blog_form = BlogForm(request.POST or None)
#     if request.method == 'POST' and blog_form.is_valid():
#         blog_form.save()
#         messages.success(request, 'blog created successfully!')
#         return redirect('index')

#     return render(request, 'temp_101/blog_create.html', {
#         'form': blog_form
#     })


# def blog_view(request, id):
#     blog = Blog.objects.get(id=id)
#     blog_form = BlogForm(request.POST or None, instance=blog)
#     if request.method == 'POST' and blog_form.is_valid():
#         blog_form.save()
#         messages.success(request, 'blog updated successfully!')
#         return redirect('index')

#     return render(request, 'temp_101/blog_update.html', {
#         'form': blog_form
#     })


# def blog_delete(request, id):
#     blog = Blog.objects.get(id=id)
#     blog.delete()
#     messages.success(request, 'blog deleted successfully!')
#     return redirect('index')


# def blog_render(request, id):
#     blog = Blog.objects.get(id=id)
#     return render(request, 'temp_101/partials/blog.html', {
#         'blog': blog
#     })


# def blog_partial_create(request):
#     title = request.POST.get('title')
#     desc = request.POST.get('description')
#     blog = Blog(
#         title=title,
#         description=desc
#     )

#     blog.save()
#     return render(request, 'temp_101/partials/blog.html', {
#         'blog': blog
#     })


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


# def blog_partial_bupdate(request, id):
#     blog = Blog.objects.get(id=id)
#     return render(request, 'temp_101/partials/blog_update.html', {
#         'blog': blog
#     })


# def blog_partial_delete(request, id):
#     blog = Blog.objects.get(id=id)
#     blog.delete()
#     return HttpResponse('')


# def blog_partial_delete_all(request):
#     inputs = request.POST.getlist('id')
#     Blog.objects.filter(id__in=inputs).delete()
#     response = HttpResponse('')
#     response['HX-Redirect'] = reverse('index')
#     return response





def save_blog(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
    title = data.get("title", "")
    description = data.get("description", "")
    print(title)
    blog = Blog(
        title=title,
        description=description,
    )
    blog.save()
    blog = MTD(blog)
    return JsonResponse(json.dumps(blog), safe=False)

def get_blogs(request):
    blogs = Blog.objects.all()
    actual_blogs = []
    for blog in blogs:
        actual_blogs.append(MTD(blog))
    return JsonResponse(json.dumps(list(actual_blogs)), safe=False)

def delete_blog(request, id):
    blog = Blog.objects.get(id = id)
    blog.delete()
    return HttpResponse(status=204)
    
def update_blog(request, id):
    blog = Blog.objects.get(id=id)
    data = json.loads(request.body)
    title = data['title']
    description = data['description']
    blog.title = title
    blog.description = description
    blog.save()
    return HttpResponse(status=204)