import turtle as t
t.shape('turtle')

# 삼각형 그리기
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

# 사각형 그리기
t.pencolor("blue")
for _ in range(4):
    t.left(90)
    t.forward(150)

# 삼각형 그리기
t.pencolor("green")
t.goto(100, -100)
t.goto(-100, -100)
t.home()