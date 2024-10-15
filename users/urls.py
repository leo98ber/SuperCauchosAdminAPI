"""User and Profile URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'persons', user_views.PersonViewSet, basename='persons')
# router.register(r'user', user_views.UserProfileViewSet, basename='profiles')
# router.register(r'professionals', ProfessionalViewSet, basename='professionals')
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('<int:pk>/enable_user/', user_views.UserProfileViewSet, name='enable_user'),
# ]
