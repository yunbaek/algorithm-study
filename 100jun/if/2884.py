input_data = input().split(' ')
h = int(input_data[0])
m = int(input_data[1])

m_1 = m - 45

if m_1 < 0:
    m_1 += 60
    h -= 1
    if h < 0:
        h += 24

print(h, m_1)
