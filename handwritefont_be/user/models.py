from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# def user_directory_path(instance, filename):
#     return 'profile/{0}/{1}'.format(instance.nickname, filename)

# Create your models here. 
class HWFUserManager(BaseUserManager):
    # def create_user(self, email,name,nickname,profile_image='',password=None):
    def create_user(self, email,name,nickname,password=None):
        if not email:
            raise ValueError('Must Have User Email')
        if not name:
            raise ValueError('Must Have User Name')
        if not nickname:
            raise ValueError('Must Have User Nickname')
        user = self.model(
            email = self.normalize_email(email),
            nickname= nickname,
            name = name,
            # profile_image = profile_image,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    # 관리자 user 생성
    def create_superuser(self, email, nickname,name, password=None):
    # def create_superuser(self, email, nickname,name,profile_image ='', password=None):
        user = self.create_user(
            email,
            password = password,
            nickname = nickname,
            name = name,
            # profile_image = profile_image,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class HWFUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(default ='', max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length = 30, default='Name')
    nickname = models.CharField(max_length=50, unique=True,default="NickName")
    # profile_image = models.ImageField(upload_to=user_directory_path,default='', null=True, blank=True)
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = HWFUserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'email'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['nickname', 'name']

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True