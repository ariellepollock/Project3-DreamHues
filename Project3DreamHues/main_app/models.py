from django.db import models

from datetime import date
# Create your models here.
FEELING = (
  # for a dropdown menu in regards to feeling of dream
  ('G', 'Good'),
  ('O', 'Okay'),
  ('N', 'Not Good'),
  ('B', 'Bad')
)

TYPE = (
  ('N', 'Nightmare')
  ('A', 'Amazing')
  ('W', 'Weird')
)


class Dreams(models.Model):
  date = models.DateField('Date of Dream')
  name = models.CharField(max_length=100)
  about = models.TextField(max_length=500)
  feeling = models.CharField(
    max_length=1,
    choices=FEELING,
    default=FEELING[0][0]
  )
  dream_type = models.CharField(
    max_length=1,
    choices=TYPE,
    default=TYPE[0][1]
  )
