from django.db import models


class Project(models.Model):
    # A Project is some software development project (e.g., 
    # Currency Calculator). It has various Needs
    pass


class Application(models.Model):
    # An Application is a request by a User to fill a Need
    pass


class Need(models.Model):
    # A Need is a particular development requirement (e.g., 
    # Python Developer). It is filled by accepting an Application
    # submitted by a User.
    pass