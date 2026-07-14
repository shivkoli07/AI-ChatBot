"""
=========================================================
Rule-Based AI Chatbot
---------------------------------------------------------
Author      : Shiv Koli
Internship  : DecodeLabs
Version     : 1.0
=========================================================
"""

import tkinter as tk
from gui import ChatbotGUI


def main():

    root = tk.Tk()

    app = ChatbotGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()