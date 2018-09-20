input = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo','Leave uid1234','Enter uid1234 Prodo','Change uid4567 Ryan']

Dic = {}
for line in input:
    word = line.split(' ')
    if word[0] == 'Enter' or 'Change':
        Dic[word[1]] = word[2]
    else:
        pass

Output = []
for line in input:
    word = line.split(' ')
    if word[0] == 'Enter':
        Output.append('%s님이 들어왔습니다.' % str(Dic[word[1]]))
    elif word[0] == 'Leave':
        Output.append('%s님이 나갔습니다.' % str(Dic[word[1]]))
    else:
        pass

print(Output)