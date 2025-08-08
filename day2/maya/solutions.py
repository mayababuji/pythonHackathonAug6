# 1. Frequency Counter
# Problem:
# Write a function to count the frequency of each element in a list using a dictionary.
#
# Input: [2, 3, 2, 5, 3, 2]
# Output: {2: 3, 3: 2, 5: 1}

Input= [2, 3, 2, 5, 3, 2]
Output={}
for i in Input:
    if i in Output.keys():
        Output[i] +=1
    else:
        Output[i] =1
print(Output)

# 2. Merge Two Dictionaries with Sum
# Problem:
# Merge two dictionaries. If a key exists in both, sum their values.
#
# Input:
# {"a": 5, "b": 10}
# {"a": 3, "c": 8}
# Output: {"a": 8, "b": 10, "c": 8}

Input_a =  {"a": 5, "b": 10}
Input_b = {"a": 3, "c": 8}
Output ={}
for k,v in Input_a.items():
    if k in Input_b:
        print(k)
        print(Input_b[k] + Input_a[k])
        Output[k] = Input_b[k] + Input_a[k]
    else:
        Output[k] = Input_a[k]
for k1,v1 in Input_b.items():
    if k1 not in Input_a:
        Output[k1] = Input_b[k1]
print(Output)
# 3. Invert a Dictionary
# Problem:
# Swap keys and values in a dictionary. If values are not unique, store keys in a list.
#
# Input: {"a": 1, "b": 2, "c": 1}
# Output: {1: ["a", "c"], 2: ["b"]}

Input= {"a": 1, "b": 2, "c": 1}
Output ={}
for k,v in Input.items():
    if v in Output:
      Output[v].append(k)
    else:
        Output[v] = list(k)

print(Output)

# 4. Find Top Scorer
# Problem:
# Given a dictionary of student scores, return the name(s) of the highest scorer(s).
#
# Input: {"Alice": 88, "Bob": 91, "Charlie": 91}
# Output: ["Bob", "Charlie"]



def max_dict(input):
    values_list = []
    students_list = []

    for student,score in input.items():
        values_list.append(score)
    print(max(values_list))
    for k,v in input.items():
        if v == max(values_list):
            students_list.append(k)

    return students_list

Input = {"Alice": 88, "Bob": 91, "Charlie": 91}
print(f"The top scorers are {(max_dict(Input))}")



# 6. Word Frequency in Sentence
# Problem:
# Count word frequency from a given sentence (ignore punctuation and case).
#
# Input: "Hello hello world!"
# Output: {"hello": 2, "world": 1}

Input=  "Hello hello world!"
list_word = []
list_dict = {}

for i in Input.split():
    list_word.append(i.lower())
print(list_word)
for i in list_word:
    if i in list_dict:
        list_dict[i] +=1
    else:
        list_dict[i] = 1

print(list_dict)


# 7. Create a Dictionary from Two Lists
# Problem:
# Create a dictionary where one list contains keys and the other contains values.
#
# Input:
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "Toronto"]
# Output: {"name": "Alice", "age": 25, "city": "Toronto"}

keys = ["name", "age", "city"]
values = ["Alice", 25, "Toronto"]
new_dict = {}
for i in keys:
    for j in values:
        new_dict[i] = j
print(new_dict)

# 9. Most Common Value
# Problem:
# Given a dictionary, find the most frequent value.
#
# Input: {"a": 1, "b": 2, "c": 1, "d": 3}
# Output: 1
Input= {"a": 1, "b": 2, "c": 1, "d": 3}
print(Input.values())
list_val = []
for i in Input.values():
    list_val.append(i)
for value in list_val:
    if (list_val.count(value)) >1:
        print(value)
# 10. Nested Dictionary – Student Grades
# Problem:
# You are given a dictionary of students and their list of grades. Calculate and return a dictionary with their average scores.
#
#
# Input:
#
# {
#     "Alice": [80, 90, 85],
#     "Bob": [70, 60, 75]
# }
#Output:  {"Alice": 85.0, "Bob": 68.33}

Input =  {
    "Alice": [80, 90, 85],
    "Bob": [70, 60, 75]
}
Output = {}
for student,scores in Input.items():

    Output[student] = sum(scores)/len(scores)

print(Output)

# 11.You are given a dictionary representing a shopping cart. Each key is the item name, and its value is another dictionary with the price and quantity of that item.
#
# Write a Python function to calculate and return the total cost of all items in the cart.
#
# Input
# cart = {
#     "apple": {"price": 2.5, "quantity": 4},
#     "banana": {"price": 1.2, "quantity": 6},
#     "milk": {"price": 3.0, "quantity": 2}
# }
# Output
# Total cost: 23.2

def caluclate_cost(Input_cart):
    total_price = []
    for item, price in Input_cart.items():
        total_price.append(price["price"] * price["quantity"])
    return(sum(total_price))


Input_cart = {
    "apple": {"price": 2.5, "quantity": 4},
    "banana": {"price": 1.2, "quantity": 6},
    "milk": {"price": 3.0, "quantity": 2}
}

print((caluclate_cost(Input_cart)))
# 5. Anagram Groups
# Problem:
# Group words that are anagrams using dictionaries.
#
# Input: ["bat", "tab", "tap", "pat", "cat"]
# Output: { 'abt': ['bat', 'tab'], 'apt': ['tap', 'pat'], 'act': ['cat'] }

def anagram_groups(words):
    ana_dict = {}
    for word in words:
        key = ''.join(sorted(word))
        if key in ana_dict:
            ana_dict[key].append(word)
        else:
            ana_dict[key] = [word]
    return ana_dict

Input= ["bat", "tab", "tap", "pat", "cat"]
print(anagram_groups(Input))
