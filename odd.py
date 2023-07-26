from flask import Flask 

odd=Flask(__name__)

@odd.route('/')
def check(n):
    if n%2==0:
        print('even')
    else:
        print('odd')
n=5
check(n)

if __name__=='__main__':
    odd.run()