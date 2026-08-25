def biggie_size(num):
    for i in range(len(num)):
        if num[i]>0:
            num[i]='big'

    return num   

print(biggie_size([-5, 2, 6, -8, -10, 8 ]))    

#_______________________________________________________

def count_positives(num):
    sum=0
    for i in num:
        if i > 0:
            sum+=i
    num[len(num)-1]=sum    
    return num
print(count_positives([0,1,2,3,4,5,6,7,8,9,10,11,12]))  

#_________________________________________________________

def sum_total(num):
    sum=0
    for i in num:
        sum+=i
    return sum
print(sum_total([0,2,3,10,15,18,2,20,50]))   

#__________________________________________________________

def average_num(num):
    average=0
    sum=len(num)
    for i in num:
        average=(average+i)
    return average/sum
print(average_num([2,4,6,8,10,12]))    

#___________________________________________________________

def minimum(num):
    min_value=num[0]
    for i in num:
        if i < min_value:
            min_value=i
    return min_value  
print(minimum([15,20,5,17,18,60,2,-1,0]))        
