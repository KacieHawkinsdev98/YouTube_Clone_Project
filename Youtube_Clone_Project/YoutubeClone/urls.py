from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentsList.as_view()),
    path('comments/<int:pk>/', views.CommentsDetail.as_view()),
    path('reply/', views.ReplySection.as_view()),
]