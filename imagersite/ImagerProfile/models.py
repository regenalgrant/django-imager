"""Models."""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

CAMERA_TYPES = (
    ('canon', 'Canon'),
    ('nikon', 'Nikon'),
    ('sony', 'SONY')
)

PHOTOGRAPHY_TYPES = (
    ('nature', 'Nature'),
    ('photography', 'Photograpy/Newborn'),
    ('6 Months', '6 Months'),
    ('baby Pics', 'Baby Pics'),
    ('maternity', 'Maternity'),
    ('babies', 'Babies')
)

class ActiveUserManager(models.Manager):
    """Query ImagerProfile of active user."""

    def get_querysets(self):
        """Return query set of profiles for active users."""
        query = super(ActiveUserManager, self).get_querysets()
        return query.filter(user__is_active__exact=True)


class ImagerProfile(models.Model):
    """Creating profile linked to user."""

    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    type_camera = models.CharField(default='', max_length=35, choices=CAMERA_TYPES, blank=True, null=True)
    type_photography = models.CharField(default='', max_length=35, choices=PHOTOGRAPHY_TYPES, blank=True, null=True)
    employable = models.BooleanField(default=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    bio = models.CharField(max_length=800, blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    travel_radius = models.IntegerField(blank=True, null=True)
    imager_id = models.UUIDField(default=uuid.uuid4, editable=False)
    active = ActiveUserManager()
    objects = models.Manager()

customer = models.ForeignKey(ImagerProfile)
        User,
        related_name="User",
        blank=True,
        null=True
        )
RESERVATION = [
    ("available", "Available"),
    ("confirmed", "Confirmed"),
    ("date", "Date"),
    ("time", "time"),
]
status = model.CharField(
    max_length=20
    choices=RESERVATION,
    default="availble"
)


    def __str__(self):
        return self.user.username


@property
def is_active(self):
    """This is active property."""
    return self.user.is_active


@receiver(post_save, sender=User)
def make_user_profile(sender, instance, **kwargs):
    """Instantiate a PatronProfile, connect to a new User instance, save that profile."""
    new_profile = ImagerProfile(user=instance)
    new_profile.save()
