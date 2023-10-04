from django.contrib.auth.base_user import BaseUserManager
  
class UserManager(BaseUserManager):
    def create_user(self, user_ID, password=None, **extra_fields):
        if not user_ID:
            raise ValueError('The Email field must be set')
        user = self.model(user_ID=user_ID, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_ID, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(user_ID, password, **extra_fields)