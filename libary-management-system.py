from datetime import date,timedelta,datetime
def menu():
    print("WELCOME to our LIBARY!!")
    
    today=datetime.now()
    
    day_of_week = today.strftime("%A")
    
    print("DATE :",datetime.today())
    
    print(f"DAY :{day_of_week}")
    
    menu_listed=["MENU","1.UPDATING NEW ARRAIVAL","2.checking_availability_OF BOOK",
                 "3.counting_targeted_book_avalability",
                 "4.borrow_book",
                 "5.display available books"]
    print("----FINE AMOUNT SHOULD BE COLLECTED IF DUE DATE EXIT----")
    
    for attempt in menu_listed:
        print(attempt)
        
menu()

class libary_system:
    @staticmethod
    def main_block():
        def new_arraival(*args):
            list_value.extend(args)
            
        def checking_availability(expected_book):
            if expected_book in list :
                print(f"{expected_book} is still available")
            else:
                print(f"sorry!\n {expected_book} is no available")
                
        def counting_targeted_book_avalability(target_book):
            print(f"total_availability_of_book_in_no: {list.count(target_book)}")
            
        def borrow_book():
            while True:
                book_name=input(f"Enter your needed_book name :")
                if book_name.isalpha():
                    current_date=date.today()
                    last_date_of_submission=date.today()+timedelta(days=10)
                    print(f"last date of your book {[book_name]} submision ={last_date_of_submission}")
                    break
                else:
                    print(f"Enter a valid input")

        def display_all_available_books():
            for i in list_value :
                print(i)
        list_value=[]
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
                        print(f"New arraivals updated successfully")
                    else:
                        print(f"Enter a valid input")
                                
                        
                value=",".join(newy_arraival)
                new_arraival(value)
                break
                        
            elif getting_input=="2":
                availability_of_book=input(f"Enter book name to check availability")
                checking_availability(availability_of_book)
                break
                
            elif getting_input=="3":
                target_book=input(f"Enter the book to count the availability :")
                counting_targeted_book_avalability(target_book)
                break
                
            elif getting_input=="4":
                borrow_book()
                break
                
            elif getting_input=="5":
                display_all_available_books()
                break
                
            else:
                print(f"Enter a valid input")
            
libary_system.main_block()


    
