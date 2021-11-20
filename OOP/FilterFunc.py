# The syntax of filter() method is:
# filter(function, iterable)

# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(letter in vowels):
        return True
    else:
        return False

filtered_vowels = list(filter(filter_vowels, letters))

print('The filtered vowels are:')
print(filtered_vowels)

#****************************************************************
#Using filter method without a filter method. 

# random list
random_list = [1, 'a', 0, False, True, '0'] #Last zero is string

# Filter will check and return true or false.
filtered_list = list(filter(None, random_list))

print('The filtered elements are:')
print(filtered_list)