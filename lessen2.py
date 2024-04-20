def print_params(a = 1, b = 'hi',c = True):
    print(a,b,c)
print_params()

def print_params(a,b,c):
    print(a,b,c)
print_params(1,'hi',False)

def print_params(b = 25,c= [1,2,3]):
    print(b,c)

print_params()

def print_params(a,b,c):
    print(a,b,c)
values_list=[1,'Andrey',True]

print_params(*values_list)

def print_params(a,b,c):
    print(a,b,c)
values_dict={'a':234,'b':245,'c':323}

print_params(**values_dict)

def print_params(a,b):
    print(a,b)
values_list_2= ['res',True]

print_params(values_list_2,42)