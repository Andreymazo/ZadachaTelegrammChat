
def evaluate_expression(lst):
    result = lst[0]
    for i in range(1, len(lst)-1, 2):
        if lst[i] == '+':
            result += lst[i+1]
        elif lst[i] == '-':
            result -= lst[i+1]
    return result
"""Функция находит убирает деление и два числа вокруг и вставляет на его место его значение"""
def evaluate_expression_devide(lst):
    for i in range(1, len(lst)-1, 2):
        result = lst[i-1]
        # while '/' not in lst:
        if i<len(lst)-1 and lst[i] == '/':  
            # print('i', i)
            result /= lst[i+1]
            # print(result)
            lst_result = lst[0:i-1]+lst[i+2:]
            lst_result.insert(i-1, int(result))
            # print('lst_result', lst_result)
            return lst_result
        elif i == len(lst)-1 and lst[i] != '/':
            return lst

"""Функция находит убирает умножение и два числа вокруг и вставляет на его место его значение"""
def evaluate_expression_multiple(lst):
    for i in range(1, len(lst)-1, 2): 
        result = lst[i-1]
        if i<len(lst)-1 and lst[i] == '*':   
            # print('i', i)
            result *= lst[i+1]
            # print(result)
            lst_result = lst[0:i-1]+lst[i+2:]
            lst_result.insert(i-1, int(result))
            # print('lst_result', lst_result)
            return lst_result
        elif i == len(lst)-1 and lst[i] != '*':
            return lst

"""Функция убирает деление"""
def evaluate_expression_devide_all(lst):
    while '/' in lst:
        lst = evaluate_expression_devide(lst)
    return lst

"""Функция убирает умножение"""
def evaluate_expression_multiple_all(lst):
    while '*' in lst:
        lst = evaluate_expression_multiple(lst)
    return lst

"""Функция считает"""    
def get_total(lst1):
    lst1 = evaluate_expression_devide_all(lst1)
    lst1 = evaluate_expression_multiple_all(lst1)
    # print(lst1) 
    total = evaluate_expression(lst1)
    print(total)
    return(total)


if __name__ == '__main__':
    lst1 = [2, '/', 2, '*', 3, '-', 2, '+', 3, '-', 4, '*', 2 , '/', 2]
    get_total(lst1)
    
