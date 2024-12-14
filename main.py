import getpass
import os
import time
import pygame
import threading


from gtts import gTTS

from data import load_data_from_file
from users import register, login, logout, view_users, DIRECTOR_PASSWORD
from logs import get_logs
from products import add_product, view_products, delete_product
from reports import generate_report
from transactions import view_transactions, create_transaction, generate_transaction_chart
from suppliers import add_supplier, view_suppliers
from warehouses import add_warehouse

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

pygame.mixer.init()

d = 0


def play_voice_message(text):
    global d
    tts = gTTS(text=text, lang='en')
    filename = f"Media/Voices/selection_{d}.mp3"
    tts.save(filename)

    # Создаем отдельный поток для воспроизведения звука
    threading.Thread(target=play_audio, args=(filename,)).start()
    d += 1

def play_audio(filename):
    pygame.mixer.init()  # Инициализация pygame mixer
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def clear_console():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def back_to_menu():
    while True:
        back = int(input("Enter 0 to back to the menu: "))
        if back == 0:
            break

def delete_voice_files():
    for filename in os.listdir("Media/Voices"):
        file_path = os.path.join("Media/Voices", filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

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
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  5.  {Colors.SOFT_PINK} Delete Product       🗑️                                         {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  6.  {Colors.SOFT_PINK} Add Supplier         🚚                                          {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  7.  {Colors.SOFT_PINK} View Suppliers       🛒                                          {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  8.  {Colors.SOFT_PINK} Add Warehouse        🏠                                          {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  9.  {Colors.SOFT_PINK} View Warehouse Info  📜                                          {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  10. {Colors.SOFT_PINK} Create Report        📊                                          {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  11. {Colors.SOFT_PINK} View Logs            🗂️                                         {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  12. {Colors.SOFT_PINK} Log Out                                                          {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  13. {Colors.SOFT_PINK} View Diagram                                                     {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  0. {Colors.SOFT_PINK}  Exit                 🔚                                          {Colors.RESET}                           
{Colors.SOFT_PURPLE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}"""

def typing_animation(text, delay=0.004):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_menu():
    clear_console()
    print(menu)
    typing_animation("Please select an option...")

def main():
    play_voice_message("Hello, WELCOME TO Warehouse, please enter the required action:")

    def register_page():
        while True:
            clear_console()
            print(f"{Colors.BOLD}{Colors.SOFT_PURPLE}{Colors.UNDERLINE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}")
            print(f"{Colors.LIGHT_BLUE}{Colors.ORQA_qora}            🌿  Welcome to the Registration System  🌿                   {Colors.RESET}")
            print(f"{Colors.SOFT_PURPLE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}")
            print(f"{Colors.ORQA_qora}🌟                                                                     🌟{Colors.RESET}")
            print(f"{Colors.SOFT_GREEN}{Colors.ORQA_qora} {Colors.BOLD}   🍃  Please choose from the options below:  🍃                        {Colors.RESET}")
            print(f"{Colors.SOFT_GREEN}{Colors.ORQA_qora}  1.  {Colors.SOFT_PINK} Register              📝                                          {Colors.RESET}")
            print(f"{Colors.SOFT_GREEN}{Colors.ORQA_qora}  2.  {Colors.SOFT_PINK} Log In                🔑                                          {Colors.RESET}")
            print(f"{Colors.SOFT_GREEN}{Colors.ORQA_qora}  3.  {Colors.SOFT_PINK} View Users            📜                                          {Colors.RESET}")
            print(f"{Colors.SOFT_GREEN}{Colors.ORQA_qora}  0.  {Colors.SOFT_PINK} Exit                  🔚                                          {Colors.RESET}")
            print(f"{Colors.SOFT_PURPLE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}")

            choice = input(f"{Colors.GOLD}{Colors.BG_GRAY} Enter your choice: {Colors.RESET}").strip()

            if choice == "1":
                if register() == "Logining":
                    break
                time.sleep(2)

            elif choice == "2":
                l = login()
                if l == 'Login Successfully':
                    time.sleep(2)
                    break
                else:
                    time.sleep(2)

            elif choice == "3":
                special_password = getpass.getpass("Please enter the director's password to view users information: ").strip()
                if special_password == DIRECTOR_PASSWORD:
                    print("Displaying user information...")
                    view_users()
                    while True:
                        back1 = int(input("Enter 0 to back to the menu: "))
                        if back1 == 0:
                            break
                else:
                    print("Incorrect password.")
                    time.sleep(2)

            elif choice == "0":
                print("Tizimdan chiqildi.")
                play_voice_message("You selected Exit")
                print("Exiting... Goodbye!")
                pygame.mixer.music.unload()
                delete_voice_files()
                return "Exit"
            else:
                print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")

    if register_page() != "Exit":
        while True:
            show_menu()
            user_choice = input(f"{Colors.GOLD}{Colors.BG_GRAY} Enter your choice: {Colors.RESET}").strip()

            if user_choice == "1":
                play_voice_message("You selected Add Transaction")
                create_transaction()
                back_to_menu()

            elif user_choice == "2":
                play_voice_message("You selected View Transactions")
                view_transactions()
                back_to_menu()

            elif user_choice == "3":
                play_voice_message("You selected Add Product")
                add_product()
                back_to_menu()

            elif user_choice == "4":
                play_voice_message("You selected View Products")
                view_products()
                back_to_menu()

            elif user_choice == "5":
                play_voice_message("You selected Delete Product")
                delete_product()
                back_to_menu()

            elif user_choice == "6":
                play_voice_message("You selected Add Supplier")
                add_supplier()
                back_to_menu()

            elif user_choice == "7":
                play_voice_message("You selected View Suppliers")
                view_suppliers()
                back_to_menu()

            elif user_choice == "8":
                play_voice_message("You selected Add Warehouse")
                add_warehouse()
                back_to_menu()

            elif user_choice == "9":
                play_voice_message("You selected View Warehouse Info")
                for i in load_data_from_file(file_name="warehouses", param_key="all"):
                    print(f""" Warehouse id: {i['id']} 
                        Warehouse name: {i['name']}
                        Warehouse location: {i['location']}
                        Warehouse general capacity: {i['capacity']}
                        Warehouse current capacity: {i['current_capacity']}    
                    """)
                back_to_menu()

            elif user_choice == "10":
                play_voice_message("You selected Create Report")
                generate_report("hisobot.pdf")
                back_to_menu()

            elif user_choice == "11":
                play_voice_message("You selected View Logs")
                get_logs()
                back_to_menu()

            elif user_choice == "12":
                play_voice_message("Goodbye")
                logout()
                register_page()
            elif user_choice == "13":
                play_voice_message("You selected view diagram")
                display_menu()

            elif user_choice == "0":
                play_voice_message("You selected Exit")
                print("Exiting... Goodbye!")
                pygame.mixer.music.unload()
                delete_voice_files()
                break

            else:
                print("Invalid option, try again.")

def display_menu():
    while True:
        print("\nMenu:")
        print("33. Generate export transactions chart")
        print("77. Generate import transactions chart")
        print("55. Exit")
        user_input = input("Please select an option: ").strip()
        if user_input == "33":
            generate_transaction_chart( 'export' )
        elif user_input == "77":
            generate_transaction_chart( 'import' )
        elif user_input == "55":
            break

if __name__ == "__main__":
    main()