from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    full_name = models.CharField(_("Full Name"), max_length=255)
    email = models.EmailField(_("Email Address"))
    subject = models.CharField(_("Subject"), max_length=255)
    message = models.TextField(_("Message"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

    def get_absolute_url(self):
        # If you have a detail view for contacts
        from django.urls import reverse
        return reverse('contact_detail', kwargs={'pk': self.pk})
