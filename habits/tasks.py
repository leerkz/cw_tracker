from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from habits.models import Habits
from habits.services import send_tg_message, is_today


@shared_task
def send_remind():
    date = now().date()
    time = now().time()

    for habit in Habits.objects.all():

        habit_time = timedelta(
            hours=habit.time.hour,
            minutes=habit.time.minute,
            seconds=habit.time.second
        ).total_seconds()

        current_time = timedelta(
            hours=time.hour,
            minutes=time.minute,
            seconds=time.second
        ).total_seconds()

        if abs(habit_time - current_time) < 60:
            if is_today(habit.periodicity, habit.user.date_joined.date(), date) and habit.user.chat_id:
                message = f"It is time for'{habit.action}' in {habit.place}."
                print(habit.user.chat_id)
                send_tg_message(habit.user.chat_id, message)