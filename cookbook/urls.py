from django.urls import path
from .views import HomeView, RecipeDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', HomeView.as_view(), name="home"),
	path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipe-detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)