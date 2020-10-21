import re

def b_t_d(a):
    b = int(str(a),2)
    return b

def o_t_d(a):
    b = int(str(a),8)
    return b

def h_t_d(a):
    b = int(str(a),16)
    return b


def d_t_b(a):
    b = '{:016b}'.format(int(a))
    c = re.compile('.{4}')
    d = '  '.join(c.findall(b))
    return d

def d_t_o(a):
    b = '{:016o}'.format(int(a))
    c = re.compile('.{4}')
    d = '  '.join(c.findall(b))
    return d

def d_t_h(a):
    b = '{:016x}'.format(int(a))
    c = re.compile('.{4}')
    d = '  '.join(c.findall(b))
    return d


# def negative(n):
#     a = n&0xfff
#     b = '{:b}'.format(a)
#     return b


