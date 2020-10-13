from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
class Account_manager(BaseUserManager):
    def create_user(self,email,contact_no,profile_image=None,password=None):
        if not email:
            raise ValueError("user must have email address")
        user=self.model(
            email=self.normalize_email(email),
            contact_no=contact_no,
            profile_image=profile_image,
        )
        user.set_password(password)
        user.is_admin=False
        user.save(using=self._db)
        return user

    def create_superuser(self,email,contact_no,profile_image=None,password=None):
        if not email:
            raise ValueError("user must have email address")
        user=self.model(
            email=self.normalize_email(email),
            contact_no=contact_no,
            profile_image=profile_image,
            
        )
        user.is_admin=True
        user.set_password(password)
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email=models.EmailField(unique=True)
    profile_image=models.ImageField(upload_to='profile/',null=True,blank=True)
    contact_no=models.CharField(max_length=15)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    full_name=models.CharField(max_length=200,blank=True,null=True)

    objects=Account_manager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['contact_no']

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin