# 4장 파이썬의 입출력 되새김 문제
## 1. 홀수, 짝수 판별하기
#def is_odd(number):
#    if number % 2 == 1 :
#        return True
#    else:
#        return False

#print(is_odd(10))
#print(is_odd(3))


## 2. 모든 입력의 평균값 구하기
#def avg_number(*args):   
#    result = 0
#    for i in args:
#        result += i
#    return result / len(args)

#print(avg_number(1,2))
#print(avg_number(1,2,3,4,5))

## 3. 프로그램 오류 수정하기1
#input1 = input("첫번째 숫자를 입력하세요:")
#input2 = input("두번째 숫자를 입력하세요:")

#total = input1 + input2
#print("두 수의 합은 %s입니다" % total)

### 수정부분
#input1 = input("첫번째 숫자를 입력하세요:")
#input2 = input("두번째 숫자를 입력하세요:")

#total = int(input1) + int(input2)
#print("두 수의 합은 %s입니다" % total)


## 4. 출력 결과가 다른 것은?
#print("you" "need" "python")
#print("you" + "need" + "python")
#print("you", "need", "python")   ## 쉼표가 있으면 공백이 포함된다!
#print("".join(["you","need","python"]))

## 5. 프로그램 오류 수정하기2
f1 = open("test.txt", 'w')
f1.write("Life is too short")

f2 = open("test.txt", 'r')
print(f2.read())

## 6. 사용자 입력 저장하기
#user_input = input("저장할 내용을 입력하세요:")
#f = open('test.txt', 'a')
#f.write(user_input)
#f.write("\n")
#f.close()


## 7. 파일의 문자열 바꾸기
#f1 = open('test7.txt', 'w')
#f1.write("Life is too short\n you need java\n") 

#f1 = open('test7.txt', 'r')
#body = f1.read()
#f1.close()

#body = body.replace('java','python')

#f1 = open('test7.txt', 'w')
#f1.write(body)
#f1.close()


## 8. 입력값을 모두 더해 출력하기
#C:\> cd doit
#C:\doit > python myargv.py 1 2 3 4 5 6 7 8 9 10

### 정답은 아래와 같이 나와있음
#import sys

#numbers = sys.args[1:]

#result = 0 
#for number in numbers:
#    result += int(number)
#print(result)