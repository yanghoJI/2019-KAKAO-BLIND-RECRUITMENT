## solution by yanghoJI

1. 스테이지 수 N 만큼의 0으로 찬 리스트(Clist)를 만든다.

2. 입력 받은 클리어 리스트를 conunt sort 한다.

3. 역순으로 Clist를 돌면서 밑을 확인한다.

- 만약 값이 0이면 zerolist에 index를 append 한다.

- 값이 0보다 크면 실패율을 계산한다. 실패율 = 현재 값 / 누적 값 

(index, 실패율) 튜플을 orderlist에 append 한다.

4. orderlist를 sort 한다.

5. sol = orderlist + zerolist
  
