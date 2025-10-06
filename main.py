import tkinter as tk
import requests
import json


class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Achievement Hunter")

        #--Initialize--
        #Canvas
        self.canvas_controls = tk.Canvas(self.window,)

        #Constant String
        self.filename_name_ids = "data/Names, ID's.txt"
        self.filename_sensitive = "data/Sensitive.txt"

        #String
        self.selected_game = ""
        self.steam_api_key = ""
        self.steam_user_id = ""

        #Lists
        self.game_name_id = []

        #Entry
        self.api_key_entry = tk.Entry(self.canvas_controls)
        self.steam_id_entry = tk.Entry(self.canvas_controls)

        #Labels
        self.api_key_label = tk.Label(self.canvas_controls,text="Api Key(Sensitive)")
        self.steam_id_label = tk.Label(self.canvas_controls,text="Steam ID(Sensitive)")
        self.achievement_load = tk.Label(self.canvas_controls,text="Load Achievements")
        self.loading_label = tk.Label(self.window,text="Game",width = 100,relief="solid")

        #Buttons
        self.button_games_load = tk.Button(self.canvas_controls,text="Load Games",command=self.load_games)
        self.button_games_previous = tk.Button(self.canvas_controls,text="Prev",command=self.todo_button)
        self.button_games_next = tk.Button(self.canvas_controls,text="Next",command=self.todo_button)
        self.button_games_refresh = tk.Button(self.canvas_controls,text="Refresh",command=self.refresh_games)
        self.button_achievements_previous = tk.Button(self.canvas_controls,text="Prev",command=self.todo_button)
        self.button_achievements_next = tk.Button(self.canvas_controls,text="Next",command=self.todo_button)
        self.button_achievements_refresh = tk.Button(self.canvas_controls,text="Refresh",command=self.todo_button)
        self.button_sensitive_load = tk.Button(self.canvas_controls,text="Load Sensitive",command=self.load_sensitive)
        self.button_sensitive_save = tk.Button(self.canvas_controls,text="Save Sensitive",command=self.save_sensitive)

        #--Placement--
        #control canvas
        self.api_key_label.grid(row=0,column=0,sticky="w",columnspan=3)
        self.api_key_entry.grid(row=1,column=0,sticky="we",columnspan=3)
        self.steam_id_label.grid(row=2,column=0,sticky="w",columnspan=3)
        self.steam_id_entry.grid(row=3,column=0,sticky="we",columnspan=3)
        self.button_games_load.grid(row=4,column=0,sticky="we",columnspan=3)
        self.button_games_previous.grid(row=5,column=0)
        self.button_games_refresh.grid(row=5,column=1)
        self.button_games_next.grid(row=5,column=2)
        self.achievement_load.grid(row=6,column=0,sticky="w",columnspan=3)
        self.button_achievements_previous.grid(row=7,column=0)
        self.button_achievements_refresh.grid(row=7,column=1)
        self.button_achievements_next.grid(row=7,column=2)
        self.button_sensitive_load.grid(row=8,column=0,sticky="we",columnspan=3)
        self.button_sensitive_save.grid(row=9,column=0,sticky="we",columnspan=3)

        self.canvas_controls.grid(row=0,column=0,rowspan=10)
        self.loading_label.grid(row=0,column=1)

        self.window.mainloop()

    def todo_button(self):
        pass

    def get_sensitive(self):
        self.steam_api_key = self.api_key_entry.get()
        self.steam_user_id = self.steam_id_entry.get()

    def load_games(self):
        pass

    def load_sensitive(self):
        with open(self.filename_sensitive,"r") as file:
            output = file.read()
        self.steam_api_key, self.steam_user_id = output.split(" ")

        self.api_key_entry.delete(0,tk.END)
        self.steam_id_entry.delete(0,tk.END)

        self.api_key_entry.insert(0,self.steam_api_key)
        self.steam_id_entry.insert(0,self.steam_user_id)

    def save_sensitive(self):
        self.get_sensitive()
        to_write = f"{self.steam_api_key} {self.steam_user_id}"
        with open(self.filename_sensitive,"w") as file:
            file.write(to_write)

    def refresh_games(self):
        self.get_sensitive()

        request = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=STEAMKEY&steamid=STEAMID"
        request = request.replace("STEAMKEY",self.steam_api_key)
        request = request.replace("STEAMID", self.steam_user_id)

        output = requests.get(request)
        output = output.text
        data = json.loads(output)
        data = data["response"]["games"]
        total_games = len(data)
        for index,entry in enumerate(data):
            self.loader(index,total_games)
            game_id = entry["appid"]
            game_data = requests.get(f"http://store.steampowered.com/api/appdetails?appids={game_id}")
            game_data = game_data.text
            game_data = json.loads(game_data)
            if game_data:
                keys = list(game_data.keys())
                key = keys[0]
                if game_data[key]["success"]:
                    game_name = game_data[key]["data"]["name"]
                    self.game_name_id.append([game_name, keys[0]])

        with open(self.filename_name_ids,"w") as file:
            file.write("")

        for item in self.game_name_id:
            name,app_id = item
            name = name.replace(" ", "_")
            to_write = f"{name} {app_id}\n"
            filename = self.filename_name_ids
            with open(filename,"a") as file:
                file.write(to_write)

    def loader(self,count,maximum):
        count = count + 1
        output = f"{count} of {maximum}"
        self.loading_label.config(text=output)
        self.loading_label.update()




Main()