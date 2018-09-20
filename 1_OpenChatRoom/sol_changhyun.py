
def solution(input):
    answer = []

    for x in input:
        line = x.split(" ")
        #print(line[0])
        if line[0] == "Enter":
            temp = []
            for y in answer:
                #print(y)
                if y.find(line[1]) != -1:
                    y = y.replace(y.split(" ")[2], line[2])
                temp.append(y)
            answer = temp
            answer.append(x)
        elif line[0] == "Leave":
            # normally!
            for y in answer:
                ansline = y.split(" ")
                if ansline[1] == line[1]:
                    answer.append(x+' '+ansline[2])
                    #print(x+' '+ansline[2])
                    break
        elif line[0] == "Change":
            #닉네임 싹 바꿔주기.
            temp = []
            for y in answer:
                if y.find(line[1])!=-1:
                    y = y.replace(y.split(" ")[2],line[2])
                temp.append(y)
            answer = temp


    answer = trans(answer)
    return answer

def trans(answer):

    #print(answer)
    statement = []
    for x in answer:
        splitx = x.split(" ")
        if splitx[0] == "Enter":
            statement.append(splitx[2]+"님이 들어왔습니다.")
        elif splitx[0] == "Leave":
            statement.append(splitx[2]+"님이 나갔습니다.")

    return statement

input = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(input))
#answer = [“Prodo님이 들어왔습니다.”, “Ryan님이 들어왔습니다.”, “Prodo님이 나갔습니다.”, “Prodo님이 들어왔습니다.”]
