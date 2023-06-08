

from django.forms import ModelForm

from lm_users.models import Profile, Skill


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username',
                  'location', 'bio', 'short_intro', 'profile_image',
                  'social_github', 'social_vk', 'social_twitter',
                  'social_youtube', 'social_website']
