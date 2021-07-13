

def solve_JCP_with_while(players_list, step, survive_num=1, start_player="name"):

    
    remaining_players = players_list.copy()
    start_point = players_list.index(start_player) 
    out_order = []
    while len(remaining_players) > survive_num:
        out_point=(start_point + step - 1) % len(remaining_players)
        out_order.append(remaining_players[out_point])
        remaining_players.pop(out_point)
        start_point = out_point
    # out_order.append(remaining_players)

    return out_order, remaining_players # 每一次踢人的顺序list




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
    sum = 8 # 总人数
    players_list = [(x+1) for x in range(sum)]
    out_order, survivor = solve_JCP_with_while(
                                            players_list = players_list,
                                            step = 3,
                                            start_player = 1,# 从name = start_person开始报数
                                            )
    for out_player in out_order:
        print('out ==> name:',out_player)

    print('最终活下来的人是：', survivor)