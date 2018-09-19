# solution by yanghoJI

1. input list를 이용해서 각 사용자의 최종 닉네임을 사전형태로 저장한다.

ex)

input : 

[“Enter uid1234 Muzi”, “Enter uid4567 Prodo”,“Leave uid1234”,“Enter uid1234 Prodo”,“Change uid4567 Ryan”] 

outdict : 

iddict = {'uid1234' : 'Prodo', 'uid4567' : 'Ryan'}



2. input list를 다시한번 돌면서 enter, leave를 처리한다. 이때 iddict에서 닉네임을 검색해서 사용한다.

outstr = "{}님이 들어왔습니다.".format(iddict['uid1234']
