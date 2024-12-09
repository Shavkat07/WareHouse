from gtts import gTTS  # matnni nutq yaratish uchun
import pygame  # nutqi ijro etish uchun
import os
import time


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


text3 = "Hello, WELCOME TO Warehouse,through this list you will get general information about the goods. please enter the required action!!!:"
audio = gTTS(text=text3, lang='en')
audio.save("output.mp3")  # matnni nutqqa (gtts) va uni pygameda ijro etish uchun

pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()


def play_voice_message(tex3):  # Matnni ovoz orqali ijro etish
	ts1 = gTTS(text=tex3, lang='en')
	ts1.save("selection.mp3")
	pygame.mixer.music.load("selection.mp3")
	pygame.mixer.music.play()

	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)


def clear_console():
	command = 'cls' if os.name == 'nt' else 'clear'
	os.system(command)


menu = f"""
{Colors.BOLD}{Colors.SOFT_PURPLE}{Colors.UNDERLINE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}
{Colors.LIGHT_BLUE}{Colors.ORQA_qora}             🌿  Welcome to the Tranquil WAREHOUSE System  🌿            {Colors.RESET}
{Colors.SOFT_PURPLE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}
{Colors.ORQA_qora}🌟                                                                     🌟{Colors.RESET}
{Colors.ORQA_qora}🌟                                                                     🌟{Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora} {Colors.BOLD}   🍃  Please choose from the options below:  🍃                        {Colors.RESET}
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  1  {Colors.SOFT_PINK} Inventory Management   📦                                         {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  2  {Colors.SOFT_PINK} Order Processing       🛒                                         {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  3  {Colors.SOFT_PINK} Warehouse Locations    🗺️                                         {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  4  {Colors.SOFT_PINK} Reports                📝                                         {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  5  {Colors.SOFT_PINK} User Management        👥                                         {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  6  {Colors.SOFT_PINK} Receiving Goods        🚚                                         {Colors.RESET}                           
{Colors.SOFT_GREEN}{Colors.ORQA_qora}  7  {Colors.SOFT_PINK} Exit                   🔚                                         {Colors.RESET}                           
{Colors.ORQA_qora}🌟                                                                     🌟{Colors.RESET}
{Colors.ORQA_qora}🌟                                                                     🌟{Colors.RESET}
{Colors.SOFT_PURPLE}═════════════════════════════════════════════════════════════════════════{Colors.RESET}"""


def typing_animatsiya(text4, delay=0.004):
	for char in text4:
		print(char, end='', flush=True)
		time.sleep(delay)
	print()


def show_menu():
	clear_console()
	typing_animatsiya(menu)


def main():
	while True:
		show_menu()
		user_choice = input(f"{Colors.GOLD}{Colors.BG_GRAY} Enter your choice: {Colors.RESET}").strip()
		if user_choice in ["1", "2", "3", "4", "5", "6", "7"]:
			play_voice_message(f"You selected {user_choice}")
			while pygame.mixer.music.get_busy():
				pygame.time.Clock().tick(15)
		else:
			play_voice_message(f"You selected an invalid option")
			while pygame.mixer.music.get_busy():
				pygame.time.Clock().tick(15)
		if user_choice == "1":
			input(f"{Colors.SOFT_GREEN} Inventory Management: {Colors.RESET}")


if __name__ == "__main__":
	main()