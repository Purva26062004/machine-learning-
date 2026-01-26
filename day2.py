# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 21:11:10 2026

@author: Admin
"""
import re
a = "Hello123"
b = re.match(r"\d+",a)
c = re.match(r"\w+",a)
d = re.match(r"\^+",a)
print(b)
print(c)
print(d)

import re
a = "Hello World 123"
b = re.findall(r"\d+",a)
c = re.findall(r"\w+",a)
d = re.findall(r"\s+",a)
e = re.findall(r"\^",a)

import re
a = "hello world 12345"
b = re.search(r"\d+",a)
c = re.search(r"\w+",a)
d = re.search(r"\s+",a)
e = re.search(r"\^",a)

import re
text = "abc 123 AAB hello_world end start"
print(re.search(r"a.c","abc"))

print(re.search(r"\d+",text))
print(re.search(r"\w+","hello_123"))
print(re.search(r"\s","hello world"))
print(re.search(r"^abc","abc123"))
print(re.search(r"end$", "the end"))
print(re.search(r"[abc]", "dog"))
print(re.search(r"[abc]", "cat"))
print(re.search(r"[0-9]+", "room42"))
print(re.search(r"ab*", "a"))
print(re.search(r"ab*", "abbb"))   
print(re.search(r"ab+", "abbb")) 
print(re.search(r"ab?", "a"))   
print(re.search(r"\d{2,4}", "Year 2024")) 
print(re.search(r"(ab)+", "ababab"))  
print(re.search(r"cat|dog", "I have a dog"))

import numpy as np
arr = np.array([10,20,30,40,50])
print(arr)
print([0])
print(arr[1:])
print(arr[:])
print(arr[:3])
print(arr[[0, 4, 2]])#fancy index

s = "Python"

print(s[0:4])    # Characters from index 0 to 3
print(s[1:5])    # Characters from index 1 to 4
print(s[:3])     # From start to index 2
print(s[2:])     # From index 2 to end
print(s[-4:-1])  # Using negative indexing
print(s[::-1])   # Reverse the string

c = np.arange(1, 5, 2)
print(c)

b = np.array([2, 4, 6, 8, 10])
print(b)

d = np.linspace(0, 100, 10)
print(d)

e = np.full((3, 3), 8)
print(e)

f = np.zeros((4, 5))
print(f)

g = np.ones((4, 3))
print(g)

h = np.array([10, 20, 20, 20, 40, 40, 50, 50])
print(h)

mean_a= np.mean(h)
print("Mean:", mean_a)

median_a= np.median(h)
print("Median:", median_a)
