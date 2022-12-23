n = int(input("Enter the number: "))
count_p = 0
count_c = 0
for i in range(2,n+1):
  count=0
  for x in range(2, i):
    if i % x == 0:
      count += 1
  if count == 0:
    print(f"{i} is a prime number.")
    count_p += 1
  else:
    print(f"{i} is a composite number.")
    count_c += 1
print(f"There are {count_p} prime and {count_c} composite number in the range.")