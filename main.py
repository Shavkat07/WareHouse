import os
import time
import pygame

from gtts import gTTS

from data import load_data_from_file
from users import register ,login,logout
from logs import get_logs,save_log
from products import add_product, view_products, delete_product
from reports import generate_report
from transactions import view_transactions,create_transaction , delete_transaction , check_product_availability
from suppliers import add_supplier, view_suppliers, delete_supplier
from warehouses import add_warehouse # view_warehouses  # Add warehouse functions

class Colors:
    SOFT_PURPLE = '\033[38;5;147m'
    LIGHT_BLUE = '\033[38;5;117m'
    SOFT_PINK = '\033[38;5;175m'
    SOFT_GREEN = '\033[38;5;151m'
    GOLD = '\033[38;5;220m'
    LIGHT_GRAY = '\033[38;5;248m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BG_GRAY = '\033[48;5;235m'
    BG_SOFT_BLUE = '\033[48;5;110m'
    BG_PINK = '\033[48;5;175m'
    ORQA_qora = '\033[40m'


text3 = "Hello, WELCOME TO Warehouse, please enter the required action:"
audio = gTTS( text=text3, lang='en' )
audio.save( "output.mp3" )

pygame.mixer.init()
pygame.mixer.music.load( "output.mp3" )
pygame.mixer.music.play()


def play_voice_message(text):
    tts = gTTS( text=text, lang='en' )
    tts.save( "selection.mp3" )
    pygame.mixer.music.load( "selection.mp3" )
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick( 10 )


def clear_console():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system( command )


menu = f"""
{Colors.BOLD}{Colors.SOFT_PURPLE}{Colors.UNDERLINE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}
{Colors.LIGHT_BLUE}{Colors.ORQA_qora}             🌿  Welcome to the Tranquil WAREHOUSE System  🌿            {Colors.RESET}
{Colors.SOFT_PURPLE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}
{Colors.ORQA_qora}🌟                                                                    🌟{Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora} {Colors.BOLD}   🍃  Please choose from the options below:  🍃                       {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  1.  {Colors.SOFT_PINK} Add Transaction      💳                                          {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  2.  {Colors.SOFT_PINK} View Transactions    📜                                          {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  3.  {Colors.SOFT_PINK} Add Product          📦                                          {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  4.  {Colors.SOFT_PINK} View Products        📝                                          {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  5.  {Colors.SOFT_PINK} Delete Product       🗑️                                          {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  6.  {Colors.SOFT_PINK} Add Supplier         🚚                                          {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  7.  {Colors.SOFT_PINK} View Suppliers       🛒                                          {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  8.  {Colors.SOFT_PINK} Add Warehouse        🏠                                          {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  9.  {Colors.SOFT_PINK} View Warehouse Info  📜                                          {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  10. {Colors.SOFT_PINK} Create Report        📊                                          {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  11. {Colors.SOFT_PINK} View Logs            🗂️                                          {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  12. {Colors.SOFT_PINK} Exit                 🔚                                          {Colors.RESET}                           
{Colors.SOFT_PURPLE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}"""


def typing_animation(text, delay=0.004):
    for char in text:
        print( char, end='', flush=True )
        time.sleep( delay )
    print()


def show_menu():
    clear_console()
    print( menu )
    typing_animation( "Please select an option..." )


is_logged_in = False


def main():
    global is_logged_in

    while True:
        print( "\n=== Tizim ===" )
        print( "1. Ro'yxatdan o'tish" )
        print( "2. Foydalanuvchilarni ko'rish" )
        print( "3. Log in" )

        #  "Log out"  faqat log in qilingan bo'lsa ko'rsatoladi
        if is_logged_in:
            print( "4. Log out" )

        print( "5. Exit" )
        choice = input( "Tanlovingizni kiriting: " ).strip()

        if choice == "1":
            register()

        elif choice == "2":
            # Ask for a password to view user information if logged in
            if is_logged_in:
                special_password = input( "Please enter the special password to view user information: " ).strip()
                if special_password == "your_password":  # Replace 'your_password' with actual logic
                    print( "Displaying user information..." )
                    # Logic to display user info
                else:
                    print( "Incorrect password." )
            else:
                print( "Please log in first." )

        elif choice == "3":
            # Log in the user
            login()
            is_logged_in = True  # Assume login is successful

        elif choice == "4" and is_logged_in:
            # Log out the user
            logout()
            is_logged_in = False

        elif choice == "5":
            print( "Tizimdan chiqildi." )
            break
        else:
            print( "Noto'g'ri tanlov. Qaytadan urinib ko'ring." )

    while True:
        show_menu()
        user_choice = input( f"{Colors.GOLD}{Colors.BG_GRAY} Enter your choice: {Colors.RESET}" ).strip()

        if user_choice == "1":
            play_voice_message( "You selected Add Transaction" )
            create_transaction()
        elif user_choice == "2":
            play_voice_message( "You selected View Transactions" )
            view_transactions()
        elif user_choice == "3":
            play_voice_message( "You selected Add Product" )
            add_product()
        elif user_choice == "4":
            play_voice_message( "You selected View Products" )
            view_products()
        elif user_choice == "5":
            play_voice_message( "You selected Delete Product" )
            delete_product()
        elif user_choice == "6":
            play_voice_message( "You selected Add Supplier" )
            add_supplier()
        elif user_choice == "7":
            play_voice_message( "You selected View Suppliers" )
            view_suppliers()
        elif user_choice == "8":
            play_voice_message( "You selected Add Warehouse" )
            add_warehouse()
        elif user_choice == "9":
            play_voice_message( "You selected View Warehouse Info" )
            for i in load_data_from_file( file_name="warehouses", param_key="all" ):
                print( f""" Warehouse id: {i['id']} 
                    Warehouse name: {i['name']}
                    Warehouse location: {i['location']}
                    Warehouse general capacity: {i['capacity']}
                    Warehouse current capacity: {i['current_capacity']}    
                """ )
        elif user_choice == "10":
            play_voice_message( "You selected Create Report" )
            generate_report()
        elif user_choice == "11":
            play_voice_message( "You selected View Logs" )
            get_logs()
        elif user_choice == "12":
            play_voice_message( "You selected Exit" )
            print( "Exiting... Goodbye!" )
            break
        else:
            play_voice_message( "Invalid option. Please try again." )
        time.sleep( 1 )


if __name__ == "__main__":
    main()