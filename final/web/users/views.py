
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

@receiver(user_signed_up)
def set_gender(sender, **kwargs):
    user = kwargs.pop('user')
    extra_data = user.socialaccount_set.filter(provider='facebook')[0].extra_data
    gender = extra_data['gender']

    if gender == 'male': # because the default is female.
        user.gender = 'male'

    user.save()
