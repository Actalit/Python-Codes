friends = {}
n = int(input("Enter the number of friends: "))
for i in range(n):
    name = input(f"Enter the name of friend {i + 1}: ")
    phone = input(f"Enter the phone number of {name}: ")
    friends[name] = phone
print("\n--- Friend List ---")
for name, phone in friends.items():
    print(f"Name: {name}, Phone: {phone}")
new_name = input("\nEnter the name of a new friend to add: ")
new_phone = input(f"Enter the phone number of {new_name}: ")
friends[new_name] = new_phone
print("\nModified dictionary after adding a new friend:")
print(friends)
delete_name = input("\nEnter the name of the friend to delete: ")
if delete_name in friends:
    del friends[delete_name]
    print(f"\nFriend '{delete_name}' deleted successfully.")
else:
    print(f"\nFriend '{delete_name}' not found.")
print("Updated dictionary:")
print(friends)
modify_name = input("\nEnter the name of the friend whose number you want to modify: ")
if modify_name in friends:
    new_number = input(f"Enter the new phone number for {modify_name}: ")
    friends[modify_name] = new_number
    print(f"\nPhone number of '{modify_name}' updated successfully.")
else:
    print(f"\nFriend '{modify_name}' not found.")
print("Updated dictionary:")
print(friends)
check_name = input("\nEnter the name of the friend to check: ")
if check_name in friends:
    print(f"\n'{check_name}' is present in the dictionary with phone number {friends[check_name]}.")
else:
    print(f"\n'{check_name}' is not present in the dictionary.")
sorted_friends = dict(sorted(friends.items()))
print("\nDictionary sorted by names:")
for name, phone in sorted_friends.items():
    print(f"Name: {name}, Phone: {phone}")
