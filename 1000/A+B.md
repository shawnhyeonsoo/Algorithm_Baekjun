[Baekjun Online Judge 1000번: A+B] </br>
출처: 백준 온라인 저지</br>
문제 링크: <https://www.acmicpc.net/problem/1000> </br>



문제 </br>
</br>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. </br>
</br>
입력</br>
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10) </br>

</br>출력</br>
첫째 줄에 A+B를 출력한다.</br>

</br>
</br>
솔루션:</br>

```python
a, b = map(int,input().split())
print(a+b)
```
</br> 
> 기본적인 문제로 두 숫자를 입력 받아 그 합을 출력하는 문제인데, 처음에는 map 함수를 사용하지 않고 input.split()만으로 입력 받은 후
  다시 int로 변환하여 문제를 풀었다가 map 함수로 더 간결하게 코딩할 수 있다는 것을 알고 map을 이용하여 다시 풀어보았다.

메모리: 29380KB
시간: 64ms
