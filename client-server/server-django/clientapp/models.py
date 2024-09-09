from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(self.user.id, filename)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return "profile {}".format(self.user.username)


class WorkSession(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    paused = models.BooleanField(default=False)
    pause_time = models.DateTimeField(null=True, blank=True)
    machine = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee.name} from {self.start_time} to {self.end_time if self.end_time else 'Ongoing'}"

    def duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        if self.paused and self.pause_time:
            return self.pause_time - self.start_time
        return timezone.now() - self.start_time
