import random

word_amount = ["car","hangman", "planet", "jorney", "family", "cloud"]
main_word = random.choice(word_amount)
miss_w = []
guessed = False
attemps = 10
word_completion = "_" * len(main_word)

def image_stages(attemps):
    stages = [ """
    
     ____________
    | /       |
    |/        O 
    |       / | | 
    |        / |
    |        
    _______________
    """,
    """
    ____________
    | /       |
    |/        O 
    |       / | | 
    |        / 
    |        
    _______________
    """,
    """
    
    ____________
    | /       |
    |/        O 
    |       / | | 
    |        
    |        
    _______________
    """,
      """
    
    ____________
    | /       |
    |/        O 
    |       / |  
    |        
    |        
    _______________
    """,
    """
    
    ____________
    | /       |
    |/        O 
    |         |  
    |        
    |        
    _______________
    """,
    """
    
    ____________
    | /       |
    |/        O 
    |       
    |        
    |        
    _______________
    """,
    """
    
    ____________
    | /       |
    |/       
    |      
    |       
    |        
    _______________
    """,
    """
    ____________
    | /    
    |/      
    |      
    |        
    |        
    _______________
    """,
    """
    ____________
    | 
    |  
    |  
    | 
    |        
    _______________
    """,
    """
    
    |    
    |    
    |      
    |        
    |        
    _______________
    """
    
    ]
    return stages[attemps]
    

print("let's start it now")


while not guessed and attemps > 0: 
    answer = input("try a letter:  ").upper()
    if len(answer) == 1:    
        if answer in miss_w:
            print("You tried this", answer)
        elif answer not in main_word:
            print(answer, " not in the word")    
            attemps -= 1
            miss_w.append(answer)
        else:
            print("right answer", answer , "is in the word")
            miss_w.append(answer)    
            list_word = list(word_completion)
            indices = [i for i, letter in enumerate(main_word) if letter == answer]
            for index in indices:
                list_word[index] = answer
            word_completion = "".join(list_word)    
            if "_" not in word_completion:
                guessed = True 
    else:
        print("error")        
    print(image_stages(attemps))
    print(word_completion)    
    print("\n")    
if guessed:
    print("victory")
else: 
    ("try again, the word was", main_word )        

