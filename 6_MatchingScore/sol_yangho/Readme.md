## solution by yanghoJI 

- nameDict = {'url1' : index, 'url2' : index, ...}을 만든다.
- scoreList = [(index1, score1), (index2, score2), ...]을 만든다.
- 그리고 각각의 html에 대해서 다음을 수행한다.

1. body 부분을 참조하여 기본점수 baseScore 를 해당 url1의 score에 더한다.

2. 링크를 한 곳에 줄 링크 점수를 계산하여 outScore에 저장해 놓는다. 
    
    outScore = baseScore / numOflink 

- 각각의 html parser class를 돌면서 outScore를 나눠준다.

- scoreList score 기준으로 정렬한다.
