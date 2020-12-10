from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=50, null=True)
    to = models.CharField(max_length=50, null=True)
    order = models.IntegerField(null=True)
    logo = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu_Item"
        verbose_name_plural = "Menu_Items"


class Footer(models.Model):
    sm_ins = models.CharField(max_length=256, null=True)
    sm_ins_icon = models.FileField(null=True, blank=True)
    sm_mail = models.CharField(max_length=256, null=True)
    sm_mail_icon = models.FileField(null=True, blank=True)
    footer_info = models.CharField(max_length=256, null=True)
    footer_year = models.CharField(max_length=256, null=True)
    footer_except = models.FileField(null=True, blank=True)
    footer_about_info = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.sm_ins

    class Meta:
        verbose_name = "Footer_Item"
        verbose_name_plural = "Footer_Items"


class Home(models.Model):
    home_title = models.CharField(max_length=256, null=True)
    home_image = models.ImageField(null=True, blank=True)
    home_info = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.home_title

    class Meta:
        verbose_name = "Home_Item"
        verbose_name_plural = "Home_Items"


class Work(models.Model):
    work_title = models.CharField(max_length=256, null=True, blank=True)
    work_image = models.ImageField(null=True, blank=True)
    work_image_line2 = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Work_Item"
        verbose_name_plural = "Work_Items"


class About(models.Model):
    about_title = models.CharField(max_length=256, null=True)
    about_image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.about_title

    class Meta:
        verbose_name = "About_Item"
        verbose_name_plural = "About_Items"


