import pandas as pd
####5 Questions to solve with the above dataset
#Q1: Store Count per City
#Write Python code to count how many stores are in each city and print the result.

# Store Locations
stores = [
    {"store_id": 1, "city": "Toronto", "manager": "Alice"},
    {"store_id": 2, "city": "Vancouver", "manager": "Bob"},
    {"store_id": 3, "city": "Montreal", "manager": "Charlie"},
]

# Product Prices
prices = {
    "Apples": 3.5,
    "Bananas": 2.0,
    "Milk": 4.5,
    "Bread": 3.0
}

# Sales Data
sales = pd.DataFrame({
    "store_id": [1, 2, 1, 3, 2, 1, 3, 3],
    "product": ["Apples", "Bananas", "Milk", "Apples", "Bread", "Bread", "Bananas", "Milk"],
    "quantity": [10, 20, 5, 15, 10, 12, 5, 8]
})
from collections import Counter
def storesCountPerCity():
#Write Python code to count how many stores are in each city and print the result.
    print (stores)
    storeDict={}    
    for rec in stores:
        storeDict.get(rec['city'],0)+1
    print('dict: ', storeDict)            
     #traditional Way
    #print('Traditional Way')
    
    #usiing Counter from collections
    print('Using Counter from collections')
    city_count = Counter(store['city'] for store in stores)
    print(city_count)
storesCountPerCity()