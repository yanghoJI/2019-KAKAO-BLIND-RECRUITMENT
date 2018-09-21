## solution by yanghoJI 

#### algorithm complexity O(n)

1. food_times 의 전체 합을 totalTime 으로 저장한다.
</br>
2. food_times에 음식 번호 인덱스를 붙이고 오름차순으로 정렬한다. 

 - ex [(foodIndex, time), ...]
</br>

3. 밑과 같이 음식 하니씩을 제외해나간다.

~~~
    for info in foodTimes:
        runtime = 남은음식개수 * (현재음식남은시간 - 전체음식먹은루프개수)
~~~

</br>
4. runtime이 남은 시간 보다 크면 종료하고 멈추고 음식 인덱스 sol을 찾는다.

