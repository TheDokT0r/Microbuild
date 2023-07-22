import tkinter as tk
from configs.settings import get_settings
from actions.builder import build


def main():
    config = get_settings()

    window = tk.Tk()
    window.title('Microbuilder 0.1')
    window.geometry(config['res'])

    button = tk.Button(window, text='Build', command=build)
    button.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
