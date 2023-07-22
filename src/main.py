import tkinter as tk
from configsReader import get_configs

def main():
    config = get_configs()

    window = tk.Tk()
    window.title('Microbuilder 0.1')
    window.geometry(config['res'])

    button = tk.Button(window, text='Build')
    button.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
