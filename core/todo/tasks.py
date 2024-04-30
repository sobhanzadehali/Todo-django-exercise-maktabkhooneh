from celery import shared_task
from todo.models import Task

@shared_task
def deleteTodos():
    ts = Task.objects.all()
    if ts:
        for i in ts:
            i.delete()
        print('tasks deleted')
    else:
        print("nothing to delete!")