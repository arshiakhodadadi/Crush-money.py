def calculate_coins(amount):  
    
    ten_toman = amount // 10  
    amount %= 10   

    two_toman = amount // 2  
    amount %= 2  

    one_toman = amount   

    return ten_toman, two_toman, one_toman  

def main():  
    # دریافت ورودی از کاربر  
    money = input("")  
    
    try:  
        money = int(money)  
        if money < 0:  
            print("")  
            return  
    except ValueError:  
        print("")  
        return  


    ten_toman, two_toman, one_toman = calculate_coins(money)  

 
    result = []  
    
    if ten_toman > 0:  
        result.append(f"{ten_toman} 10")  
    if two_toman > 0:  
        result.append(f"{two_toman} 2")  
    if one_toman > 0:  
        result.append(f"{one_toman} 1")  


    if result:  
        print("،".join(result))  

main()  