from django.db import models


# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    pdf_file = models.FileField(upload_to="pdfs/", default="default_cv.pdf")
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About service")

    def __str__(self):
        return self.name


# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title


# Client model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name
    
# Modify your models.py to include project details
class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Project title")
    description = models.TextField(verbose_name="Project description")
    image = models.ImageField(upload_to="project_images/")
    # Add any additional fields you need, such as project URL, technologies used, etc.

    def __str__(self):
        return self.title

