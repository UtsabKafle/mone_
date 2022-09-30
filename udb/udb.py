import os
from datetime import date
class udb:
    def __init__(self):
        pass
    def load(self,_name):
        try:
            self.db = open(_name,'a+')
        except FileNotFoundError:
            print(f"The {_name} file is not found.")
    def create(self,_name):
        self.db = open(_name,'w+')
        self.db.close()
    def delete(self,_name):
        try:
            os.remove(_name)
        except:
            pass
    def read(self):
        print("reading")
        with self.db as file:
            print(file.readline())
    def process_description(self,desc):
        d_list = desc.split("_")
        desc_ = ""
        for i in d_list:
            desc_ += i+" "
        return desc_

    def write(self,method,amount:int,desc:str):
        """

        :date-amount-description:

        date ->  date {obj}
        amount -> amount {float}
        description -> reason {str} :: will be seperated by _ instead of ' '.
                eg - used_money_to_buy_clothes

        {str} ->  will be written between two strings:
                eg - *hello world*

        
        """
        received = ['add','earned','plus','got','made']
        spent = ['spent','bought','gave','lended','sub','subtract','minus']
        today = date.today()
        if method in received:
            self.db.write(f":(r)-{str(date.today()).replace('-','_')}-{amount}*{self.process_description(desc)}*:")
        elif method in spent:
            self.db.write(f":(s)-{str(date.today()).replace('-','_')}-{amount}*{self.process_description(desc)}*:")
    def close(self):
        self.db.close()

    def save(self):
        pass



def main():
    db = udb()
    db.load("utsab.udb")
    # db.write(100,"working_in_the_farm")
    db.read()
if __name__ == "__main__":
    main()