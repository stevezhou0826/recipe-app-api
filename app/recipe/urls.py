"""
URLs for recipe app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'
urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )