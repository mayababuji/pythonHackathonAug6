#fun1: #Write a function to count the frequency of each element in a list using a dictionary.
#fun2: Merge Two Dictionaries using inbuilt function '|'
#fun3: Merge Two Dictionaries with Sum 
#fun4: invert dicitionary noraml and to maintain duplicate key
#fun5: find top scorer
#fun6: Anagram Groups
#fun7: Anagram Groups using defaultdict from collection module
#fun8:Word Frequency in Sentence using Counter class from colecctions
#fun9: Create a Dictionary from Two Lists
#fun10
#fun11
#fun12: Calculate and return a dictionary with their average scores. nested dictionary

#Write a function to count the frequency of each element in a list using a dictionary.
#Notes: 
    #The comprehension is typically used to build that dictionary in a compact way.
def fun1():
    input= [2, 3, 2, 5, 3, 2]
    print(input)
    countDict={}
    for i in input:
        if i in countDict:
            countDict[i]+=1
        else:
            countDict[i]=1
    print (countDict)    

#2. Merge Two Dictionaries using inbuilt function '|'
#Merge overwrites the value if key is present in the added dictionary
#new element will get added at the end
#If both dicts have the same key, the right-hand dictionary’s value overwrites the left’s.
def fun2():
    dict1={
        "1":1,
        "2":1,
        "3":1,
        "5":"2",
        6:23
    }
    dict2= {
        "1":2,
        "3":2,
        "4":2,
        "5":"2"
    }
    #mergedDict=dict1 | dict2
     
    print(dict1)
    print(dict2)
    #print(mergedDict)
    print("using '|'",dict1|dict2)
    dict1.update(dict2)
    print("using update: ", dict1)
    # ** creates new dict Values from the second dict overwrite the first if keys match.
    newDict = {**dict1,**dict2}
    print('using **', newDict)
#2. Merge Two Dictionaries with Sum 
def fun3():
    mergedDict={}
    dict1={
        "1":1,
        "2":1,
        "3":1,
        "5":"2"
    }
    dict2= {
        "1":2,
        "3":2,
        "4":2,
        "5":"2"
    }
    for key,value in dict1.items():
        if key in dict2:
            mergedDict[key]=value+dict2[key]
        else:
            mergedDict[key]=value
    for key,value in dict2.items():
        if key not in mergedDict:
            mergedDict[key]=value
    print(dict1)
    print(dict2)
    print(mergedDict)

def fun4(dict4):
    from collections import defaultdict
    newDict={}
    #overwrites the duplicate keys
    print('overwrites the duplicate keys')
    for key,value in dict4.items():
        newDict[value]=key
    print(newDict)
    #To preserve duplicates converted into list
    #use defaultdict function to get invert dicitionary maintaining duplicate keys
    #convert dictionary into list
    inverted = defaultdict(list)
    for key,value in dict4.items():
        inverted[value].append(key)
    print(inverted)
    #print(inverted.keys())
    newLst=[[[key],value] for key,value in inverted.items()]
    print(newLst)

def fun5(stuDict):
#Find Top Scorer
#Problem:
#Given a dictionary of student scores, return the name(s) of the highest scorer(s).
#Given a dictionary of student scores with single highest scorer,
# and only has numeric values as well as non numerical values
#Used recursive function after creating dict with numeric values
# return the name(s) of the highest scorer(s) .
   
    try:
        highestValue = max(stuDict.values())
        keyForHighestValue = [key for key,value in stuDict.items() if value==highestValue ]
        print(max(stuDict.values())) #Works if dict has only numerical values
        print(highestValue,keyForHighestValue)
    except TypeError as e:
        print(e)
        #For dict having non numeric values 
        numDict = {key:value for key,value in stuDict.items() if isinstance(value,(int,float))}
        fun5(numDict)
        #highestValue = max(numDict.values())
        #keyLst= [key for key,value in stuDict.items() if value==highestValue]
        #print(highestValue,keyLst)

    #print([key for value in  stuDict.items() if value is max(stuDict.values())])
def fun6(lst6):
#Output: { 'abt': ['bat', 'tab'], 'apt': ['tap', 'pat'], 'act': ['cat'] }
#Group words that are anagrams using dictionaries.
    print(lst6)
    #sort the characters to get common key
    #sorted returns list of characters
    anagramDict={}
    for ele in lst6:
        key = ''.join(sorted(ele)) #convert list into a string by join
        if key in anagramDict: 
            anagramDict[key].append(ele)
        else:
            anagramDict[key]= [ele]  
    print(anagramDict)
def fun7(lst6):
    #defaultdict(list) is a special kind of dictionary from Python’s collections module.
    #Normally, KEyError raises if you try to access a key that doesn’t exist in a regular dictionary, 
    #But with defaultdict(list), if the key doesn’t exist, 
    # it automatically creates it with an empty list as the default value—no error.
    from collections import defaultdict
    print(lst6)
    print(defaultdict(list))
    anagramTD = defaultdict(list)
    #Using traditional for loop
    for word in lst6:
        key = ''.join(sorted(word))
        anagramTD[key].append(word)
    print('Dict using Tradtional For loop: ')
    print(dict(anagramTD))
    #Using comprehension
    anagramCD={}
    [anagramCD[''.join(sorted(ele))].append(ele) for ele in lst6]
    print('Dict using List Comprehension one-line code: ')
    print(anagramCD)
    print(dict(anagramCD))
def fun8(str8):
#Counter is a class from Python’s collections module designed 
# to count how many times each item appears in an iterable (like a list or string).
#It works like a dictionary where:Keys:(e.g., words or characters) 
# and Values are the counts (how many times each item occurs)
#for tradional: day01/listAssignment/10
    from collections import Counter
    import string
    #Output: {"hello": 2, "world": 1}
    print('ot: ',str8 )
    str8 = str8.lower().translate(str.maketrans('','',string.punctuation))
    strLst = str8.split()
    print('ch: ',str8)
    freqCntDict = Counter(strLst)
    print('Dict: ',dict(freqCntDict))
def fun9(keys,values):
    #Output: {"name": "Alice", "age": 25, "city": "Toronto"}
    print(keys)
    print(values)
    dictFromList=dict(zip(keys,values))   
    print(dictFromList)
def fun10(inputStr):
    import string 
    from collections import defaultdict
    #Count how many digits, letters, and special characters are in a string using a dictionary.
    #if using defaultdict from collection
    charTypeDict={}
    #charTypeDictLst= defaultdict(list)

    for ch in inputStr:
        if ch.isalpha():
            charTypeDict['letters']=charTypeDict.get('letters',0)+1
            #charTypeDictLst['letters']+=1
        elif ch.isdigit():
            charTypeDict['digits']=charTypeDict.get('digits',0)+1
        elif ch.isspace():
            charTypeDict['spaces']=charTypeDict.get('spaces',0)+1
        elif ch in string.punctuation:
            charTypeDict['punctucation'] = charTypeDict.get('punctuation',0)+1
        else:
            charTypeDict['others']=charTypeDict.get('others',0)+1
    #Output: {"letters": 5, "digits": 3, "specials": 2}
    print(inputStr)
    print(charTypeDict)
def fun11(dict11):
    #Counter counts how many time each value appears in the dict
    #input: iterable with list,string,tuple or any sequence of hashable table
    #Returns  Counter object works like a dicitionary with extra counting feature
    #most_common returns a list of tuples with sigle most common (value,count)pair
    #returns the items sorted by their counts in descending order
    #To access the most common value: most_common(1) returns list with tuple with 1st element
    #to acess the value most_common(1)[0] and count most_common(1)[0][0]
    #Output: 1
    from collections import Counter
    print(dict11)
    print(Counter(dict11))
    print(Counter(dict11.values()).most_common)
    print(Counter(dict11.values()).most_common(1))
    print(Counter(dict11.values()).most_common(1)[0][0])
def fun12(dict12): #Nested Dictionary calculate average
#Output:  {"Alice": 85.0, "Bob": 68.33}
    print(dict12)
    avg=0
    avgDict={}
    for key, value in dict12.items():
        avg=0
        for grade in value:
            avg += grade
        avgDict[key]=round(avg/len(value),2)
    print(avgDict)
    #single line solution
    avgDict1 = {key: round(sum(value)/len(value),2) for key,value in dict12.items()}
    print(avgDict1)
def fun13(cart):
    #output: Total cost: 21.8
    print(cart.values())
    costDict =sum([round(value['price']*value['quantity'],2) for key,value in cart.items()])
    print(costDict) 
#fun1() 
#fun2()
#fun3()
dict4 = {
    1:12,
    2:'Test',
    3:True,
    4:1+2j,
    5:12.3,
    6:12,
    7:6
}
#fun4(dict4) # invert a dicitionary
stuDict = {    
        "Alice":300,
        "Scott":400,
        "Luis":100,
        "Peter":400.4,
        "Willaims":"Absent"
}
#fun5(stuDict) #Find highest value
lst6 = ["bat", "tab", "tap", "pat", "cat"]
#Output: { 'abt': ['bat', 'tab'], 'apt': ['tap', 'pat'], 'act': ['cat'] }
#fun6(lst6) #Group words that are anagrams using dictionaries.
#fun7(lst6) #Group words that are anagrams using dictionaries using defaultdict collections comprehension
str8 = "Hello hello world!"
#fun8(str8) #Word Frequency in Sentence using Counter from collections. for tradional: day01/listAssignment/10
keys = ["name", "age", "city"]
values = ["Alice", 25, "Toronto"]
#fun9(keys,values) # : Create a Dictionary from Two Lists using zip function from dict
inputStr= "Hello123@!"
#fun10(inputStr) #Character Type Counter
dict11 = {"a": 1, "b": 2, "c": 1, "d": 3}
#fun11(dict11) #Most Common Value in dictionary
#dict12 dictionary with list of numbers
dict12 = {
    "Alice": [80, 90, 85],
    "Bob": [70, 60, 75]
}
#fun12(dict12) #Calculate and return a dictionary with their average scores. nested dictionary
cart = {
    "apple": {"price": 2.5, "quantity": 4},
    "banana": {"price": 1.2, "quantity": 6},
    "milk": {"price": 3.0, "quantity": 2}
}
fun13(cart) #Write a Python function to calculate and return the total cost of all items in the cart.

