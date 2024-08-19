from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
# Create your models here.


class StudentManager(BaseUserManager):
    def _create_user(self, email, firstname, middlename, lastname, gender, phonenumber, state_of_origin, religion, password, **extra_fields):
        if not email:
            raise ValueError('Email is not provided')
        if not password:
            raise ValueError('Password is not provided')
        
        student = self.model(
            email = self.normalize_email(email),
            firstname = firstname,
            middlename = middlename,
            lastname = lastname,
            gender = gender,
            phonenumber = phonenumber,
            state_of_origin = state_of_origin,
            religion = religion,
            **extra_fields
        )

        student.set_password(password)
        student.save(using=self.db)
        return student
    
    def create_user(self, email, firstname, middlename, lastname, gender, phonenumber, state_of_origin, religion, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, firstname, middlename, lastname, gender, phonenumber, state_of_origin, religion, password, **extra_fields)
    
    def create_superuser(self, email, firstname, middlename, lastname, gender, phonenumber, state_of_origin, religion, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, firstname, middlename, lastname, gender, phonenumber, state_of_origin, religion, password, **extra_fields)
    

class Student(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=200)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    phonenumber = models.CharField(unique=True, max_length=100)
    state_of_origin = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(default='127.0.0.1')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = StudentManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'middlename', 'lastname', 'gender', 'phonenumber', 'state_of_origin', 'religion']

    

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'