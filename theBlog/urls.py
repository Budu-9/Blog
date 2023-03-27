from django.urls import path
#from . import views
from .views import HomePage, PostDetail, PostPage, EditPage, DeletePost, CategoryPage, Categories, Category_list, LikePage,ShowProfilePage, CommentPage

urlpatterns = [
    #path('',views.home, name = "home"),
    path('', HomePage.as_view(), name = "home"),
    path('postdetail/<int:pk>', PostDetail.as_view(), name = "post_detail"),
    path('addpost/', PostPage.as_view(), name = "addpost"),
    path('addcategory/', CategoryPage.as_view(), name = "addcategory"),
    path('postdetail/edit/<int:pk>', EditPage.as_view(), name = "post_edit"),
    path('postdetail/delete/<int:pk>', DeletePost.as_view(), name = "delete_post"),
    path('categories/<str:cats>', Categories, name = "categories"),
    path('category-list/', Category_list, name = "category-list"),
    path('like/<int:pk>', LikePage, name = "like_post"),
    path('<int:pk>/profile/', ShowProfilePage.as_view(), name = 'profile_page'),
    path('article/<int:pk>/comment', CommentPage.as_view(), name = "comment_page"),
    
]