import schedule
import time


import pyautogui
pyautogui.PAUSE = 1

# Variables definition


def job_that_executes_once(input_msg):
    # We send the message with pyautogui.
    pyautogui.write(input_msg)

    pyautogui.press('enter')

    return schedule.CancelJob


def main():

	time_selected = input('Please, introduce in the following format the hour in which you want to schedule the message: "HH:MM": ')
	message_selected = input('Now, introduce the message you want to send: ')
	schedule.every().day.at(time_selected).do(job_that_executes_once, input_msg=message_selected)

	while True:
		schedule.run_pending()
		time.sleep(1)


if __name__ == '__main__':
	main()
