from django.db import models
from user.models import HWFUser

def user_directory_path(instance, filename):
    return 'media/font/{0}/{1}'.format(instance.owner.nickname, filename)

class Font(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    created_date = models.DateField(auto_now_add=True)
    like_users = models.ManyToManyField(HWFUser, blank=True, related_name='like')
    owner = models.ForeignKey(HWFUser, related_name='font', on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)

    @property
    def like_num(self):
        return self.like_users.count()

    def __str__(self):
        return self.name
    