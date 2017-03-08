from random import choice

# Source: towwdso, SpeedSolving.net
# Will probably get rid of this and implement a way for PyCube to grab scrambles from the JS generator

def k(l, w):
    m=[y.replace(l[-1],'') for y in w] if l[-1:] else w
    h=[int(''.join(l[-2:]) in [x,x[::-1]]) for x in w]
    if 1 in h:m.pop(h.index(1))
    return m

def scramble():
    w, l = ['RL','UD','BF'], []
    
    for _ in range(30):
        l.append(choice(choice(k(l, w))))
    
    s = ""
    for x in l:
        c = choice(" '2")
        if c != ' ':
            s += x + c
    return s