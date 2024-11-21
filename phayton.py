def even_number(*args):
    
    if num % 2 == 0:
        print('число четный')
    else:
        print('не чётный')
        return 'введите другой'
        
num = int(input('ваш число '))        
print(even_number(num))    