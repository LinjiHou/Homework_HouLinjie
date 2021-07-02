def solve_JCP_with_while(num, step=3, survive_num=1, starting_point=1):
    """
    'JCP' means josephus circle problem
    'num' represents the total number of the team member
    """
    remaining_points=[ (x+1) for x in range(num)]
    new_starting_point = starting_point - 1 
    while len(remaining_points) > survive_num:
        out_point=(new_starting_point + step - 1) % len(remaining_points)
        print('出去的人是 ',remaining_points[out_point],' 号')    
        remaining_points.pop(out_point)
        new_starting_point=out_point
    return remaining_points

def solve_JCP_with_for(num, step=3, survive_num=1, starting_point=1):
    remaining_points=[ (x+1) for x in range(num)]
    new_starting_point = starting_point -1 
    for i in range(num - survive_num):
        out_point=(new_starting_point -1 + step) % len(remaining_points)
        print('第 %s 个出去的人是 '% (i+1), remaining_points[out_point],' 号')    
        remaining_points.pop(out_point)
        new_starting_point=out_point
    return remaining_points

## 下面还在改
def solve_JCP_with_recursion(num, step=3, survive_num=1, starting_point=1):
    remaining_points=[ (x+1) for x in range(num)]
    
    if len(remaining_points) > num - survive_num:
        new_starting_point = starting_point -1 
        out_point=(new_starting_point -1 + step) % len(remaining_points)
        print('第 %s 个出去的人是 '% (i+1), remaining_points[out_point],' 号')    
        remaining_points.pop(out_point)
        new_starting_point=out_point
    return remaining_points

if __name__ == "__main__":
    survive_people=solve_JCP_with_for(5, survive_num=1)
    print('最终活下来的人是：', survive_people)