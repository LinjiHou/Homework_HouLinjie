def solve_JCP_with_while(list_of_SNM, step=-1, survive_num=1, starting_person="person_name"):
    """
    'JCP' means josephus circle problem    对一个容器的一种遍历方式
    'SNM' means sequence number of member ,  assert 检查参数 target_list
    step 可以用 interval  , side effect"""

    remaining_SNM = list_of_SNM.copy()
    starting_point = remaining_SNM.index(starting_person) 
    while len(remaining_SNM) > survive_num:
        out_point=(starting_point + step - 1) % len(remaining_SNM)
        print('出去的人是 %s 号', remaining_SNM[out_point])
        remaining_SNM.pop(out_point)
        starting_point=out_point

    return remaining_SNM # 每一次踢人的顺序list




def solve_JCP_with_for(list_of_SNM, step, survive_num=1, starting_person=1):
    remaining_SNM = list_of_SNM.copy()
    starting_point = remaining_SNM.index(starting_person) 
    for i in range(len(list_of_SNM) - survive_num):
        out_point=(starting_point + step -1) % len(remaining_SNM)
        print('出去的人是 %s 号', remaining_SNM[out_point])    
        remaining_SNM.pop(out_point)
        starting_point=out_point
    return remaining_SNM
# 把JCP做成一个类型，对它直接做for，得出结果。对象特性：姓名， 学号， 性别， 




## 为什么当 step 不等于3 的时候会报错
def solve_JCP_with_recursion(list_of_SNM, step, survive_num=1, starting_person = 1 ):
    remaining_SNM = list_of_SNM
    starting_point = remaining_SNM.index(starting_person)

    if len(remaining_SNM) >  survive_num:
        out_point=(starting_point + step -1) % len(remaining_SNM)
        print('出去的人是 %s 号' , remaining_SNM[out_point])
          
        remaining_SNM.pop(out_point)
        print('还剩下', remaining_SNM)  
        return solve_JCP_with_recursion(list_of_SNM = remaining_SNM,
                                        step = step,
                                        survive_num = survive_num,
                                        starting_person = remaining_SNM[out_point]
                                        )
    else:
        return remaining_SNM

if __name__ == "__main__":
    sum = 13 # 总人数
    step = -1 # 数到step的人out
    starting_person = 1     # 从第starting_person个人开始报数
    survive_sum = 1     #最终剩下survive_sum个人

    survive_people=solve_JCP_with_while(list_of_SNM = [(x+1) for x in range(sum)],
                                            # step = step,
                                            starting_person = starting_person,
                                            survive_num = survive_sum
                                            )

    print('最终活下来的人是：', survive_people)