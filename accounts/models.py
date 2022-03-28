from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = None
    last_name = None
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False,blank = True,null=True)
    username = models.CharField(max_length=30, unique=True,blank = True,null=True,
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                ('Enter a valid username. This value may contain only '
                 'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': ("A user with this username already exists."),
        },
    )
    email = models.EmailField(unique=True,error_messages={
            'unique': ("A user with this Email already exists."),
        },)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    