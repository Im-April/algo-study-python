def second_index(text,initials):
    if text.count(initials) < 2 :
        return None
    
    first = text.find(initials)
    return text.find(initials, first+1)


s_second = second_index('sims','s')
print(s_second)

d_second = second_index('abc','d')
print(d_second)