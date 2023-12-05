from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    home_page = models.URLField(max_length=512, null=True, blank=True)

    def __str__(self) -> str:
        return self.username.__str__()


class Commentary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Commentaries"

    def __repr__(self) -> str:
        return f"<Commentary from {self.user.username} at {self.created}>"

    def __str__(self) -> str:
        return self.body if len(self.body) < 80 else self.body[:80] + "..."

    def get_comments(self):
        return Commentary.objects.filter(parent=self).prefetch_related("user")
