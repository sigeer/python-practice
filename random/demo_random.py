import random
from collections import Counter

def win(rate: float) -> bool:
    if rate < 0:
        return False
    
    if rate > 1:
        rate = rate / 100
    return random.random() < rate
    

def get_reward(pool: dict):
    weight = 0
    total = sum(pool.values())
    random_flag = random.random()
    for item, rate in pool.items():
        weight += rate / total
        if random_flag < weight:
            return item
    raise Exception("no reward")

def get_random(arr: list):
    if (len(arr) == 0):
        return None
    
    random.shuffle(arr)
    return arr[0]

pool = {
    "石头": 1,
    "剪刀": 1,
    "布": 1,
}

all = []
for i in range(1000):
    all.append(get_reward(pool))
    
def count_elements(arr):
    counter = Counter(arr)

    print([x for x in counter.items()])

all.sort()
count_elements(all)

def guess(input: str):
    rules = list(pool.keys())
    
    from_machine = get_reward(pool)
    result = rules.index(input) - rules.index(from_machine)
    print(f"机器人出了：{from_machine}")
    if result == 0:
        print("平局")
    elif result == -1 or result == 2:
        print("赢")
    else:
        print("输")

for i in range(5):
    from_mine = get_reward(pool)
    print(f"我出了：{from_mine}")
    guess(from_mine)
    print("=========")
    
get_random([1,2,3,5])