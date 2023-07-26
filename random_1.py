from flask import Flask 
random=Flask(__name__)

@random.route('/')
def find_random_val(n):
    num=1,2,3,45,55
    for i in n:
        if i in num:
            num+=i 
    return num 

if __name__=='__main__':
    random.run()