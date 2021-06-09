# 택시 기하학에서 중심이 (0,0)이고 반지름이 r인 원을 좌표평면에 그린다고 하자.
# 제 1사분면에 포현되는 모습은 x + y = r 형태이므로 좌표평면과 그래프로 둘러쌓인 도형은 직각이등변삼각형이 된다.
# 즉 원의 넓이는 2 * (r ** 2) 가 된다.
import math

r = int(input())

u_circle = math.pi * r * r
print('%0.6f'%u_circle)
t_circle = 2 * r * r
print('%0.6f'%t_circle)