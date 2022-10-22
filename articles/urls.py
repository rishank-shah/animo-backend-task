from django.urls import path
from .views import ArticleAPIView, ArticleDetailView

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('article-detail/<int:id>', ArticleDetailView.as_view()),
]