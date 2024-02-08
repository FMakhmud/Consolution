from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Banner(models.Model):
    subtitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner/')
    link = models.URLField()

    def __str__(self):
        return self.subtitle


class Static(BaseModel):
    student_count = models.PositiveBigIntegerField(default=0)
    universities_count = models.PositiveBigIntegerField(default=21)
    years_of_experienced = models.IntegerField()
    countries_count = models.PositiveBigIntegerField(default=5)

    def __str__(self):
        return str(self.student_count)


class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Result(BaseModel):
    full_name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    image = models.ImageField(upload_to='result/')

    def __str__(self):
        return self.full_name


class Contact(BaseModel):
    class DegreeChoice(models.TextChoices):
        BACHELOR = "BACHELOR", "Bachelor"
        MASTER = "master", "Master"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.TextField(blank=True)
    degree = models.CharField(max_length=100, choices=DegreeChoice.choices,
                              default=DegreeChoice.BACHELOR)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Review(BaseModel):
    full_name = models.CharField(max_length=100)
    characterization = models.TextField(blank=True)
    image = models.ImageField(upload_to='review/')

    def __str__(self):
        return self.full_name


class SocialMedia(models.Model):
    icon = models.URLField()
    social_name = models.CharField(max_length=100)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.social_name
