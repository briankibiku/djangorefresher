from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='posts_home'),
    path('greet/', view=views.greet, name='greet_name'),
    path('posts/', view=views.all_posts, name='all_posts'),
    path('posts/<int:post_id>/', view=views.single_post, name='one_post'),
    path('about/', view=views.about, name='posts_about'),
    path('services/', view=views.services, name='posts_services'),
]
