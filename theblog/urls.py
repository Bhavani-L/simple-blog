from django.urls import path
from .views import HomeView,ArticleDetailedView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView, CategoryListView,LikeView

urlpatterns = [
    # path('',views.home,name='home'),
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailedView.as_view(),name='article-details'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('artile/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('artile/delete/<int:pk>',DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category_list/',CategoryListView,name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
]