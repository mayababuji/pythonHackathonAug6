#1. How do you access the first and last elements of a list?  numbers = [10, 20, 30, 40, 50]
numbers = [10, 20, 30, 40, 50]
print(f"the first element is {numbers[0]} and the last element of the list is {numbers[-1]}")
#2.How can you add and remove elements from a list?  fruits = ['apple', 'banana']
fruits = ['apple', 'banana']
fruits.append('orange')
fruits.remove('apple')
print(fruits)
#3.  Write a program to find the sum of all elements in a list. numbers = [1, 2, 3, 4]
numbers = [1, 2, 3, 4]
print(sum(numbers))
#4.How do you check if an element exists in a list? colors = ['red', 'green', 'blue'] check if green is in colors
colors = ['red', 'green', 'blue']
if 'green' in colors:
    print("yes")
else:
    print("no")

#5. Write a function that takes a list and returns a new list with only the even.
def even(mixed_list):
    even_list = []
    for i in mixed_list:
        if i%2==0:
            even_list.append(i)
    return even_list
user_input = input("enter the numbers space seperatted: ")
mixed_list = list(map(int,user_input.split()))
print(mixed_list)
print(even(mixed_list))
#6 find the output
x = "5"
y = 3
print(x * y)
#7. a = [1, 2]  b = [1, 2] what will be a ==b and a is b output?
a = [1, 2]
b = [1, 2]
print(a==b)
print(a is b)
#8. Write a function that takes a string and returns a dictionary with each character as a key and its frequency as the value.

def count_characters(word):
    word_count = {}
    for i in word:
        if i in word_count:
            word_count[i] +=1
        else:
            word_count[i] = 1
    return word_count
word = 'banana'
print(count_characters(word))
#9.Given a list of words, return a dictionary where the key is the word length, and the value is a list of words of that length
# example
# Input: ["hi", "hello", "hat", "at"]
# Output: {2: ["hi", "at"], 5: ["hello"], 3: ["hat"]}

Input= ["hi", "hello", "hat", "at"]
Output={}
for i in Input:

    #print(len(i))
    if len(i) in Output:

        Output[len(i)].append(i)
    else:
        Output[len(i)]=[i]
print(Output)
# 10. Write a function that counts how many times each word appears in a sentence (ignore punctuation and case).
#    example
#       Input: "The cat and the hat."
#       Output: {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}

Input="The cat and the hat."
Output={}
for i in Input.split():
    print(i.lower())
    if i.lower() in Output:
        Output[i.lower()] +=1
    else:
        Output[i.lower()] =1
print(Output)





