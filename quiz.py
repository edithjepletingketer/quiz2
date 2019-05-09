def list():
    x=[100,110,120,130,140,150]
    a=[b//3 for b in x]
    print(a)
    
        


def sorted():
    a=["apple","banana","mango"]
    b=["ovacado","peach","orange"]
    c=["pinneapple","lemon"]
    d=[]
    d=a+b+c
    d.sort()


def divisible_by_three(n):
    if a in range(1,n):
        a//3
        print(a)


    

def flatten():
    x=[[1,2],[3,4],[5,6]]
    flatten=[val for a in x for val in a] 


def smallest():
    a=[1,3,6,8,2,4,5.7]
    print(min(a))

def remove_duplicate():
    x=['a','b','a','e','d','b','e','f','g','h']
    print(x.remove([a]))


def squares():
    a=dict()
    numbers=range(149,159)
    for number in numbers:
        a[number]=number*number
        print(a[number])

def students():
    student1={"age":19,"name":"Eunice"}
    student2={"age":21,"name":"Agness"}
    student3={"age":18,"name":"Teresa"}
    student4={"age":22,"name":"Asha"}
    students=[student1,student2,student3,student4]

    for student in students:
        yob=2019-student["age"]
        print("Hello {}, you were born in year {}".format(student["name"],yob))



