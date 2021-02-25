# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
# Refactored.
import math 
import pytest

def display_grade_stat():
    """Gathers stats and print them out."""
    # grade_list = read_input()
    
    # Calculate the mean and standard deviation of the grades
    mean, standard_deviation = calculate_stat([1,2,3,4,5])
    # print out the mean and standard deviation in a nice format.
    print_stat(mean, standard_deviation)

def read_input():
    """Get the inputs from the user."""
    grade_list = []
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calculate_stat(grade_list):
    """Calculate the mean and standard deviation of the grades."""
    if not grade_list:
        return float('NaN')
    
    total = 0
    for grade in grade_list:
        if isinstance(grade, float) or isinstance(grade, int):
            total = total + grade
                    
            mean = total / len(grade_list)
            sum_of_sqrs = 0 
        else:
            return None 
            
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list)) # standard deviation
    return mean, sd

def print_stat(mean, sd):
    """print out the mean and standard deviation in a nice format."""
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

def test_calculate_stat():
    pass
    # with pytest.raises(TypeError):
    assert calculate_stat([1,2,3,4,5]) == (3.0, 1.4142135623730951)
    assert calculate_stat([0]) == (0.0, 0.0)
    assert calculate_stat('hello') == None
    
    

display_grade_stat()