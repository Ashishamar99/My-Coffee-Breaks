# Trying to install required modules and importing them.
for ch in list(range(2)):
	try:
		import sys
		from tkinter import *
		import requests
		import json
	except ImportError:
		import os
		os.system('python -m pip install requests')

root = Tk()
root.title('Fetch User Information')
root.geometry('450x450+500+300')

my_label = Label(root, text = 'Enter Your Github username: ')
my_label.pack()

my_text_box = Entry(root, width = 50)
my_text_box.pack()

def fetch_github_id():
	display_information = []
	response = requests.get('https://api.github.com/users/' + my_text_box.get())
	my_github_api = json.loads(response.text)
	for key,value in my_github_api.items():
		display_information.append(f'{key}: {value}\n')
	my_result_label = Label(root, text = display_information)
	my_result_label.pack()


submit_button = Button(root, text = 'Get my info', command = fetch_github_id)
submit_button.pack()
root.mainloop()
