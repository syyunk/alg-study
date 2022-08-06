from xml.etree.ElementTree import iselement


class Stack :
    def __init__(self):                            # 생성자 
        self.top=[]

    def __str__(self):return str(self.top)          # stack객체 출력시 이 함수를 통해 자동으로 리스트객체로 변환해줌
                                #self.top[::-1]     역순 출력

    def isEmpty(self): return len(self.top)==0  # true or false를 출력
    def size(self): return len(self.top)
    def clear(self): self.top = []                 # 이제 전역변수 선언이 필요 없다. <- 왜?

    def push(self, item): self.top.append(item)
    def pop(self): 
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    



