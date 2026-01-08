suffixes = [
    'wards', 'ations', 'ation', 'tions', 'tion', 'asions', 
    'asion', 'sions', 'sion', 'ment', 'ness', 'ship', 
    'hood', 'able', 'ible', 'less', 'ward', 'wise', 'ion', 'ity', 'age',
    'ize', 'ise', 'ify', 'ate', 'ful', 'ous', 'ish', 'ive', 'ing', 'ers', 'er',
    'or', 'ty', 'en', 'ic', 'al', 'ly'
]


def stem(word: str) -> str:
    """Helper function to stem a word by removing suffixes."""
    for suffix in suffixes:
        n = len(suffix)
        if word.endswith(suffix):
            return word[:-n]
    return word
    
with open(filename) as f:
    for line in f:
        words = line.split()
        print(" ".join(stem(word) for word in words))

# #Another Method:

# suffixes = [
#     'wards', 'ations', 'ation', 'tions', 'tion', 'asions', 
#     'asion', 'sions', 'sion', 'ment', 'ness', 'ship', 
#     'hood', 'able', 'ible', 'less', 'ward', 'wise', 'ion', 'ity', 'age',
#     'ize', 'ise', 'ify', 'ate', 'ful', 'ous', 'ish', 'ive', 'ing', 'ers', 'er',
#     'or', 'ty', 'en', 'ic', 'al', 'ly'
# ]

# # Write your code to read the file, process it, and print the result.
# # Use the variable filename for the name of the file.
# with open(filename,'r') as file:
#     l=[]
#     s=[]
#     line=file.readline()
#     while(line):
#         l=line.rstrip().split(' ')
#         # print (l)
#         for i in l:
#             c=0
#             for j in suffixes:
#                 if i.endswith(j):
#                     c=1
#                     new=i.replace(j,'')
#                     s.append(new)
#                     break
#             if c==0:
#                 s.append(i)
            
#         print(' '.join(s))
#         s=[]
#         line=file.readline()

# Simple Stemmer
# Given a multiline text file containing lowercase words separated by spaces or newlines, stem each word (remove certain suffixes) according to the list of suffixes given in the suffixes list and print the contents in the same format.

# Do not change the line or order of the words.

# suffixes = [
#     'wards', 'ations', 'ation', 'tions', 'tion', 'asions', 
#     'asion', 'sions', 'sion', 'ment', 'ness', 'ship', 
#     'hood', 'able', 'ible', 'less', 'ward', 'wise', 'ion', 'ity', 'age',
#     'ize', 'ise', 'ify', 'ate', 'ful', 'ous', 'ish', 'ive', 'ing', 'ers', 'er',
#     'or', 'ty', 'en', 'ic', 'al', 'ly'
# ]
# Remove the first suffix from the list of suffixes that matches a given word. For example for the word "education" the suffix "ation" and "tion" matches but "ation" is present first in the suffixes list thus the word is stemmed as "educ".

# NOTE: This is a file-in-stdout type question where the input is read from the file and the output is printed in the standard output.
                
