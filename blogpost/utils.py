import datetime
from django.utils import timezone

from blogpost.models import Action


def create_or_delete_action(user, verb, post, create=True):
    actions = Action.objects.filter(user=user, verb=verb, post=post)
    # delete same actions
    for action in actions:
        action.delete()

    if create:
        action = Action.objects.create(user=user, verb=verb, post=post)
        action.save()
    return True
