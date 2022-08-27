#while
#
i = 1
while i < 6:
  print(i)
  i += 1

#break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break #break statement we can stop the loop even if the while condition is true
  i += 1

#continue
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #continue statement we can stop the current iteration, and continue with the next
  print(i)
#Note that number 3 is missing in the result