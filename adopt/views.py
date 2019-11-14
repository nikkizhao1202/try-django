from django.http import HttpResponse
import random

def index(requests):
    i = random.random()
    return HttpResponse(f'Hi! How are you !!!{i}')

