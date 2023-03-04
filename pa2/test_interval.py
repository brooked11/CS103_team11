from Interval import Interval

def test_interval():
    ''' test the +-*/ interval operators '''
    x1 = Interval(0.9,1.1)
    x2 = Interval(1.999,2.001)
    x3 = Interval(-1,1)
    x4 = Interval(10,10)
    print('x1=',x1)
    print('x2=',x2)
    print('x3=',x3)
    print('x4=',x4)
    print('x1+x2=',x1+x2)
    print('x2*x3=',x2*x3)
    print('x3/x4=',x3/x4)
    print('x4-x1*x2/(x4+x3)-(x1+x2)',x4-x1*x2/(x4+x3)-(x1+x2))
    print(f'x1.intersect(x3)={x1.intersect(x3)}')
    print(f'x1.intersects(x3)={x1.intersects(x3)}')
    print(f'x1.intersects(x2)={x1.intersects(x2)}')

    try:
        print(x4/x3)
    except Exception as err:
        print(f'exception: "{err}"')
    try:
        a=Interval(2,-2)
    except Exception as err:
        print(f'exception: "{err}"')
    
if __name__=='__main__':
    test_interval()