from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action in ['list']:
            return Habits.objects.filter(is_public=True)
        return Habits.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return [IsOwner()]
        return super().get_permissions()
