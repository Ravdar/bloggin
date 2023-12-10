from django.contrib.auth.models import User
from users.models import Profile

def make_existing_users_profiles():

    existing_users = User.objects.all()


    for user in existing_users:

        if not Profile.objects.filter(user=user).exists():
            Profile.objects.create(user=user)

# if __name__ == "__main__":
#     make_existing_users_profiles()