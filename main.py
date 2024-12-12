import getpass
import os
import time
import pygame

from gtts import gTTS

from data import load_data_from_file
from users import register ,login,logout, view_users, DIRECTOR_PASSWORD
from logs import get_logs
from products import add_product, view_products, delete_product
from reports import generate_report
from transactions import view_transactions,create_transaction
from suppliers import add_supplier, view_suppliers
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


# text3 = "Hello, WELCOME TO Warehouse, please enter the required action:"
# audio = gTTS( text=text3, lang='en' )
# audio.save( "output.mp3" )

pygame.mixer.init()
# pygame.mixer.music.load( "output.mp3" )
# pygame.mixer.music.play()

d = 0
def play_voice_message(text):
    global d
    tts = gTTS( text=text, lang='en' )
    tts.save( f"Voices/selection_{d}.mp3" )
    pygame.mixer.music.load( f"Voices/selection_{d}.mp3" )
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick( 10 )
    d += 1

def clear_console():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system( command )

def back_to_menu():
    while True:
        back = int( input( "Enter 0 to back the menu: " ) )
        if back == 0:
            break

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
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  12. {Colors.SOFT_PINK} Log Out                                                          {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  0. {Colors.SOFT_PINK}  Exit                 🔚                                          {Colors.RESET}                           
{Colors.SOFT_PURPLE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}"""

#  "Log out"  faqat log in qilingan bo'lsa ko'rsatoladi
# if is_logged_in():
#     print( "4. Log out" )
def typing_animation(text, delay=0.004):
    for char in text:
        print( char, end='', flush=True )
        time.sleep( delay )
    print()


def show_menu():
    clear_console()
    print( menu )
    typing_animation( "Please select an option..." )


def main():
    play_voice_message("Hello, WELCOME TO Warehouse, please enter the required action:")
    def register_page():
        while True:
            clear_console()
            print( "\n=== Tizim ===" )
            print( "1. Ro'yxatdan o'tish" )
            print( "2. Log in" )
            print( "3. Foydalanuvchilarni ko'rish" )
            print( "0. Exit" )
            choice = input( "Tanlovingizni kiriting: " ).strip()

            if choice == "1":
                if register() == "Logining":
                    break
                time.sleep(2)

            elif choice == "2":
                # Log in the user
                l = login()
                if l == 'Login Successfully':
                    time.sleep(2)
                    break

            elif choice == "3":
                # Ask for a password to view user information if logged in
                special_password = getpass.getpass(
                    "Please enter the directors password to view users information: " ).strip()
                if special_password == DIRECTOR_PASSWORD:  # Replace 'your_password' with actual logic
                    print( "Displaying user information..." )
                    view_users()
                    while True:
                        back1 = int( input( "Enter 0 to back the menu: " ) )
                        if back1 == 0:
                            break

                else:
                    print( "Incorrect password." )
                    time.sleep(2)

            elif choice == "0":
                print( "Tizimdan chiqildi." )
                play_voice_message("You selected Exit")
                print("Exiting... Goodbye!")
                pygame.mixer.music.unload()
                for filename in os.listdir("Voices"):
                    file_path = os.path.join("Voices", filename)
                    if os.path.isfile(file_path):  # Check if it is a file
                        os.remove(file_path)
                return
            else:
                print( "Noto'g'ri tanlov. Qaytadan urinib ko'ring." )

    register_page()

    while True:
        show_menu()
        user_choice = input( f"{Colors.GOLD}{Colors.BG_GRAY} Enter your choice: {Colors.RESET}" ).strip()

        if user_choice == "1":
            play_voice_message( "You selected Add Transaction" )
            create_transaction()
            back_to_menu()

        elif user_choice == "2":
            play_voice_message( "You selected View Transactions" )
            view_transactions()
            back_to_menu()
        elif user_choice == "3":
            play_voice_message( "You selected Add Product" )
            add_product()
            back_to_menu()
        elif user_choice == "4":
            play_voice_message( "You selected View Products" )
            view_products()
            back_to_menu()

        elif user_choice == "5":
            play_voice_message( "You selected Delete Product" )
            delete_product()
            back_to_menu()
        elif user_choice == "6":
            play_voice_message( "You selected Add Supplier" )
            add_supplier()
            back_to_menu()
        elif user_choice == "7":
            play_voice_message( "You selected View Suppliers" )
            view_suppliers()
            back_to_menu()
        elif user_choice == "8":
            play_voice_message( "You selected Add Warehouse" )
            add_warehouse()
            back_to_menu()
        elif user_choice == "9":
            play_voice_message( "You selected View Warehouse Info" )
            for i in load_data_from_file( file_name="warehouses", param_key="all" ):
                print( f""" Warehouse id: {i['id']} 
                    Warehouse name: {i['name']}
                    Warehouse location: {i['location']}
                    Warehouse general capacity: {i['capacity']}
                    Warehouse current capacity: {i['current_capacity']}    
                """ )
            back_to_menu()
        elif user_choice == "10":
            play_voice_message( "You selected Create Report" )
            generate_report()
            back_to_menu()
        elif user_choice == "11":
            play_voice_message( "You selected View Logs" )
            get_logs()
            back_to_menu()

        elif user_choice == "12":
            play_voice_message("Goodbye")
            # Log out the user
            logout()
            register_page()
        elif user_choice == "0":
            play_voice_message( "You selected Exit" )
            print( "Exiting... Goodbye!" )
            pygame.mixer.music.unload()
            for filename in os.listdir( "Voices" ):
                file_path = os.path.join( "Voices", filename )
                if os.path.isfile( file_path ):  # Check if it is a file
                    os.remove( file_path )
            break
        else:
            play_voice_message( "Invalid option. Please try again." )
        time.sleep(2)


if __name__ == "__main__":
    main()
