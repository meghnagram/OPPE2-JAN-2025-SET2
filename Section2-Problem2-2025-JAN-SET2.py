# Write your code here

# Read the number of names
n = int(input())
names = []

# Process each name
for _ in range(n):
    name = input()
    parts = name.split()
    # Extract the last name
    last_name = parts[-1]
    # Extract the initials of the first and middle names
    initials = ".".join(part[0] for part in parts[:-1])
    # Format the name as "Last, F.M."
    formatted_name = f"{last_name}, {initials}."
    names.append(formatted_name)

# Sort and print the results
for name in sorted(names):
    print(name)

# #Another Method:

# # Write your code here

# x=int(input())
# l=[]
# s=[]
# temp=[]

# while(x!=0):
#     x -=1
#     s=input().split()
#     last=s.pop()
#     s.insert(0,last)
#     for i in range(1,len(s)):
#         s[i]=s[i][0]+'.'
#     a=''
#     for i in range(1,len(s)):
#         a=a+s[i]
#     temp.append(s[0])
#     temp.append(a)
#     l.append(temp)
#     temp=[]
    
# l.sort(key=lambda x:x[0]) 
# for i in l:
#     print (f"{i[0]}, {i[1]}")

# Abbreviate Initials And Sort
# Write a Python function that takes a list of full names, processes them to create abbreviated forms in the format "Last, F.M." (where F and M are the initials of the first and middle names), and returns the list sorted alphabetically.

# Assume that the names are given in the correct case.

# Hint: Use sorted function or list.sort to sort the list

# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input Format

# First line contains the number of names, n.
# Next n lines contain one full name per line.
# Output Format

# Output the processed names in sorted order, one per line.
# Example

# Input:

# 3
# John Doe
# Alice Johnson
# Bob Alan Rickman
# Output:

# Doe, J.
# Johnson, A.
# Rickman, B.A.
    
