def solve_JCP_with_while(list_of_SNM, step, survive_num=1, starting_person=1):
    """
    'JCP' means josephus circle problem
    'SNM' means sequence number of member
    """
    remaining_SNM = list_of_SNM
    starting_point = remaining_SNM.index(starting_person) 

    while len(remaining_SNM) > survive_num:
        out_point=(starting_point + step - 1) % len(remaining_SNM)
        print('出去的人是 %s 号',remaining_SNM[out_point])    
        remaining_SNM.pop(out_point)
        starting_point=out_point
    return remaining_SNM

def solve_JCP_with_for(list_of_SNM, step, survive_num=1, starting_person=1):
    remaining_SNM = list_of_SNM
    starting_point = remaining_SNM.index(starting_person) 
    
    for i in range(len(list_of_SNM) - survive_num):
        out_point=(starting_point + step -1) % len(remaining_SNM)
        print('出去的人是 %s 号', remaining_SNM[out_point])    
        remaining_SNM.pop(out_point)
        starting_point=out_point
    return remaining_SNM

## 下面还在改
def solve_JCP_with_recursion(list_of_SNM, step, survive_num=1, starting_person = 1 ):
    remaining_SNM = list_of_SNM
    starting_point = remaining_SNM.index(starting_person)

    if len(remaining_SNM) >  survive_num:
        out_point=(starting_point + step -1) % len(remaining_SNM)
        print('出去的人是 %s 号' , remaining_SNM[out_point])    
        remaining_SNM.pop(out_point)
        return solve_JCP_with_recursion(list_of_SNM = remaining_SNM,
                                        step = step,
                                        survive_num = survive_num,
                                        starting_person = remaining_SNM[out_point]
                                        )
    else:
        return remaining_SNM

if __name__ == "__main__":
    sum = 13 # 总人数
    step = 3 # 数到step的人out
    starting_person = 1     # 从第starting_person个人开始报数
    survive_sum = 1     #最终剩下survive_sum个人

    survive_people=solve_JCP_with_recursion(list_of_SNM = [(x+1) for x in range(sum)],
                                            step = step,
                                            starting_person = starting_person,
                                            survive_num = survive_sum
                                            )

    print('最终活下来的人是：', survive_people)