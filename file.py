from fire import Fire
from udb import udb

def main(meth,amt,res):
    db = udb.udb()
    db.load("utsaeb.udb")
    db.write(method=meth,amount=amt,desc=res)
    db.close()
    

    


if __name__ == "__main__":
    Fire(main)