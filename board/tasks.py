from celery import shared_task
from .models import Order
import time
@shared_task
def hello():
    time.sleep(10)
    print('Hello, World!')