user = int(input("What's your age:"))
if user <= 18:
    print("You are a minor")
elif 18 <=  user <=65:
    print("You are an adult")
else:
    print("You are a senior citizen")