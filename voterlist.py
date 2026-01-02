raw_voters=["Amit","Rahul","Krish","Rudra","Harshit","Atharv","Adarsh","Rishabh","Priyansu"]
unique_voters= set(raw_voters)
registered_voters= set(raw_voters)

print("Total Unique Voters:", len(unique_voters))
print("Registered Voters:", unique_voters)
print()

voted_names=["Amit","Rahul","Rudra","Harshit","Atharv","Adarsh","Rishabh","Priyansu","Sachin"]
voted_names=set(voted_names)
print()

print("The people who voted",len(raw_voters))
print("Registered Voters",len(registered_voters))
print("people who voted",voted_names)






# Your data
raw_voters = ["Amit","Rahul","Krish","Rudra","Harshit","Atharv","Adarsh","Rishabh","Priyansu"]
registered_voters = set(raw_voters)  # Unique registered voters

voted_names = ["Amit","Rahul","Rudra","Harshit","Atharv","Adarsh","rishabh","Priyansu","Sachin"]
voted = set(voted_names)  # Convert to set (note: "rishabh" has lowercase 'r')

print("Polling Booth: ABC")
print("="*50)
print()

# Basic info
print(f"Total Registered Voters: {len(registered_voters)}")
print(f"Registered Voters: {registered_voters}")
print()
