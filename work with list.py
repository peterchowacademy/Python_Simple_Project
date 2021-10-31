# ##basic of the list
# friends = ["kevin", "karen", "jim", "oscar"]
#
# print(friends)
# print(friends[0])
# print(friends[2])
# print(friends[-1])  #from the back order the first one is -1
# print(friends[1:]) #grab everything from index 1 to the rest
# print(friends[0:2]) #grab everything from index 0 to index 2 but not include index2
##can modify the list
# friends[1] = "Mike"
# print(friends[1])
# print(friends[0:2])

##list functions

lucky_numbers = [4,8,15,16,23,245]
friends = ["kevin", "karen", "Jim", "oscar", "oscar"]
print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1,"Kelly")
print(friends)
friends.remove("Jim")
print(friends)
# friends.clear()
# print(friends)
friends.pop()
print(friends)
print(friends.index("kevin"))
print(friends.count("oscar"))
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)