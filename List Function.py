lucky_numbers = [455,8,15,16,23,42]
friends = ["kevin", "jim", "karen", "jim","jim", "oscar", "toby"]
print(sum(lucky_numbers))
print(friends)
friends.insert(1, "kelly")
print(friends)
print(friends.index("jim"))
print(friends.count("jim"))
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends2=friends.copy()
friends2.extend(lucky_numbers)
print(friends2)
lucky_numbers.reverse()
print(lucky_numbers)
lucky_numbers[2] = 555555
print(lucky_numbers)