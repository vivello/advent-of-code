# Part 1
# Find 2 most active monkeys after 20 rounds and multiply number of inspections each does
# 56120

# Part 2
# Find 2 most active monkeys after 1000 rounds (manage worry numbers so they aren't massive)
# 24389045529

from math import prod

class Monkey:
    def __init__(self, items, operation, test, mt, mf):
        self.items = items
        self.operation = operation
        self.test = test
        self.m_true = mt
        self.m_false = mf
        self.inspected = 0

    def __str__(self):
        return f"Holding: {self.items}\nInspected: {self.inspected}"

def make_monkey(m_lines):
    start = [int(x.strip(',')) for x in m_lines[1].strip().split()[2:]]
    op = m_lines[2].strip().split()[-2:]
    if op[1] != 'old':
        op[1] = int(op[1])
    div = int(m_lines[3].strip().split()[-1])
    mt = int(m_lines[4].strip().split()[-1])
    mf = int(m_lines[5].strip().split()[-1])
    return Monkey(start,op,div,mt,mf)

def new_worry(operator,op_value,old_worry):
    ops = {'+': lambda x,y: x + y,
           '*': lambda x,y: x * y}
    if op_value == 'old':
        return ops[operator](old_worry,old_worry)
    else:
        return ops[operator](old_worry,op_value)

def throw(m_dict, rounds):
    mod = prod([m.test for i,m in m_dict.items()])
    for i in range(rounds):
        for j,m in m_dict.items():
            how_many = len(m.items)
            m.inspected += how_many
            for k in range(how_many):
                to_throw = m.items.pop(0)
                new = new_worry(m.operation[0],m.operation[1],to_throw)
                if (new % m.test) == 0:
                    m_dict[m.m_true].items.append(new % mod)
                else:
                    m_dict[m.m_false].items.append(new % mod)
    return sorted([(v.inspected,n) for n,v in m_dict.items()])[-2:]

def main(file_name):
    monkeys = {}
    with open(file_name) as f:
        inp = f.readlines()
        for i in range(8):
            m_start = i * 7
            monkeys[i] = make_monkey(inp[m_start: m_start + 7])
        return throw(monkeys,10000)
        
