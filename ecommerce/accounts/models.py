from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager
	)
class UserManager(BaseUserManager):
	def create_user(self,email,full_name=None,password=None,is_staff=False,is_admin=False,is_merchant=False,is_active=False):
		if not email:  
			raise ValueError("User must have an email address")
		if not password:  
			raise ValueError("User must have a password")
# 		if not full_name:  
# 			raise ValueError("User must provide a full name")
# 		
		user_obj = self.model(
			email = self.normalize_email(email),
			full_name = full_name
			)
		user_obj.set_password(password)
		
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.merchant = is_merchant
		user_obj.active = is_active
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self,email,full_name=None,password=None):
		user = self.create_user(email,full_name=full_name,password=password,is_staff=True,is_active=True)
		return user

	def create_merchant(self,email,full_name=None,password=None):
		user = self.create_user(email,full_name=full_name,password=password,is_merchant=True,is_active=True)
		return user

	
	def create_superuser(self,email,full_name=None,password=None):
		user = self.create_user(email,full_name=full_name,password=password,is_staff=True,is_admin=True,is_active=True)
		return user

class User(AbstractBaseUser):
	email 		=	models.EmailField(max_length=255,unique=True)
	full_name	=	models.CharField(max_length=255,blank=True,null=True)
	active		=	models.BooleanField(default=False)
	staff		=	models.BooleanField(default=False)
	admin		=	models.BooleanField(default=False)
	merchant	=	models.BooleanField(default=False)  # New merchant field
	timestamp	=	models.DateTimeField(auto_now_add=True)
	
	objects = UserManager()
	
	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = [] #python manage.py createsuperuser
	
	def __str__(self):
		return self.email

	def get_full_name(self):
		if self.full_name:
			return self.full_name
		return self.email

	def get_short_name(self):
		return self.email
	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_merchant(self):
		return self.merchant

	@property
	def is_active(self):
		return self.active
	
	def has_perm(self,perm,obj=None):
		return True
	
	def has_module_perms(self,app_label):
		return True

# Create your models here.
class GuestEmail(models.Model):
	email 		=	models.EmailField()
	active 		=	models.BooleanField(default=True)
	update		=	models.DateTimeField(auto_now=True)
	timestamp	=	models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email