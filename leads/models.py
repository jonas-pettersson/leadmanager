from django.db import models
from django.utils.translation import gettext as _


class Lead(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    message = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Lead")
        verbose_name_plural = _("Leads")

    def __str__(self):
        return self.name
