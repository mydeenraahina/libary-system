from datetime import date,timedelta,datetime
def menu():
    print("WELCOME to our LIBARY!!")
    
    today=datetime.now()
    
    day_of_week = today.strftime("%A")
    
    print("DATE :",datetime.today())
    
    print(f"DAY :{day_of_week}")
    
    menu_listed=["MENU","1.UPDATING NEW ARRAIVAL","2.checking_availability_OF BOOK",
                 "3.borrow_book",
                 "4.display available books"]
    print("----FINE AMOUNT SHOULD BE COLLECTED IF DUE DATE EXIT----")
    
    for attempt in menu_listed:
        print(attempt)
        
menu()
list_value=()
class libary_system:
    def new_arraival(self,*args):
        global list_value
        list_value+=(args)
        print(list_value)
            
    def checking_availability(self,expected_book):
        if expected_book in list_value :
            print(f"{expected_book} is still available")
        else:
            print(f"sorry!\n {expected_book} is no available")
    
            
    def borrow_book(self):
        while True:
            book_name=input(f"Enter your needed_book name :")
            if book_name.isalpha():
                current_date=date.today()
                last_date_of_submission=date.today()+timedelta(days=10)
                print(f"last date of your book {[book_name]} submision ={last_date_of_submission}")
                break
            else:
                print(f"Enter a valid input")

    def display_all_available_books(self):
        if not list_value:
            print("Book list is empty!!!")
        else:
            print("Available books:")
            for i in list_value :
                print(i)
class main_block:
    def __init__(self):
        while True:        
            getting_input=input(f"Enter your choice :")
                        
            if getting_input=="1":
                while True:
                    try:
                        no_of_new_arraival=int(input(f"Enter how many books are arrived :"))
                        newy_arraival=[]
                        break
                    except ValueError:
                        print("enter a valid input")
                                
                for i in range(1,no_of_new_arraival+1):
                    getting_books_arrived=input("Enter the name of newly arrived book")
                    if getting_books_arrived.isalpha():
                        newy_arraival.append(getting_books_arrived)
                    else:
                        print(f"Enter a valid input")
                print(f"New arraivals updated successfully")
                                        
                                
                value=",".join(newy_arraival)
                obj=libary_system()
                obj.new_arraival(value)
                break
                                
            elif getting_input=="2":
                availability_of_book=input(f"Enter book name to check availability")
                obj1=libary_system()
                obj1.checking_availability(availability_of_book)
                break
                        
            elif getting_input=="3":
                obj3=libary_system()
                obj3.borrow_book()
                break
                        
            elif getting_input=="4":
                obj4=libary_system()
                obj4.display_all_available_books()
                break
                        
            else:
                print(f"Enter a valid input")
object=main_block()
while True:
    getting_input_for_continue=input("Do you want to continue process [yes\\no] ")
    if getting_input_for_continue.casefold()=="yes":
        object1=main_block()
        break
    elif getting_input_for_continue.casefold()=="no":
        print("Exit!")
        break
    else:
        print("Enter a valid input")
        


                

