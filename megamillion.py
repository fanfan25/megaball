"""
program: megamillion.py
Author: Jude 11/19/2021

***Note: the file breezypythongui.py Must be in the same directory as this file for the application to work.
***
This app require pillow install to be able to work
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
from tkinter import PhotoImage
from PIL import ImageTk, Image
import random

class MegaMillion(EasyFrame):
	""" Displays multiple labels in a window."""

	def __init__(self):
		"""Sets up the window and the label."""
		EasyFrame.__init__(self, "Mega Million", width = 400, height =480,background = "#6495ED",  resizable = False)
		# now the window is established, add componens to that window 
		imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
		# Load the image and associate with the image label
		self.image = PhotoImage(file = "log.png")
		imageLabel["image"] = self.image 


		self.titleLabel = self.addLabel(text = "BE RICH IN A SECOND!", row = 1, column = 0, background = "#6495ED", columnspan = 3, foreground = "yellow", font = Font(family = "Impact", size = 28), sticky = "NSEW")
		self.titleLabel["underline"] = 0

		# Fields for the random numbers to appear
		self.numField1 = self.addIntegerField(value = 0, row = 2, column = 0, state = "readonly", sticky = "SNE")
		self.numField2 = self.addIntegerField(value = 0, row = 3, column = 0,state = "readonly", sticky = "SNE")
		self.numField3 = self.addIntegerField(value = 0, row = 4, column = 0, state = "readonly", sticky = "SNE")
		self.numField4 = self.addIntegerField(value = 0, row = 5, column = 0, state = "readonly", sticky = "SNE")
		self.numField5 = self.addIntegerField(value = 0, row = 6, column = 0, state = "readonly", sticky = "SNE")
		#Megaball field
		self.numField6 = self.addLabel(text = "0", row = 7, column = 0,  background = "yellow", sticky = "SNE")
		self.textMessage = self.addLabel(text = "Mega Ball", row = 7, column = 0, columnspan =2, background = "#6495ED")
		self.textMessage["anchor"] = "center"
		self.textMessage["height"] = 3
		self.textMessage["width"] = 20

		self.numField6["anchor"] = "center"
		self.numField6["height"] = 3
		self.numField6["width"] = 8

		# command button
		self.lotoButton = self.addButton(text = "Play to win!", row = 8, column = 0, columnspan = 3, command = self.play)
		self.lotoButton["background"] = "red"
		self.lotoButton["foreground"] = "white"
		self.lotoButton["font"] = ("Arial", 10, "bold")
		self.lotoButton["padx"] = 15
		self.lotoButton["pady"] = 20 

		#Label foroutput message
		self.outputLabel = self.addLabel(text = "", row = 9, column = 0, columnspan = 2, background = "#6495ED", sticky = "NSEW", foreground = "white", font = Font(family = "Georgia", size = 18))

	def play(self):
		# variables and constants
		num1 = random.randint(1, 70)
		num2 = random.randint(1, 70)
		num3 = random.randint(1, 70)
		num4 = random.randint(1, 70)
		num5 = random.randint(1, 70)
		num6 = random.randint(1, 25)

		#output phase
		self.numField1.setNumber(num1)
		self.numField2.setNumber(num2)
		self.numField3.setNumber(num3)
		self.numField4.setNumber(num4)
		self.numField5.setNumber(num5)
		self.numField6["text"] = num6
	

# definition of the main() function for program entry
def main():
	"""Instantiation and pops up the window."""
	MegaMillion().mainloop()

# global call to trigger the main() function
if __name__ == "__main__":
	main()

