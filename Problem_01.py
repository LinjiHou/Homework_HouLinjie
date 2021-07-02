"""
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import random 
import string

base_str = string.ascii_letters + string.digits
def generate_key(len):
    random_str = []
    for i in range(len):
        if (i % 5 == 0) & (i != 0) :            
             random_str.append('_')
        random_str.append(random.choice(base_str))
    # print(key)
    return "".join(random_str) 

if __name__ == "__main__":
    L=[]
    for i in range(200):
        L.append(generate_key(16))
    # print(L)


