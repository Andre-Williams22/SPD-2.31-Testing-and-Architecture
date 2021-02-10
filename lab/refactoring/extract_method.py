# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

def print_stat():
    '''Prints Statistics'''
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
        
    mean = calculate_mean(grade_list)
    sd = calculate_std(grade_list, mean)

    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')
    
    return grade_list 

def calculate_mean(grade_list):
    '''Calculates means given a list'''
    # Calculate the mean and standard deviation of the grades
    sum_grades = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum_grades = sum_grades + grade
    mean = sum_grades / len(grade_list)
    
    return mean
    
    
def calculate_std(grade_list, mean):
    '''Calculates STD'''
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    
    return sd 
    

