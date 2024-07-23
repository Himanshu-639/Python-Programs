class Bank:
    def __init__(self,name, accountNum, type, amount):
        self.accountNum=accountNum
        self.name=name
        self.type=type
        self.amount=amount

    def deposit(self, depAmount):
        self.amount+=depAmount
        return self.amount
    def withdrawal(self, withdrawAmount):
        if withdrawAmount>self.amount:
            return 'Phle kama toh le BSDK'
        else:
            self.amount-=withdrawAmount
            return self.amount
    def findInterest(self):
        a=self.amount
        if a>=500000:
            return a*0.08
        elif a>=300000:
            return a*0.07
        elif a>=100000:
            return a*0.05
        else:
            return a*0.03
    def __str__(self):
         s='Name: '+self.name+'\n Acc No: '+str(self.accountNum)+'\n Type :'+self.type+'\n Amount: '+str(self.amount)+'\n Interest: '+self.findInterest()
         return s

a1 = Bank("Papa",1234567,"Savings",5500000)
