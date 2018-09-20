# solution by yanghoJI

1. 데이터를 열 별로 다시 정렬한다.

2. 열 index를 돌면서 1 ~ 열 개수 만큼 조합 할수 있는 경우의 수(nCk)를 만들면서 다음을 확인한다.
- 만약 유일성을 만족하는 열 index를 알아내면 sollist에 append한다.
- 위에서 추가한 열 index는 조합 할 수는 경우에서 제거한다.

3. n < k 가 되면 종료한다.
