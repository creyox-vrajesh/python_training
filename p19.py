# Write a Python program that accepts the names and birthdates (YYYY-MM-DD) of 3 people, then identifies and prints the oldest and the youngest person among them.

# p1 = input("enter birthdate for person 1 in YYYY-MM-DD format : ").split('-')
# p2 = input("enter birthdate for person 2 in YYYY-MM-DD format : ").split('-')
# p3 = input("enter birthdate for person 3 in YYYY-MM-DD format : ").split('-')

p1 = "2025-11-05".split('-')
p2 = "2025-11-03".split('-')
p3 = "2025-11-04".split('-')

p1 = [int(x) for x in p1]
p2 = [int(x) for x in p2]
p3 = [int(x) for x in p3]

youngest = min(p1,p2,p3)
oldest = max(p1,p2,p3)

print(f"youngest is {youngest}, oldest is {oldest}")
