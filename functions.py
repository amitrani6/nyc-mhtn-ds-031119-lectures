# Make a function to determine if a number is odd or even

def odd_even(number):
    if number%2==0:
        return True
    else:
        return False

# Make a function that takes in a list of numbers and returns the numbers that are even

def even_list(numbers):
    even_numbers = []
    for number in numbers:
        if odd_even(number)==True:
            even_numbers.append(number)
    return even_numbers


# Given a list return the unique names in the list

def unique_names(list_of_names):
    unique_names=[]
    for name in list_of_names:
        if name.isinstance(list_of_names):
            unique_names.append(name)
    return unique_names


# Make a function that determines if a word is a palindrome

#def palindrome_detector(string):
    """
    Input: string
    returns : True/False"""
    pass

print(odd_even(4))
print(odd_even(139))
print(even_list([1,3,4,6,7]))
print(unique_names(['john', 'john', 'john']))
#print(palindrome_detector('racecar'))
#print(palindrome_detector('not'))
