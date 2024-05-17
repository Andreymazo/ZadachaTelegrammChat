import itertools
from a import get_total

def express_num(num_to_express, num_in_expression, number_num_in_expression):
    can_be_done = ['+', '-', '*', '/']
    filter_result_out = [num_in_expression]*number_num_in_expression
    # print(filter_result_out)

    combinations_can_be_done = list(itertools.combinations_with_replacement(can_be_done, 2))
    # print(combinations_can_be_done)
    
    # c = list(chain(*zip(a,b)))
    result_lst = []
    for t in combinations_can_be_done:
        # new_lst = list(chain(*zip(filter_result_out, t)))
        new_lst = [item for pair in zip(filter_result_out, t) for item in pair]
        new_lst.append(filter_result_out[-1])
    #     new_lst = [j for i in zip(filter_result_out, t) for j in i]
    # for i, ii in zip(filter_result_out, combinations_can_be_done):
    
        if get_total(new_lst) == num_to_express:
            result_lst.append((new_lst))
            # print(get_total(new_lst))
    print(result_lst)
if __name__ == '__main__':
    express_num(1, 2,3)
    # num_in_expression = 2
# number_num_in_expression = 3
# can_be_done = ['+', '-', '*', '/']