from django.urls import path
from .views import (
    CourseView,
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    # path('', my_fbv, name='courses-list'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
]