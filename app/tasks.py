import random
import string

from celery import shared_task
from .models import SuperModel


@shared_task
def create_new_object():
    random_name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    random_counter = random.randint(1, 100)
    new_object = SuperModel.objects.create(name=random_name, counter=random_counter)
    return new_object.name, new_object.counter

