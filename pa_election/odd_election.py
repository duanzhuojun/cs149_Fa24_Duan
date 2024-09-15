"""Odd Election Tools.

Author: CS149 instructors
Version: 09/15/2024
"""
def countPopular(count0, count1, count2):
   # Invalid ballot count 
    if count0 < 0 or count1 < 0 or count2 < 0:
       return -1
    
    # Find the popular
    max_val = count0
    max_candidate = 0
    tie = 0
    
    if max_val < count1:
        max_val = count1
        max_candidate = 1
    
    if max_val < count2:
        max_val = count2
        max_candidate = 2
    
    # Detect the tie: no winner because tie
    if max_candidate == 0 and (count0 == count1 or count0 == count2):
        tie = -1
         
    if max_candidate == 1 and (count1 == count0 or count1 == count2):
        tie = -1; 
        
    if max_candidate == 2 and (count2 == count0 or count2 == count1):
        tie = -1
        
    if tie == -1: 
        max_candidate = -1
       
    return max_candidate


def countMajority(count0, count1, count2):
    # Invalid ballot count 
    if count0 < 0 or count1 < 0 or count2 < 0:
       return -1
              
    max_val = count0
    max_candidate = 0
    tie = 0
    totalCount = count0 + count1 + count2
        
    max_val = count0
    max_candidate = 0
        
    if max_val < count1:
        max_val = count1
        max_candidate = 1
    
    if max_val < count2:
        max_val = count2
        max_candidate = 2
        
    # Detect the tie: no winner because tie
    if max_candidate == 0 and (count0 == count1 or count0 == count2):
        tie = -1
         
    if max_candidate == 1 and (count1 == count0 or count1 == count2):
        tie = -1; 
        
    if max_candidate == 2 and (count2 == count0 or count2 == count1):
        tie = -1
        
    if tie == -1: 
        max_candidate = -1
    
    # no winner because not absolute majority or tie   
    if max_val < totalCount / 2 or tie == -1:
        max_candidate = -1
        
    return max_candidate;   

def isOdd(count):
    return count % 2 == 1 and count % 10 != 5

def count_odd(count0, count1, count2):

    # Invalid ballot count 
    if count0 < 0 or count1 < 0 or count2 < 0:
       return -1
        
    odd_count0 = count0
    odd_count1 = count1
    odd_count2 = count2
        
    if isOdd(count0):
        odd_count0 = count0 * 2
 
    if isOdd(count1):
        odd_count1 = count1 * 2      

    if isOdd(count2):
        odd_count2 = count2 * 2
        
    winner = countPopular(odd_count0, odd_count1, odd_count2)       
    return winner

def count_even_odder(count0, count1, count2):
    
    # Invalid ballot count 
    if count0 < 0 or count1 < 0 or count2 < 0:
       return -1
        
    odd_count0 = count0
    odd_count1 = count1
    odd_count2 = count2
         
    if count0 % 2 == 0:
        if (count0 % 10) != 4:
            odd_count0 = count0 * 2
        else:
            odd_count0 = count0 - 10

 
    if count1 % 2 == 0:
        if (count1 % 10) != 4:
            odd_count1 = count1 * 2
        else:
            odd_count1 = count1 - 10      

    if count2 % 2 == 0:
        if (count2 % 10) != 4:
            odd_count2 = count2 * 2
        else:
            odd_count2 = count2 - 10    
        
    winner = countPopular(odd_count0, odd_count1, odd_count2)
            
    return winner

    