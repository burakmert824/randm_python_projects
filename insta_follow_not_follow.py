import instaloader

# Get instance
bot = instaloader.Instaloader()

# Open the file in read mode
with open('userpasstxt', 'r') as file:
    # Read the first line and assign it to a variable
    username = file.readline().strip()
    # Read the second line and assign it to another variable
    password = file.readline().strip()
print("Login yapiliyor...")
bot.login(user=username,passwd=password)

profile = instaloader.Profile.from_username(bot.context,'sudealaann')

print("Followingler cekiliyor...")
followings = [followee.username for followee in profile.get_followees()]
print(f"--- Followings[{len(followings)}] ---")
for p in followings[0:3]:
    print(p)
print("--- ---------- ---")

print("Followerlar cekiliyor... ")
followers = [follower.username for follower in profile.get_followers()]
print(f"--- Followers[{len(followers)}]---")
for p in followings[0:3]:
    print(p)
print("--- ---------- ---")

ll = []
for i in followings:
    if(i not in followers):
       ll.append(i)
print(f"---Following but not followers[{len(ll)}]---")
for i in ll:
    print(i)
print("--- ---------- ---")
