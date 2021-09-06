from django.db import models
from django.contrib.auth.models import User

class userdata1(User):
    Address=models.CharField(max_length=300)
