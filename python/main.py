
def count_down(n):
    list1=[]
    for i in range(n,-1,-1):
        list1.append(i)
    return list1    
print(count_down(5))

#___________________________________________________________
def print_and_return(non):
    
    print(non[0])

    return(non[1])

print_and_return([1,2])

print(print_and_return([1,2]))

#_____________________________________________________________
  
def first_plus_length(list):

    return(list[0]+len(list))

print(first_plus_length([1, 2, 3, 4, 5]))

#_____________________________________________________________

def value_greater_than_second(num):
    list2=[]
    n=0
    for x in num:
        if x>num[1]:
            list2.append(x)
            n+=1
    print(n)
    return list2
print(value_greater_than_second([5, 2, 3, 2, 1, 4]))

#_______________________________________________________________

def lenght_and_value(num):
    non=[]
    for i in range(num[0]):
        non.append(num[1])
    return non
print(lenght_and_value([4,7])) 

#______________________________________________________________







