from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitsList, HabitsCreate, HabitsUpdate, HabitsDestroy, HabitsDetail, PublicHabitsList

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitsList.as_view(), name='habit-list'),
    path('create/', HabitsCreate.as_view(), name='habit-create'),
    path('update/<int:pk>', HabitsUpdate.as_view(), name='habit-update'),
    path('detail/<int:pk>', HabitsDetail.as_view(), name='habit-detail'),
    path('delete/<int:pk>', HabitsDestroy.as_view(), name='habit-delete'),
    path('public/', PublicHabitsList.as_view(), name='habit-public'),
]
