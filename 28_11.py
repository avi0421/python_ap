'''
sports1 = {"Sanoj", "Neha", "Dev", "Raj", "Shweta", "Hiral"}
sports2 = {"Neha", "Shweta", "Hiral", "Arjun", "Ram", "Sahyog"}

# Find the total participants by combining both sets
total_Ath = (sports1 | sports2)

print("Total participants:", total_Ath)

for s in total_Ath: 
    print(s)

# set difference 
New_sports1 = (sports1 - sports2)
print("The new sports1 list is :", New_sports1)
'''
email_data = ["user1@yahoo.com", "sang@gmail.com", "Rax1@gmail.com", "user1@yahoo.com", "sar@gmail.com"]
print("The data of email as below: ")
print(email_data)

unique_emails = set(email_data)
print("The unique data is:", unique_emails)

new_emails = {"raj@gmail.com", "Harsh@gmail.com", "sang@gmail.com", "Rax1@gmail.com"}
updata = new_emails - unique_emails
print("New customers are:", updata)

