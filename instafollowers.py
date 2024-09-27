from instaloader import Instaloader

L = Instaloader()
L.login("username", "password")  # Replace with your credentials

profile = instaloader.Profile.from_username(L.context, "username to load")

followers = [user.username for user in profile.get_followers()]
following = [user.username for user in profile.get_followees()]

print("Followers:", followers)
print("Following:", following)
