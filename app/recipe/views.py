"""
Views for the recipe apis
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeDetailSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        """Return the serializer class for request"""
        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class