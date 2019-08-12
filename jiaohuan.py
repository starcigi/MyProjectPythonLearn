member = ['张贻辉','狗','李宗彬']
print(member)
member.insert(0,member[len(member)-1])
member.append(member[1])
del (member[1])
del (member[len(member)-2])
print(member)
