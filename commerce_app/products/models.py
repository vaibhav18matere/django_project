from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class ChaiVariety(models.Model):
    #     CHAI_TYPE_CHOICE = [
    #     ("ML", "MASALA"),
    #     ("EL", "ELAICHI"),
    #     ("GN", "GINGER"),
    #     ("GT", "GREENTEA"),
    # ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    # type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

# One to Many Relationship - Chai and ots reviews

class ChaiReviews(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE) # CASCADE: When the chai is deleted, the reviews are also deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE: When the user is deleted, the reviews are also deleted
    review = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.chai.name}"

# Many to Many Relationship - Chai and Stores

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores') # Many to Many: A store can sell many chai varieties and a chai variety can be sold in many stores
    # phone = models.CharField(max_length=15)
    # email = models.EmailField()
    # website = models.URLField()
    # date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# One to One Relationship - Chai and Cup

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    # date_expired = models.DateTimeField(default=timezone.now)
    # certificate_type = models.CharField(max_length=100)
    # certificate_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.chai.name} - {self.certificate_number}"