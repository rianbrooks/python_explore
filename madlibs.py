## Learning to concatinate strings
# you want to print out "subscribe to _____"
# youtuber = "Rian Brooks"

# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))

# # f-string provides a way to embed expressions inside string literals with minimal syntax
# print(f"Subscribe to {youtuber}")

#Assigning variables to populate madlib 

adj = input("Adjective: ")
verb = input("Verb: ")
famous_person = input("Famous person: ")
adj2 = input("Adjective: ") 
adj3 = input("Adjective: ") 

# Creating madlib to fill in
madlib = f"Going to yoga is so {adj}. The first thing I do when I walk into the classroom \
is {verb} because I am so {adj2} to be there. {famous_person} is my yoga instructor and boy \
are they {adj3}!"

print(madlib)


