from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from habits.models import Habits
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitsList(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsOwner]
    pagination_class = HabitPaginator


class HabitsDetail(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsOwner]


class HabitsCreate(CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitsUpdate(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsOwner]


class HabitsDestroy(DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsOwner]


class PublicHabitsList(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.filter(is_public=True)