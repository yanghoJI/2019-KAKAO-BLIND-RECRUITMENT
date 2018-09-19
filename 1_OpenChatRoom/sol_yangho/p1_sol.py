
input = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo','Leave uid1234','Enter uid1234 Prodo','Change uid4567 Ryan']

# get idDict
idDict = {}
for info in input:
    info = info.split(' ')
    cmd = info[0]
    if cmd in ('Enter', 'Change'):
        idDict[info[1]] = info[2]
    else:
        pass

# make solution list
solution = []
for info in input:
    info = info.split(' ')
    cmd = info[0]
    if cmd == 'Enter':
        solution.append("{}님이 들어왔습니다.".format(idDict[info[1]]))
    elif cmd == 'Leave':
        solution.append("{}님이 나갔습니다.".format(idDict[info[1]]))
    else:
        pass

print(solution)