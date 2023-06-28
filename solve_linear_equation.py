def solve_linear_equation(a, b):
    if a != 0:
        x = -b / a
        return x
    elif b == 0:
        return "해가 무수히 많습니다."
    else:
        return "해가 없습니다."

# 이 함수 호출을 통해 원하는 일차방정식의 계수를 대입하여 결과를 확인하세요
a = 2
b = -4
result = solve_linear_equation(a, b)
print("결과:", result)
