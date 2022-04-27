from django.urls import path
from . import views

urlpatterns = [
   path('', views.news_home, name='news_home'),
   path('create', views.create, name='create'),
   path('authorize', views.authorize, name='authorize'),
   path('comments', views.comments, name='comments'),
   path('<int:pk>/update', views.NewUpdateView.as_view(), name='news_update'),
   path('<int:pk>/delete', views.NewDeleteView.as_view(), name='news_delete'),
   path('courses', views.courses, name='courses'),
   path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail')
]