thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist[1] = "blackcurrant"
print(thislist)


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist.append("damson")
print(thislist)

thislist.remove("banana")
print(thislist)

print(len(thislist))
