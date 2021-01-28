# -*- coding: utf-8 -*-
"""
Gauss - Jordan Elimination Helper

Created on Thu Jan  7 15:36:44 2021

Notice: This program is in no way meant to be used to cheat.
        Use this program only to check your answers
        and improve your understanding of gauss - jordan elimination
        especially for ungraded practice problems
        
        or
        
        if you are an instructor, tutor, or TA,
        use this to find answers for arbitrary example problems quickly
        
        ie: you want to give students an arbitrary matrix to solve 
            and no answer has been provided for this arbitray matrix you just came up with

@author: chris sarkisyan
"""
'''
_____________________________________________________________________________

documentation key (for quick search):  
    -#todo: points out things that need to be added/ changed
    -#temp: shows where an item, or the state of an item is temporary
_____________________________________________________________________________    
    
'''
import numpy

#todo: add a feature to let user not see extra instructions if they re-start the program loop

'''
variables

'''
#array holding all seperate .txt files referenced in the program:
t_files = ["disclaimer_message.txt", "input_instructions.txt", "input_instructions_2.txt", "step_1.txt", "step_1_b.txt", "step_2.txt"]
#for a list fo which index corresponds to which file and it's meaning, see details.txt in the folder

orig_m = None #will hold the original matrix
cur_m = None #will hold current matrix
temp_m = None #will hold temporary row opperation results
cur_num = None #will hold entries used in opperations
cur_scale = None #will hold scalars used in opperations
'''
functions

'''
def init_matrix (in_m, in_n):
    print(print_f(t_files[2]))
    matrix = numpy.zeros((in_m, in_n))
    
    
    for i in range(in_m):
        for j in range(in_n):
            print(i, ",", j, ": ")
            matrix[i][j] = input()
        
    #todo: input nessisary code here
    
    return matrix

def print_f (file_name):
    temp_file = open(file_name)
    print(temp_file.read())
    temp_file.close()
    
    
def reset_file (): #do we need this at all?
    print()#temp placeholder

def go():
    input("Press 'enter' to continue")
'''
running portion of the code:

'''
print("\n\n", print_f(t_files[0]), "\n\n") #prints disclaimer message

print(print_f(t_files[1]))

#todo: make it so that m and n cannot be double

m = int(input("\tm = "))
n = int(input("\tn = "))

orig_m = init_matrix(m, n)
cur_m = numpy.copy(orig_m)

print("\n\nThe matrix you have entered is:\n", orig_m) #todo: add an option to re-enter the matrix if there is a mistake
go()


for row in range(m):                                #row will reffer to the current row being worked
    print("\n\nRow ", row, ":\n")
    print_f(t_files[3])
    go()
    print_f(t_files[4])
    
    # print("\nthe number I need to divide by itself: ")#temp testor statement
    # print(orig_m[row][row])#temp testor statement
    
    cur_scale = orig_m[row][row]#stores pivot entry
    
    cur_scale = float(orig_m[row][row]) 
    # print("cur scale = ", cur_scale) #temp testor
    
    cur_m = orig_m
    for index in range(n):    
        cur_num = float(orig_m[row][index])
        #print("cur num = ", cur_num)#temp testor #temp testor
        cur_m [row][index] = float(cur_num / cur_scale) 
        
    
    print(cur_m)
    orig_m = cur_m
    go()
    
   
    print_f(t_files[5])
   
    if(row == 0): #case if current row is top-most row
            print("you're working from the top-most row")#temp testor
            start = 1
    elif(row == m-1): #case if current row is bottom-most row
            print("you're working from the bottom-most row")#temp testor
            start = 0
    else:
            print("you're working from a middle row")#temp testor
            #figure out what to do here
            
    
    for oRow in range(m-1):                     #oRow will reffer to the current, other row being compared to the current row
        print("Other Row ", oRow + 1, ":")
        
        temp_m = cur_m[row]
        
        print("temp m = ", temp_m)
        
        cur_scale = cur_m[start + oRow][row]
        print("scalar", cur_scale)
        
        temp_m *= cur_scale
        print("temp m = ", temp_m)
        
        temp_m -= cur_m[start + oRow]
        print("temp m = ", temp_m)
        
        print(cur_m)
        
        cur_m[start + oRow]  = temp_m      #todo: this doesn't work
        
        print(cur_m)
            
        #todo: get the first non-pivot entry in oRow. (make it cur_scale)
        
        
        go()
    