def rectangle_parimeter(l,w):
    return 2*(l+w)
print(rectangle_parimeter(2,5))  



def beginwithanA(name):
    return name[0]=='A'

def namesBeginwithanA(Students_name):
    for name in Students_name:
        if (beginwithanA(name)):print(name)

file = open("C:\My studies\CLA\Inputs\Students_name.txt")
names= file.read()
names= names.split()
namesBeginwithanA(names)

