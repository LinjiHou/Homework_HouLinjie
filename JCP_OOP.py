import zipfile  ##要去用for循环完成遍历
import csv
import chardet
import os 

class reader(object):
    def get_players_list(self):
        raise NotImplementedError

class txt_reader(read):
    def __init__(self, path):
        self.path = path

    def get_players_list(self):
        with open(self.path) as fp: 
            people_str = fp.readlines()
        players_list = []
        for line in people_str:
            line = list(line.strip().split(' '))
            players_list.append(line)
        return players_list

class csv_reader(read):
    def __init__(self, path):
        self.path = path

    def get_players_list(self):
        players_list = []
        with open(self.path) as csvfile: 
            readcsv = csv.reader(csvfile, delimiter = ',')
            for row in readcsv:
                players_list.append(row)
        return players_list

class zip_reader(read):
    def __init__(self, path):
        self.path = path

    def get_players_list(self):
        players_list = []
        with zipfile.ZipFile(self.path, 'r') as zf: #打开zip中的.txt文件
            first_file_name = zf.namelist()[1]
            people_betye = zf.read(first_file_name)
            people_str = people_betye.decode(chardet.detect(people_betye)['encoding'])#解码 
        temp = list(people_str.strip().split('\r')) #\r 表示回车
        for x in temp:
            x = list(x.strip().split(' '))
            players_list.append(x)
        return players_list


"""    def get_players_list(self):  #打开zip中的.csv文件
        players_list = []
        with zipfile.ZipFile(place, 'r') as zf: 
            first_file_name = zf.namelist()[0]
            people_betye = zf.read(first_file_name)
            people_str = people_betye.decode(chardet.detect(people_betye)['encoding'])#解码 
        temp = list(people_str.replace('\r','').split('\n'))
        for x in temp:
            x = list(x.strip().split(','))
            players_list.append(x)
        return players_list"""


def read(path):
    file = os.path.splitext(path)
    filename, type = file
    if type == '.txt':
        return txt_reader(path).get_players_list()
    elif type == '.csv':
        return csv_reader(path).get_players_list()
    elif type == '.zip':
        return zip_reader(path).get_players_list()
    else:
        pass


class person():
    def __init__(self, id, name, hub):
        self.id = id
        self.name = name
        self.hub = hub

def get_person_list(players_list):#获得对象列表     #   依次出局的名单
    person_list = Josephus()
    for i in (range(len(players_list))):#行数
        temp = person(players_list[i][0], players_list[i][1], players_list[i][2])
        person_list.append(temp)
    return person_list
    
"""
class Josephus():
    def __init__(self):
        self.people = []
    
    def append(self, Person):
        self.people.append(Person)
        return self.people

    def get_out_person(self, step, start_num):
        total_num = len(self.people)
        i = 0
        while i < (total_num - 1):
            start_num = (start_num + step - 1) % len(self.people)#测试
            yield self.people[start_num] #生成器代替return
            del self.people[start_num] 
            i += 1
#start_point = remaining_SNM.index(start_person)"""

def solve_JCP(players_list, step, survive_num=1, start_player="name"):
    remaining_players = players_list.copy()
    start_point = players_list.index(start_player) 
    out_order = []
    while len(remaining_players) > survive_num:
        out_point=(start_point + step - 1) % len(remaining_players)
        out_order.append(remaining_players[out_point])
        remaining_players.pop(out_point)
        start_point = out_point
    return out_order, remaining_players 

if __name__ == '__main__':
    players_list = read('stu_info.txt')
    out_order, survivor  = solve_JCP(players_list = players_list,
                                    step = 3,
                                    start_player = '侯琳杰',
                                    )

    for x in out_order:
        print('out ==> name:',x.name, 'gender:',x.gender, 'age:',x.age)

    survival = person_list.people[0]
    print('survival ==> name:',survival.name, 
        'gender:',survival.gender, 
        'age:',survival.age)


#*************约瑟夫类测试***********************
def test(people_list, start_num, interval):
    person_list = get_person_list(people_list)
    killed_person = person_list.get_out_person(start_num, interval)
    killed_list = []
    for x in killed_person:
        killed_list.append(x.name)
    #survival = person_list.people[0]
    return killed_list

people_list = [[1,2,3],[4,5,6],[7,8,9]]    

dead_list1 = test(people_list, -1, 1)
assert(dead_list1 == [7,1]) #start_num = -1，interval = 1

dead_list2 = test(people_list, 1, -1)
assert(dead_list2 == [7,1]) #start_num = -1，interval = -1

#*************读取文件reader类测试**************
people_list0 = reader('py.txt')
assert people_list0[0][1] == '女'

people_list1 = reader('py.csv')
assert people_list1[0][0] == '妮妮'

people_list3 = reader('people.zip')
assert people_list3[0][1] == '女'