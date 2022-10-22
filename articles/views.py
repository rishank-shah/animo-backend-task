from django.shortcuts import render
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class ArticleAPIView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(APIView):
    
    def get(self, request, id):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, id = id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, id):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, id = id)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request, id):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, id = id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)