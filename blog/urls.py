from django.contrib import admin
from django.urls import path
from django.conf.urls import url
# from .views import PostView,PostDetailView,PostCreateView,UserLoginView,HomeView
from .views import HomeView,postview,postdetailview,postcreate,postupdate,postdeleteview

urlpatterns = [
	# path('posts/',PostView.as_view(),name='listview'),
	# url(r'^(?P<pk>\d+)/$',PostDetailView.as_view(),name='DetailView'),
	# path('create/',PostCreateView.as_view(),name='create'),
	path('',HomeView.as_view(),name='blog'),
	path('home/',HomeView.as_view(),name='homeview'),
	path('posts/',postview.as_view(),name='postview'),
	path('posts/create',postcreate.as_view(),name='postcreate'),
	path('posts/update/<int:pk>/',postupdate.as_view(),name='postupdate'),
	path('posts/<int:pk>/',postdetailview.as_view(),name='detailview'),
	path('posts/delete/<int:pk>/',postdeleteview.as_view(),name='deleteview'),


	# path('login/',UserLoginView.as_view()),
    # path('admin/', admin.site.urls),

]
