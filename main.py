#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name` is not valid because it begins with a number, which is a no no for python variable names
3. `age` is valid because it follows the rules
4. `total_amount` is valid, use of underscore is correct and describes something that would probably be used in a python program for totaling something
5. `while` is invalid since we already use this, it's reserved, so we can't use it as a variable name
6. `Student` is valid because it follows the rules
7. `my-variable` is invalid because dashes aren't allowed, and it'll give you an error
8. `for` is invalid because it's already used for loops. 
9. `_temp` valid, but I usually don't start with an underscore. I can't remember what that was used for. 
10. `value#` is invalid because it uses a special character, which is against the law. The python police will get you. 

"""
# Problem 2
"""
1. `calculate_total`valid because it uses lowercase and underscore
2. `3rd_function` invalid because it starts with a number.
3. `print_values` valid, follows the rules
4. `find-item`invalid because the hypens
5. `def` invalid, this is reserved for defining a function
6. `updateProfile` valid, although my previous professor advised against a capital letter in the middle
7. `my_function` valid because it follows the rules
8. `try` is invalid because it's reserved
9. `init_data` valid, snake case and describes
10. `value@function` is invalid becauase special character


"""
# Problem 3
"""
1. `True and False` - valid. It evaluates to false because both sides of and have to be true, and since it won't be that, it will be false. 
2. `5 > 3 or "apple" < "banana"` - valid. It will evaluate to true because of the OR. Since 5 > 3, and that is true, it doesn't matter if the other operand is false.
3. `not 10 <= 20` valid. this is tricky, so the 10 <= 20 is actually true, but when you put 'not' in front of it, it becomes false. 
4. `True or 5 = 4` invalid. trying to assign 5 to be 4, instead of compare 5 to 4. should be ==
5. `"apple" != "orange" and 5` is valid. the != means not equal to, so it evaluates to true
6. `3 < 5 not True` invalid. there should be an operator after the 5. Something like 3 < 5 and not true
7. `False == (3 > 4)`valid. 3 > 4 is false, and so false == false. == means equal to
8. `10 <= "10"` invalid. when you put quotes around something it becomes a string. When you try to run this you'll get a type error
9. `True or not False` is valid. true is true and not false is true, so it will evaluate to true. 
10. `5 and or 4` invalid. you can't say and or. it has to be one or the other. I would get a syntax error if I put this in python. 


"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
