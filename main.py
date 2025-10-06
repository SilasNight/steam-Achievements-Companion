import tkinter as tk

class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Achievement Hunter")

        #--Initialize--
        #Canvas
        self.canvas_controls = tk.Canvas(self.window,)

        #String
        self.selected_game = ""
        self.steam_api_key = ""
        self.steam_user_id = ""

        #Lists
        self.game_name_api = []

        #Entry
        self.api_key_entry = tk.Entry(self.canvas_controls)
        self.steam_id_entry = tk.Entry(self.canvas_controls)

        #Labels
        self.api_key_label = tk.Label(self.canvas_controls,text="Api Key(Sensitive)")
        self.steam_id_label = tk.Label(self.canvas_controls,text="Steam ID(Sensitive)")

        #Buttons
        self.button_games_load = tk.Button(self.canvas_controls,text="Load Games",command=self.todo_button)
        self.button_games_previous = tk.Button(self.canvas_controls,text="Prev",command=self.todo_button)
        self.button_games_Next = tk.Button(self.canvas_controls,text="Next",command=self.todo_button)
        self.button_games_refresh = tk.Button(self.canvas_controls,text="Refresh",command=self.todo_button)
        self.button_achievements_previous = tk.Button(self.canvas_controls,text="Prev",command=self.todo_button)
        self.button_achievements_next = tk.Button(self.canvas_controls,text="Next",command=self.todo_button)
        self.button_achievements_ref = tk.Button(self.canvas_controls,text="Refresh",command=self.todo_button)
        self.button_sensitive_load = tk.Button(self.canvas_controls,text="Load Sensitive",command=self.todo_button)
        self.button_sensitive_save = tk.Button(self.canvas_controls,text="Save Sensitive",command=self.todo_button)

        #--Placement--

        self.window.mainloop()

    def todo_button(self):
        pass

Main()