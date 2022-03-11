n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")

"""
조건문이나 반복문의 코드블록 안에서 continue 가 실행되면,
반복 블록 안에 있는 나머지 부분을 실행하지 않고, 다음 반복 단계로 넘어간다.
즉, 반복 블록의 나머지 부분은 실행되지 않고, 다음 단계의 반복을 계속(continue)하는 것이다.
"""
