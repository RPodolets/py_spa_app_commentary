from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128),
    email = models.EmailField()

    def __str__(self) -> str:
        return self.username.__str__()


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"<Commentary from {self.user.username} at {self.created}>"
