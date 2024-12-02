def somme(a,b) :
     result = a + b
     return result
def difference(a,b) :
     result = a - b
     return result
def rapport(a,b) :
     result = a / b
     return result
def produit(a,b) :
     result = a * b
     return result
ask_number_1 = int(input("entrez un nombre :"))
if ask_number_1 :
     print(ask_number_1)     
ask_signe = input("entrez un signe :")
LISTE = ["+","-","/","*"]              
learning =  True 
while  learning == True :
    if ask_signe == "+" :
        print("+")
        learning = False
    elif ask_signe == "-" :
         print("-")
         learning = False  
    elif ask_signe == "/" :
         print("/")
         learning = False  

    elif ask_signe == "*" :
         print("*")
         learning = False 
    elif not ask_signe or ask_signe != ("+" and "-" and "/" and "*"):
         ask_signe = input("entrez un signe :")
         learning = True
ask_number_2 = int(input("entrez un nombre :"))
if ask_number_2 :
     print(ask_number_2)   
ask_egale = input("resultat : ") 
learn = True
while learn == True :
     if not ask_egale or ask_egale != "=" :
          ask_egale = input("resultat : ")
          learn = True           
if ask_egale == "=" :                                                                
     if ask_signe == "+"  : 
          resultat = somme(ask_number_1,ask_number_2)
          print(resultat)   
     elif ask_signe == "-" :
          resultat = difference(ask_number_1,ask_number_2)    
          print(resultat)
     elif ask_signe == "*" :
          resultat = produit(ask_number_1,ask_number_2)    
          print(resultat)
     elif ask_signe == "/" :
          try :
               resultat = rapport(ask_number_1,ask_number_2) 
          except ZeroDivisionError :
               print("eureur division par 0")  
          print(resultat)                                