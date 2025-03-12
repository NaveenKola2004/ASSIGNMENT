#1. Who Has More Followers?

alice_followers=5000
bob_followeres=7000

result=(
    alice_followers > bob_followeres,
    alice_followers < bob_followeres,
    alice_followers == bob_followeres
)

print(result)

#2. VIP Club Membership Check

vip_list=["Elon", "Bill", "Steve", "Sundar"]
person="Sundar"

result=(
    person in vip_list
)
print(result)

#3. Battery Sufficient for a Trip?

battery_percentage=75
battery_percentage_check=battery_percentage>=60
print(battery_percentage_check)

#4. Streaming Plan Upgrade Check

current_usage = 250
limit_usage=200
check=current_usage>limit_usage
print(check)

#5. Social Media Friend Suggestion

mutal_friends=["John", "Emma", "Sophia"]
person="Emma"

mutal_friends_check=person in mutal_friends
print(mutal_friends_check)

#6. Logical AND: Are Both Apps Installed?

installed_apps=["whatsapp","facebook","instagram"]
required_app1="whatsapp"
required_app2="instagram"

checking=required_app1 in installed_apps or required_app2 in installed_apps
 
print(checking)

#7. Logical OR: Can Access Premium Content?

subscription ="Free"
reward_points=6000

check_Subscription=reward_points > 5000
print(check_Subscription)

#8. Logical NOT: Is the Device Not in the Blacklist?

blacklisted_devices = ["iPhone 6", "Samsung J7", "Nokia 3310"]  
device = "iPhone 12"  

check_device=device not in blacklisted_devices
print(check_device)

#.9 Who Has the Newer Phone?

user_a_phone = ("iPhone 12", 2020)  
user_b_phone = ("iPhone 14", 2022)  

result=(
    2022<2020,
    2022>2020,
    user_a_phone==user_b_phone
)
print(result)

#10. Does the Password Contain Special Characters?

password = "Pass@word123"  
character="@"
check=character in password
print(check)
