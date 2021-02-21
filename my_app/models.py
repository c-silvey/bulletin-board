from django.db import models

class new_note(models.Model):
  alias = models.CharField(max_length=20)
  note = models.TextField()
  timestamp = models.DateField(auto_now_add=True)

  def __srt__(self):
    return self.alias