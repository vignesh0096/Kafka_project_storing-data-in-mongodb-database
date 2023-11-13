from django.db import models
from .mongodb import db

collection = db['kafka_django']
