import collections;
testCases = int(input()) # number of test cases
while testCases: # iterate over the number of test cases
testCases -= 1
string = input() # get the string
halve = len(string) // 2 # get the half length of the string
if len(string) % 2 == 0: # if the length of the string is even
if sorted(string[:halve]) == sorted(string[halve:]): # if the first 
half is equal to the second half
print('YES')
else: # if the first half is not equal 
to the second half
print('NO')
else: # if the length of the string is odd
if sorted(string[:halve]) == sorted(string[halve + 1:]): # if the 
first half is equal to the second half
print('YES')
else:
print('NO'