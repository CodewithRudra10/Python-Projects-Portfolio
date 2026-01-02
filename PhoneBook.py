
phonebook={
"rudra":"122-455-788",
"mom":"356-4478-3647",
"bob":"2747-3675-89",

}
phonebook["dad"]="1164-378"
print(phonebook["rudra"])
phonebook.update({"bob":"1298-5474-37"})
del phonebook["mom"]
print(phonebook)
name=input("enter the name:").lower()
if name in phonebook:
    print(f"{name.capitalize()}'s number : {phonebook[name]} ")
else:
    print("Sorry! name not found")
for name, numbers in phonebook.items():
    print(f"Name: {name.capitalize()} Phone:{numbers}")

