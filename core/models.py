from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating created and modified fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """ Custom model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Save a User with the given email and password."""
        if not email:
            raise ValueError('email must be provided')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    CLIENT = 1
    WRITER = 2
    ROLE_CHOICES = (
        (CLIENT, 'Client'),
        (WRITER, 'Writer'),
    )
    RATE_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=False, null=True)
    name = models.TextField(null=False, default='')
    surname = models.TextField(null=False, default='')
    phone_number = models.TextField(null=False, default='')
    rating = models.PositiveSmallIntegerField(
        choices=RATE_CHOICES, blank=False, null=True)

    objects = UserManager()


class JobType(TimeStampedModel):
    name = models.TextField(null=False, default='')

    class Meta:
        verbose_name_plural = 'Job Types'

    def __str__(self):
        return self.name


class PremiumJob(TimeStampedModel):
    name = models.TextField(null=False, default='')
    price = models.FloatField(null=False, default=0.0)

    class Meta:
        verbose_name_plural = 'Premium jobs'

    def __str__(self):
        return self.name


class Subject(TimeStampedModel):
    name = models.TextField(null=False, default='')

    class Meta:
        verbose_name_plural = 'Subject Types'

    def __str__(self):
        return self.name


class Order(TimeStampedModel):
    """
        Order
    """
    PENDING = 1
    APPROVED = 2
    ACCEPTED = 3
    AMENDS_REQUESTED = 4
    REJECTED = 5
    STATUS_CHOICES = (
        (PENDING, 'pending'),
        (APPROVED, 'Approved'),
        (ACCEPTED, 'Accepted'),
        (AMENDS_REQUESTED, 'Amends_requested'),
        (REJECTED, 'Rejected')
    )

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, related_name="created_by")
    job_type = models.ForeignKey(
        JobType, on_delete=models.CASCADE, null=False, related_name="job_type")
    premium_job = models.ForeignKey(
        PremiumJob, on_delete=models.CASCADE, null=False, related_name="premium_job")
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=False, related_name="subject")
    word_count = models.IntegerField(null=False, default=10)
    company = models.TextField(null=False, default='')
    company_url = models.TextField(null=False, default='')
    keywords = models.TextField(null=False, default='')
    deadline = models.DateTimeField()
    brief = models.TextField(null=False, default='')
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, blank=False, null=True)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.subject
