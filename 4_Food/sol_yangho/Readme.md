## solution by yanghoJI 

1. food_times 의 전체 합을 totalTime 으로 저장한다.
</br>
2. food_times에 음식 번호 인덱스를 붙이고 오름차순으로 정렬한다. 

- ex [(foodIndex, time), ...]
</br>
3. 밑과 같이 음식 하니씩을 제외해나간다.

~~~
for info in food_times
   runtime = time * len(남은 음식)
~~~

</br>
4. runtime이 남은 시간 보다 크면 종료하고 멈춤 음식 인덱스 sol을 찾는다.

