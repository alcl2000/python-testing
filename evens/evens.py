def even_number_of_evens(numbers):
    """
    should raise a type error if a list is not typed into the function
    error message "a list was not typed into function"
    if numbers is empty return false
    if number of even numbers is odd return false
    if number of even numbers is 0 return false
    if number of even numbers is even return true
    """
    if isinstance(numbers, list):
        evens = (sum([1 for n in numbers if n % 2 == 0]))
        return True if evens and evens % 2 == 0 else False
        
    else:
        raise TypeError("A list was not being passed into the function")


if __name__ == "__main__":
    print(even_number_of_evens([1, 2, 4]))