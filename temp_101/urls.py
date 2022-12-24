from django.urls import path, include

from temp_101 import views
urlpatterns = [
    path('', views.index, name="index"),
    # path('blog/create/', views.blog_create, name="blog-create"),
    # path('blog/update/<id>/', views.blog_view, name="blog-update"),
    # path('blog/delete/<id>/', views.blog_delete, name="blog-delete"),
    # path('blog/render/<id>/', views.blog_render, name="blog-render"),
    # path('blog/partial-create/', views.blog_partial_create, name="blog-partial-create"),
    # path('blog/partial-bupdate/<id>/', views.blog_partial_bupdate, name="blog-partial-bupdate"),
    # path('blog/partial-aupdate/<id>/', views.blog_partial_aupdate, name="blog-partial-aupdate"),
    # path('blog/partial-delete/<id>/', views.blog_partial_delete, name="blog-partial-delete"),
    # path('blog/partial-delete-all/', views.blog_partial_delete_all, name="blog-partial-delete_all"),
    path('blogs/', views.save_blog, name="save_blog"),
    path('get_blogs/', views.get_blogs, name="get_blogs"),
    path('delete_blog/<int:id>', views.delete_blog, name="delete_blog"),
    path('update_blog/<int:id>', views.update_blog, name="update_blog"),
]