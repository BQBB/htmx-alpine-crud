from typing import List
from django.shortcuts import get_object_or_404, HttpResponse
from ninja import Router
from temp_101.models import Blog
from temp_101.schema import BlogSchema, BlogIn, SuccessSchema, ErrorSchema

router = Router(tags=['blog'])


@router.get("/", response=List[BlogSchema])
def get_all_blogs(request):
    blogs = Blog.objects.all()
    return blogs


@router.post("/", response={200: SuccessSchema, 404: ErrorSchema})
def create_blog(request, payload: BlogIn):
    try:
        blog = Blog.objects.create(**payload.dict())
        blog.save()
        return 200, {
            "message": "Ok"
        }
    except Exception as e:
        return 400, {
            "message": f"{e}"
        }


@router.delete("/{blog_id}", response={200: SuccessSchema, 404: ErrorSchema})
def delete_blog(request, blog_id: int):
    try:
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.delete()
        return 200, {
            "message": "Ok"
        }
    except Exception as e:
        return 404, {
            "message": f"{e}"
}


@router.put("/", response={200: SuccessSchema, 404: ErrorSchema})
def update_blog(request, payload: BlogSchema):
    try:
        blog = get_object_or_404(Blog, pk=payload.id)
        for key, value in payload.dict().items():
            setattr(blog, key, value)
        blog.save()
        return 200, {
            "message": "Ok"
        }
    except Exception as e:
        return 404, {
            "message": f"{e}"
}
