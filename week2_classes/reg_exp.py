# search method
# find all
# finditer

import re

text="I have 31 students and 2 TM's"

# Finds the first digit
match=re.search(r"\d+", text)
# print(match.group())
# print(match.start())
# print(match.end())

# Returns all but can't tell which is the first or last
match=re.findall(r"\d+", text)
# print(match)

match=re.finditer(r"\d+", text)
# print(match)
# for x in match:
#     print(x.group(), x.start(), x.end())



# Meta Characters
# a dot(.)-- Takes the place of any character
text="acb accbb ab"
pattern="a.b"
matches=re.findall(pattern, text)
# print(matches)


# Caret (^)-- Matches the start of a string
pattern="^bcb"
matches=re.findall(pattern, text)
# print(matches)

# Dollar sign($)-- Matches the end of a string
pattern="b$"
matches=re.findall(pattern, text)
# print(matches)


# An Asterisk(*)-- Returns only what you want and where they are 
pattern="b*"
matches=re.findall(pattern, text)
# print(matches)


# Character Classes
# [abc]
text="apple banana cat dog"
pattern=r"[cat]"
matches=re.findall(pattern, text)
# print(matches)



# d -- Used to locate digits   Also 0-9
text="I have 31 students and 3 TM's"
# pattern=r"\d+"
# match=re.findall(pattern, text)
# print(match)


pattern=r"[0-9]"
match=re.findall(pattern, text)
# print(match)
# Case
# lower -- [a-z]
text="Are we early"
pattern=r"[a-z]"
matches=re.findall(pattern, text)
# print(matches)



# UPPPER -- [A-Z]
text="Are we early"
pattern=r"[A-Z]"
matches=re.findall(pattern, text)
# print(matches)


# Any Whitespace-- spaces, tabs, newlines Use a \s
# text="We are in class.\n\tAre you there?"
# print(text)
# pattern=r"\s"
# matches=re.findall(pattern, text)
# print(matches)


# ?-- Checks wether what we are r searching for is there
text="I have 31 students and 3 TM's"
pattern=r"\d?"
matches=re.findall(pattern, text)
# print(matches)


# Exact Scenarios
# Use {n}
text= "aa ba bac dca"
# pattern=r"a{2}"
# matches=re.findall(pattern, text)
# # print(matches)


# {n,m}
text="aa ba bac dca"
pattern=r"a{1,2}"
matches=re.findall(pattern, text)
# print(matches)


# Extract Phone numbers
# text="Contact us at 123-456-3210"
# pattern=r"\d{3}-\d{3}-\d{4}"
# matches=re.findall(pattern, text)
# print(matches)


# QUESTIONS
# Scenario: You want to collect all email addresses from a document.
# text = "Send an email to support@example.com or sales@company.net for inquiries."
# pattern=r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{3}"
# matches=re.findall(pattern, text)
# print(matches)



# Scenario: You need to extract dates from a document (formats: DD/MM/YYYY, MM-DD-YYYY).
# text = "The event is on 12/08/2023 and another one on 07-15-2024."
# pattern=r"\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}"
# matches=re.findall(pattern, text)
# print(matches)



# Scenario: You need to check if a password meets security requirements:
# At least 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one number
# At least *one special character (@, $, !, %, , ?, &)
password=input("Enter your password:")
pattern=r"\d?[a-z]?[A-Z]?[0-9]?[@&!$%]?[a-zA-Z0-9@&!$%]{8,}"
match=re.findall(pattern, password)
print(match)
