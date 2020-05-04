[Baekjun Online Judge 1001번: A-B] </br>
출처: 백준 온라인 저지</br>
문제 링크: <https://www.acmicpc.net/problem/1001> </br>



문제 </br>
</br>두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오. </br>
</br>
입력</br>
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10) </br>

</br>출력</br>
첫째 줄에 A-B를 출력한다.</br>

</br>
</br>
솔루션:</br>

```python
a, b = map(int,input().split())
print(a-b)
```
</br> 

> 앞서 풀었던 1000번: A+B 문제에서 '+' 를 '-'로 바꿔 응용하는 문제로 어렵진 않은 기본 문제로,
  어렵진 않았으나 map 함수 사용에 익숙해질 수 있었던 문제였다.

메모리: 29380KB
시간: 64ms
