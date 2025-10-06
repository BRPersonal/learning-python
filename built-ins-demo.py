
import io

#divmod
total_seconds = 7132
minutes, seconds = divmod(total_seconds, 60) #quotient is minutes, remainder is seconds
hours, minutes = divmod(minutes, 60)  #quotient is hours, remainder is minutes
print(f"Time Elapsed: {hours:02d} hours {minutes:02d} minutes {seconds:02d} seconds")

#slice - reusable
evens = slice(0, None, 2) #start,stop,step ; zero-based index
text = "abcdefghij"
print(text[evens])
fruits = ["apple", "orange","banana","grapes","guava"]
print(fruits[evens])

#iter
"""
prefixing b in a string denotes binary string
lambda that we see here is parameterless lambda
which turns a statement into callable. 
usually we see lambda like lambda x:x[1] . This is different
iter takes a callable and sentinel that signals end of iteration

"""
f = io.BytesIO(b"abcdefgh")
for chunk in iter(lambda:f.read(3),b""):
    print(chunk)
