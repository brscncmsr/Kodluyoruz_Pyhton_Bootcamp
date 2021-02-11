
import random


        
def wordchosser():
            global show,selection
            Words=["BARIS","SERKAN","HALIL","ELIF","CEREN","AYSENUR","OMER","ALI","SELAHATTIN","MUSTAFA","EYUP","MELIS","DILARA","BUSRA","MUZAFFER","OKKES","MEHMET","FERIDUN","CEMRE","ESRA","GOKCE","SILA","FATMA"]
            selection= random.choice(Words)
            show = ["_"] * len(selection)
            print("Lütfen Türkçe Karakter Girmeyiniz")
            print(show)
            
wordchosser()


        

def takeguess():
    
        while True:
            guess=input("Bir harf giriniz=")
            if len(guess) == 1 and guess.isalpha() and guess.upper() not in show:
                break
            else:
                print("Hatalı Giriş Yapıldı")
        return guess.upper()
        
        
    
    
def checkletter(letter):
            position=[]
            for index, l in enumerate(selection):
                if l == letter:
                    position.append(index)
            return position


def takeanswer():
                global life
                a=0
                while a==0:
                        print("Harfi doğru buldunuz")
                        print("Tahmin Yapmamak için herhangi bir tuşa basınız")
                        thought=input("Tahmin yapmak için . tuşuna basınız")
                        if thought==".":
                            a=1
                            print(a)
                        else:
                            break
                        while a==1:
                            answer=input("Tahmininizi giriniz :")
                            if answer.upper()==selection:
                                print("Tahmininiz Doğru")
                                again=input("Tekrar oynamak ister misiniz E/H")
                                if again.upper()=="E":
                                    a=2
                                elif again.upper()=="H":
                                    print("Gidiyor Gönlümün Efendisi")
                                    exit()
                                else:
                                    print("Hatalı Giriş")  


                            elif answer.upper() !=selection:
                                print("Hatalı Tahmin")
                                life-=1
                                break
                            else:
                                print("Hatalı Giriş")
                                continue
                        while a==2:
                            wordchosser()
                            gamemotor()
                            
                        




                    
def gamemotor():
            global show,life
            life=6
            
            while life > 0 and selection !="".join(show) :
                print("kelime: " + "".join(show))
                print(life)
                draw()
                letter=takeguess()
                positions=checkletter(letter)
                if positions:
                    for p in positions :
                        show[p]=(letter)
                        takeanswer()
                else:
                 life-=1
            if life<=0:
                print("Maalesef kaybettiniz")
                print("Kelime:",selection)
                draw()
                exit()
def draw():
        global life
        picture = ["""
         +---+
         |   |
             |
             |
             |
             |
      --------""","""
         +---+
         |   |
         O   |
             |
             |
             |
      --------""","""
         +---+
         |   |
         O   |
         |   |
             |
             |
      --------""","""
         +---+
         |   |
         O   |
        /|   |
             |
             |
      --------""","""
         +---+
         |   |
         O   |
        /|/  | 
             |
             |
      --------""","""
         +---+
         |   |
         O   |
        /|/  |
        /    |
             |
      --------""","""
         +---+
         |   |
         O   |
        /|/  |
        / /  |
             |
      --------"""]
        if life ==6:
          print(picture[0])
        elif life==5:
            print(picture[1])
        elif life==4:
            print(picture[2])
        elif life==3:
            print(picture[3])
        elif life==2:
            print(picture[4])
        elif life==1:
            print(picture[5])
        elif life==0:
            print(picture[6])


        
           
                            
                



gamemotor()





            

            
    



                
               


   


    

 