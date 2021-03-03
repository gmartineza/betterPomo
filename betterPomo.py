import time
from plyer import notification
import os

clear=lambda: os.system("cls")

def main():
	start = time.time()
	input("Enter to stop work period, Ctrl+C to exit.\n")
	end = time.time()
	rest = round((end-start)/4)
	print("Starting resting period...")
	time.sleep(rest)
	notification.notify(
	title="Temporizador",
	message="Se terminó el tiempo.",
	app_icon=None,
	timeout=5,
	)
	time.sleep(1)
	clear()

while True:
	try:
		main()
	except KeyboardInterrupt:
		exit()