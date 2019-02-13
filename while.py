# while loop using add of array element 

a = [1,2,3,4,5]
summ = 0
count = 0
while (count < len(a)):
    summ = summ + a[count]
    count+=1

print(summ)



# check even or add number

a = [1,2,3,4,5]
even = []
odd = []
count = 0
while (count < len(a)):
   
      
    # checking condition 
    if a[count] % 2 == 0: 
        even.append(a[count])
    else: 
        odd.append(a[count])
      
    # increment num  
    count += 1
      
print("Even numbers in the list: ", even) 
print("Odd numbers in the list: ", odd)  
    
