i = 1
while i < 25:
  print(i)
  if i == 23:
# break statement
    break
    print(i)
  i += 1
# continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# while else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
# List Iteration
l = ["i", "like", "to code"]
for i in l:
  print(i)
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("i", "like", "to code")
for i in t:
  print(i)
# Iterating over a String
print("\nString Iteration")
s = "abhi"
for i in s:
  print(i)
# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
  print("%s  %d" % (i, d[i]))
# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
  print(i),
# continue
for letter in 'abhirmn':
    if letter == 'h' or letter == 'm':
         continue
    print (letter)
# break loop
for letter in 'abhiram':
  if letter == 'b' or letter == 'r':
    break
print('Current Letter :', letter)
# An empty loop prints last item
for letter in 'abhiram':
   pass
print ('Last Letter :', letter)
ā