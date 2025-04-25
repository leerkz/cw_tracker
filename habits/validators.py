import re
from datetime import timedelta
from rest_framework import serializers

from habits.models import Habits


class LimitLeadTime:
    def __init__(self, max_minutes=120):
        self.max_duration = timedelta(minutes=max_minutes)

    def __call__(self, data):
        lead_time = data.get('lead_time')

        if lead_time:
            match = re.match(r'(\d+)\s*minutes?', lead_time)
            if match:
                minutes = int(match.group(1))
                lead_td = timedelta(minutes=minutes)
                if lead_td > self.max_duration:
                    raise serializers.ValidationError("Lead time exceeds 120 minutes.")
            else:
                raise serializers.ValidationError("Invalid lead_time format. Use like '10 minutes'.")

# class RelatedOrReward:
#     def __call__(self, data):
#         if data.get('related_habit') and data.get('reward'):
#             raise serializers.ValidationError("Нельзя одновременно указывать related_habit и reward.")
#
#
# class ValidRelated:
#     def __call__(self, data):
#         related_habit = data.get('related_habit')
#
#         if related_habit:
#             try:
#                 habit = Habits.objects.get(id=related_habit)
#             except Habits.DoesNotExist:
#                 raise serializers.ValidationError(f"Habit with id {related_habit} does not exist.")