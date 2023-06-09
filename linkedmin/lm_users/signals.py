from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

from django.core.mail import send_mail
from django.conf import settings


# create user profile automatically when user is created
# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            owner=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        print('profile created')

        subject = 'Welcome to LinkedMin'
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.owner

    if created == False:
        user.first_name = profile.name
        user.email = profile.email
        user.save()


# delete user when profile is deleted
def delete_user(sender, instance, **kwargs):
    try:
        print("Deleting user...")
        owner = instance.owner
        owner.delete()
    except User.DoesNotExist:
        print("User does not exist. This has to do with the relationship between User and Profile.")


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(delete_user, sender=Profile)
