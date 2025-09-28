import pprint
class A:
    def ad(self,value1,value2):
        self.x = value1
        self.y = value2
    def send_sum(self,num1,num2):
        print(num1 + num2)
a = A()
pprint.pprint(a.__dict__)
a.ad('Hello','world!')
pprint.pprint(a.__dict__)   
a.send_sum(5,4)
    
