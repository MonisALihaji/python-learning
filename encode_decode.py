    
# encryption   and decryption program


alphabets="abcdefghijklmnopqrstuvwxyz"

def encode_decode():
    
    user_try_again = "yes"
    while user_try_again=="yes":
        
       
        userchoice=input("\n Type \"encode\" to encrypt , type \"decode\" to decrypt: ").lower()
        
        if userchoice not in ("encode","decode"):
            print("Enter valid input!⚠️")
            continue
            
        text=input("Type your text: ").lower()
        shift =int(input("Enter the shift number: "))
    
        if userchoice=="encode":
            encrypted_text=""
            
            for i in text:
                if  i in alphabets:
                    index=(alphabets.find(i)+shift)%26
                    encrypted_text+=alphabets[index]
                else:
                    encrypted_text +=i
            print(f"Your encoded text : {encrypted_text}")        
        
        
                
        elif  userchoice=="decode":
            
            decrypted_text=""
            for i in text:
                        if  i in alphabets:
                            index=(alphabets.find(i)-shift)%26
                            decrypted_text+=alphabets[index]
                        else:
                            decrypted_text +=i
            print(f"Your decoded text : {decrypted_text}") 
        
        user_try_again=input("Type \"yes\" if you want to go again. Otherwise type \"no\". ").strip().lower()
        
encode_decode()      


# instead of using two conditionals we can use only one above , but i used two so that it can be easy for beginners to understand the code.

# python programming ❤️