thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
print(thisdict)
thisdict["apple"] = "red"
print(thisdict)
thisdict =	dict(apple="green", banana="yellow", cherry="red")
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
thisdict["damson"] = "purple"
print(thisdict)
del(thisdict["banana"])
print(thisdict)
print(len(thisdict))
