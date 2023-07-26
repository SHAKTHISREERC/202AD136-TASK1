from flask import Flask 

fibo=Flask(__name__)

@fibo.route('/')
def fibo(n):
    if n<0:
        print('invalid')
    elif n==0:
        return 0 
    elif n==1:
        return 1 
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(11))

if __name__=='__main__':
    fibo.run()