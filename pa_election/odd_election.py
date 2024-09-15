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


    
    