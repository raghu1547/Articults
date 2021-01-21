from django.urls import path,re_path

from . import views

#app_name = "posts"

app_name = 'posts'

urlpatterns = [
    path('',views.PostList.as_view(),name='all'),
    path('new/',views.CreatePost.as_view(),name='create'),
    path('search/',views.PostList.searchart,name='search'),
    path('byuser',views.user_post_list,name='user_post_list'),
    # re_path(r'^by/(?P<username>[-\w]+)$',views.user_post_list,name='for_user'),
    re_path(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    re_path(r'^delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name='delete'),
    path('bycovid/',views.Group1Posts.as_view(),name="g1"),
    path('byastronomy/',views.Group2Posts.as_view(),name="g2"),
    path('byscience/s',views.Group3Posts.as_view(),name="g3"),
    path('bymedicalsciences/',views.Group4Posts.as_view(),name="g4"),
    path('bytechnology/',views.Group5Posts.as_view(),name="g5"),
    path('byeconomics/',views.Group6Posts.as_view(),name="g6"),
]
