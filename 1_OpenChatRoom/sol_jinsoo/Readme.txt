input 중에 먼저 1줄(line)을 읽는다.
그 줄을 3개의 단어(word)로 나눈다.
line : word[0] (=상태) , word[1] (=uid) , word[2] (=닉네임)
상태가 Enter 또는 Change일 경우, uid를 Dic에 저장하여 완성.

다시 line을 읽어오면서 단어를 나누고,
word[0] (=상태)에 맞는 uid의 닉네임을 찾아 
Output에 문자열을 append 해준다. (%s 사용)

Output 출력.
