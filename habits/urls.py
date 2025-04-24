from django.urls import path
from habits.views import HabitViewSet

app_name = 'habits'

habit_list = HabitViewSet.as_view({'get': 'list', 'post': 'create'})
habit_detail = HabitViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

urlpatterns = [
    path('', habit_list, name='habit-list'),
    path('<int:pk>/', habit_detail, name='habit-detail'),
    path('', HabitViewSet.as_view({'get': 'list'}), name='habit-list'),
    path('<int:pk>/', HabitViewSet.as_view({'get': 'retrieve'}), name='habit-detail'),
]
