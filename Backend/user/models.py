from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    
    return './storage/user_{0}/{1}'.format(instance.user.id, filename)

class Document(models.Model):
    name = models.CharField(max_length=100)
    docfile = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documents',on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.docfile.delete()
        super().delete(*args, **kwargs)

class Counter(models.Model):
    count = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Counter',on_delete=models.CASCADE)