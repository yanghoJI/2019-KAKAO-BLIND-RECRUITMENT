실패율 : 

스테이지에 도달한 플레이어 중 클리어 못한 플레이어 수 / 스테이지에 도달한 플레이어 수

제약 :

전체 스테이지 : N

사용자의 도달 현황 : stages (배열)

<hr>

실패율을 내림차순으로 정렬하여 해당 번호가 리턴되어야 함.

실패율 같으면 작은 번호 우선.

도달못한 스테이지 -> 실패율 0 처리

<hr>

알고리즘

1. index로 스테이지 상태 dict 하나 생성하고,

2. for 문을 돌면서 모든 스테이지의 실패율 계산.

3. dict의 값을 기준으로 내림차순 정렬하여 key 값을 차례대로 새로운 list에 추가한다.
