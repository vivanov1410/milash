import turtle

def draw_square(side):
  for x in range(1, 5):
    t.forward( side )
    t.left( 90 )

def draw_perfect_triangle(side):
  t.forward( side )
  t.left( 120 )
  t.forward( side )
  t.left( 120 )
  t.forward( side )

def draw_star(side):
  t.reset()
  for x in range(1, 38):
    t.forward( side )
    t.left( 175 )

def draw_baloon():
  t.reset()

  t.color(1,1,0)
  t.begin_fill()
  t.circle( 100 )
  t.end_fill()

  triangle_side = 20
  t.begin_fill()
  t.right( 120 )
  t.forward( triangle_side )
  t.left( 120 )
  t.forward( triangle_side )
  t.left( 120 )
  t.forward( triangle_side )
  t.end_fill()

  t.color(0,0,0)
  t.right( 210 )
  t.up();
  t.forward( triangle_side - 2 )
  t.down()
  t.forward( 150 )
  
t = turtle.Pen()
draw_baloon()

