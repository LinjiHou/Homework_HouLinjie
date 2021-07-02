def solve_JCP_with_while(num, step=3, survive_num=1, starting_point=1):
    """
    'JCP' means josephus circle problem
    'num' represents the total number of the team member
    """
    remaining_points=[ (x+1) for x in range(num)]

    new_starting_point=starting_point
    while len(remaining_points) > survive_num:
        out_point=(new_starting_point -1 + step) % len(remaining_points)
        print('出去的人是 ',remaining_points[out_point],' 号')    
        remaining_points.pop(out_point)
        new_starting_point=out_point
    return remaining_points


if __name__ == "__main__":
    solve_JCP_with_while(90)