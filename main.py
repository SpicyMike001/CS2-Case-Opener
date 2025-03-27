import tkinter as tk
from tkinter import messagebox
#from PIL import Image, ImageTk
import random
import time

MONEY = 150
CASE_COST = 500
CENTER_LINE_X = 400
SCROLL_SPEED = 16
ANIMATION_DURATION = 5000
ADJUSTMENT_SPEED = 5

GENERIC_SKINS = [
    "glock_18_candy_apple",  
    "glock_18_ground_water", 
    "p2000_grassland",       
    "p2000_silver",          
    "usps_forest_leaves",    
    "usps_royal_blue",       
    "five-seven_candy_apple",
    "five-seven_jungle",     
    "cz75-auto_army_sheen",  
    "cz75-auto_tuxedo",      
    "famas_colony",          
    "famas_contrast_spray",  
    "galil_ar_sage_spray",   
    "galil_ar_varicamo",     
    "m4a1-s_varicamo",       
    "m4a4_urban_ddpat",      
    "sg553_waves_perforated",
    "ssg08_blue_spruce",     
    "mp9_sand_dashed",       
    "nova_sand_dune", 
]

GOLDEN_SKINS = [
    "bayonet",
    "bowie_kinfe",
    "butterfly_kinfe",
    "flip_knife",
    "m9_bayonet",
    "broken_fang_gloves",
    "sport_gloves",
    "moto_gloves",
    "driver_gloves",
]

FRACTURE_SKINS = [
    "negev_ultralight",
    "p2000_gnarled",
    "sg553_olrusty",
    "ssg08_mainframe001",
    "p250_cassette",
    "p90_freight",
    "ppbizon_runic",
    "mag7_monstercall",
    "tec9_brother",
    "mac10_allure",
    "galilar_connexion",
    "mp5sd_kitbash",
    "m4a4_toothfairy",
    "glock18_vogue",
    "xm1014_entombed",
    "deagle_printstream",
    "ak47_legionofanubis",
]

CASES = {
    "kilowatt": {
        "name": "Kilowatt Case",
        "cost": 0.92+2.35,
        "skins": ["ak47_inheritance", "awp_chrome_cannon", "zeus_olympus", "kukri_knife"] + GENERIC_SKINS + GOLDEN_SKINS
    },
    "dreams_nightmares": {
        "name": "Dreams & Nightmares Case",
        "cost": 1.97+2.35, 
        "skins": ["ak47_nightwish", "dualberettas_melondrama", "ppbizon_spacecat", "butterfly_marble_fade"] + GENERIC_SKINS + GOLDEN_SKINS
    },
    "prisma_case": {
        "name": "Prisma Case",
        "cost": 1.12+2.35,
        "skins": ["awp_atheris", "m4a1_decimator"] + GENERIC_SKINS + GOLDEN_SKINS
    },
    "op_b_fang_case": {
        "name": "Operation Broken Fang Case",
        "cost": 7.03+2.35, 
        "skins": ["awp_corticera", "m4a1-s_bullet_rain"] + GENERIC_SKINS + GOLDEN_SKINS
    },
    "cac_2_case": {
        "name": "Chroma & Chroma 2 Cases",
        "cost": 5.00+2.35, 
        "skins": ["ak-47_neon_revolution", "awp_worm_god"] + GENERIC_SKINS + GOLDEN_SKINS
    },
    "sas_2_case": {
        "name": "Spectrum & Spectrum 2 Cases",
        "cost": 3.80+2.35, 
        "skins": ["m4a4_the_emperor", "ak-47_neon_revolution"] + GENERIC_SKINS + GOLDEN_SKINS
    },
    "fracture_case":{
        "name": "Fracture Case",
        "cost": 0.50+2.35,
        "skins": FRACTURE_SKINS + GOLDEN_SKINS
    }
}

SKINS = {
    "ak47_inheritance": {"name": "AK-47 | Inheritance", "value": 85.0, "standing": "gold"},
    "awp_chrome_cannon": {"name": "AWP | Chrome Cannon", "value": 12.00},
    "zeus_olympus": {"name": "Zeus | Olympus", "value": 3.00},
    "kukri_knife": {"name": "Kukri Knife | Fade", "value": 22.00, "standing": "gold"},
    "ak47_nightwish": {"name": "AK-47 | Nightwish", "value": 7.00},
    "dualberettas_melondrama": {"name": "Dual Berettas | Melondrama", "value": 4.00},
    "ppbizon_spacecat": {"name": "PP-Bizon | Spacecat", "value": 6.00},
    "butterfly_marble_fade": {"name": "Butterfly Knife | Marble Fade", "value": 35.00},
    "awp_atheris": {"name": "AWP | Atheris", "value": 10.00},
    "m4a1_decimator": {"name": "M4A1-S | Decimator", "value": 8.00},
    "awp_corticera": {"name": "AWP | Corticera", "value": 15.00},
    "m4a1-s_bullet_rain": {"name": "M4A1-S | Bullet Rain", "value": 12.00},
    "ak-47_neon_revolution": {"name": "AK-47 | Neon Revolution", "value": 10.00},
    "awp_worm_god": {"name": "AWP | Worm God", "value": 8.00},
    "m4a4_the_emperor": {"name": "M4A4 | The Emperor", "value": 15.00},

    "glock_18_candy_apple": {"name": "Glock-18 | Candy Apple", "value": 2.0},
    "glock_18_ground_water": {"name": "Glock-18 | Groundwater", "value": 2.5},
    "p2000_grassland": {"name": "P2000 | Grassland", "value": 1.5},
    "p2000_silver": {"name": "P2000 | Silver", "value": 2.0},
    "usps_forest_leaves": {"name": "USP-S | Forest Leaves", "value": 1.0},
    "usps_royal_blue": {"name": "USP-S | Royal Blue", "value": 1.5},
    "five-seven_candy_apple": {"name": "Five-Seven | Candy Apple", "value": 2.0},
    "five-seven_jungle": {"name": "Five-Seven | Jungle", "value": 2.5},
    "cz75-auto_army_sheen": {"name": "CZ75-Auto | Army Sheen", "value": 1.0},
    "cz75-auto_tuxedo": {"name": "CZ75-Auto | Tuxedo", "value": 1.5},
    "famas_colony": {"name": "Famas | Colony", "value": 1.0},
    "famas_contrast_spray": {"name": "Famas | Contrast Spray", "value": 1.5},
    "galil_ar_sage_spray": {"name": "Galil AR | Sage Spray", "value": 1.0},
    "galil_ar_varicamo": {"name": "Galil AR | VariCamo", "value": 1.5},
    "m4a1-s_varicamo": {"name": "M4A1-S | VariCamo", "value": 2.0},
    "m4a4_urban_ddpat": {"name": "M4A4 | Urban DDPAT", "value": 2.5},
    "sg553_waves_perforated": {"name": "SG553 | Waves Perforated", "value": 2.0},
    "ssg08_blue_spruce": {"name": "SSG08 | Blue Spruce", "value": 2.5},
    "mp9_sand_dashed": {"name": "MP9 | Sand Dashed", "value": 1.0},
    "nova_sand_dune": {"name": "Nova | Sand Dune", "value": 1.5},

    "bayonet": {"name": "Bayonet", "value": 30.00, "standing": "gold"},
    "bowie_kinfe": {"name": "Bowie Knife", "value": 25.00, "standing": "gold"},
    "butterfly_kinfe": {"name": "Butterfly Knife", "value": 25.00, "standing": "gold"},
    "flip_knife": {"name": "Flip Knife", "value": 25.00, "standing": "gold"},
    "m9_bayonet": {"name": "M9 Bayonet", "value": 30.00, "standing": "gold"},
    "broken_fang_gloves": {"name": "Broken Fang Gloves", "value": 20.00, "standing": "gold"},
    "sport_gloves": {"name": "Sport Gloves", "value": 20.00, "standing": "gold"},
    "moto_gloves": {"name": "Moto Gloves", "value": 20.00, "standing": "gold"},
    "driver_gloves": {"name": "Driver Gloves", "value": 20.00, "standing": "gold"},

    "negev_ultralight": {"name": "Negev | Ultralight", "value": 0.21},
    "p2000_gnarled": {"name": "P2000 | Gnarled", "value": 0.22},
    "sg553_olrusty": {"name": "SG 553 | Ol' Rusty", "value": 0.20},
    "ssg08_mainframe001": {"name": "SSG 08 | Mainframe 001", "value": 0.22},
    "p250_cassette": {"name": "P250 | Cassette", "value": 0.19},
    "p90_freight": {"name": "P90 | Freight", "value": 0.22},
    "ppbizon_runic": {"name": "PP-Bizon | Runic", "value": 0.18},
    "mag7_monstercall": {"name": "MAG-7 | Monster Call", "value": 1.76},
    "tec9_brother": {"name": "Tec-9 | Brother", "value": 1.49},
    "mac10_allure": {"name": "MAC-10 | Allure", "value": 1.55},
    "galilar_connexion": {"name": "Galil AR | Connexion", "value": 1.35},
    "mp5sd_kitbash": {"name": "MP5-SD | Kitbash", "value": 1.27},
    "m4a4_toothfairy": {"name": "M4A4 | Tooth Fairy", "value": 8.41},
    "glock18_vogue": {"name": "Glock-18 | Vogue", "value": 10.09},
    "xm1014_entombed": {"name": "XM1014 | Entombed", "value": 7.49},
    "deagle_printstream": {"name": "Desert Eagle | Printstream", "value": 92.48},
    "ak47_legionofanubis": {"name": "AK-47 | Legion of Anubis", "value": 15.3},
}

def build_weighted_skin_order(skin_list, multiplier=3):
    weighted_pool = []
    for skin in skin_list:
        if skin in GOLDEN_SKINS:
            weighted_pool.extend([skin] * 1)
        else:
            weighted_pool.extend([skin] * 5)
    order = []
    count = multiplier * len(skin_list)
    for i in range(count):
        order.append(random.choice(weighted_pool))
    return order

class CaseOpenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CS2 Case Opener")
        self.root.geometry("1200x700")
        self.setup_background()
        self.money = tk.IntVar(value=MONEY)
        self.full_inventory_value = tk.DoubleVar(value=0.0)
        self.sell_inventory_value = tk.DoubleVar(value=0.0)
        self.inventory = []
        self.active_case = None
        self.is_animating = False
        self.is_adjusting = False
        self.animation_start_time = 0
        self.target_tile = None
        self.tiles = []
        self.animation_after_id = None
        self.create_widgets()
        self.load_case_buttons()
        self.skip_animations_enabled = False  

    def setup_background(self):
        #try:
        #    self.app_bg_image = ImageTk.PhotoImage(Image.open("cs2bg.png"))
        #    bg_label = tk.Label(self.root, image=self.app_bg_image)
        #    bg_label.place(x=0, y=0, relwidth=1, relheight=1,)
        #    bg_label.lower()
        #except Exception as e:
        #    print("App background image not loaded:", e)
            self.root.configure(bg="#BFBFBF")
            
    def create_widgets(self):
        top_frame = tk.Frame(self.root, bg="#ffffff")
        top_frame.pack(pady=10)
        tk.Label(top_frame, text="Balance: €", bg="#ffffff").pack(side=tk.LEFT)
        tk.Label(top_frame, textvariable=self.money, bg="#ffffff").pack(side=tk.LEFT, padx=5)

        between_frame = tk.Frame(self.root, bg="#ffffff")
        between_frame.pack(pady=3)
        tk.Label(between_frame, text="Full Inventory Value: €", bg="#ffffff").pack(side=tk.LEFT)
        tk.Label(between_frame, textvariable=self.full_inventory_value, bg="#ffffff").pack(side=tk.LEFT, padx=5)

        between2_frame = tk.Frame(self.root, bg="#ffffff")
        between2_frame.pack(pady=3)
        tk.Label(between2_frame, text="Inventory Sell Value: €", bg="#ffffff").pack(side=tk.LEFT)
        tk.Label(between2_frame, textvariable=self.sell_inventory_value, bg="#ffffff").pack(side=tk.LEFT, padx=5)

        cheat_frame = tk.Frame(self.root, bg="#ffffff")
        cheat_frame.pack(pady=5)
        self.cheat_entry = tk.Entry(cheat_frame, width=25)
        self.cheat_entry.pack(side=tk.LEFT)
        tk.Button(cheat_frame, text="Enter", command=self.process_cheat).pack(side=tk.LEFT, padx=5)

        self.case_frame = tk.Frame(self.root, bg="#808080")
        self.case_frame.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=800, height=250, bg="#2a2a2a")
        self.canvas.pack(pady=15)
        self.canvas.create_line(CENTER_LINE_X, 0, CENTER_LINE_X, 250, fill="#FFD700", width=3, tags="center_line")

        inv_frame = tk.Frame(self.root, bg="#808080")
        inv_frame.pack(pady=10)
        self.inventory_list = tk.Listbox(inv_frame, width=50, height=8) 
        self.inventory_list.pack(side=tk.LEFT)
        tk.Button(inv_frame, text="Sell\n(75% Value)", command=self.sell_skin, height=4).pack(side=tk.LEFT, padx=10)
        tk.Button(inv_frame, text="Sell Inventory\n(75% Value)", command=self.sell_inventory, height=4).pack(side=tk.LEFT, padx=10)




    def load_case_buttons(self):
        for case_id, case in CASES.items():
            btn = tk.Button(self.case_frame, text=f"{case['name']}\n€{case['cost']}",
                            command=lambda c=case_id: self.start_case(c))
            btn.pack(side=tk.LEFT, padx=10)

    def create_skin_tile(self, skin, x_pos, index):
        group_tag = f"tile_{index}"
        if 1 == 2:
            print("Robinak kicsi a homloka")
            #"image" in skin and os.path.exists(skin["image"]): 
            #img = Image.open(skin["image"]).resize((150, 100))
            #img_tk = ImageTk.PhotoImage(img)
            #rect = self.canvas.create_image(x_pos, 125, image=img_tk, tags=(group_tag, "skin", "tile"))
            #self.canvas.image = img_tk
        else:
            fill_color = "#3a3a3a"
            if skin.get("standing", "").lower() == "gold":
                fill_color = "#FFD700"
            rect = self.canvas.create_rectangle(x_pos - 75, 75, x_pos + 75, 175,
                                                fill=fill_color, outline="#FFD700",
                                                tags=(group_tag, "skin", "tile"))
            self.canvas.create_text(x_pos, 125, text=skin["name"], fill="white", width=140, justify="center",
                                    tags=(group_tag, "tile"))
        return rect, group_tag

    def start_case(self, case_id, from_cheat=False):
        if self.is_animating or self.is_adjusting:
            return
        if not from_cheat and self.money.get() < CASES[case_id]["cost"]:
            messagebox.showerror("Error", "Not enough money!")
            return
        if self.animation_after_id is not None:
            self.root.after_cancel(self.animation_after_id)
            self.animation_after_id = None
        if not from_cheat:
            self.money.set(self.money.get() - CASES[case_id]["cost"])
        self.active_case = case_id
        
        if self.skip_animations_enabled:
            self.select_skin_immediately()
        else:
            self.animate_case_opening()

    def animate_case_opening(self):
        self.is_animating = True
        self.is_adjusting = False
        self.target_tile = None
        self.canvas.delete("tile")
        self.tiles = []
        case_skins = CASES[self.active_case]["skins"]
        self.skin_order = build_weighted_skin_order(case_skins, multiplier=3)
        random_offset = random.randint(0, 200)
        for i, skin_id in enumerate(self.skin_order):
            skin = SKINS[skin_id]
            x = 800 + i * 200 + random_offset
            rect, group_tag = self.create_skin_tile(skin, x, i)
            self.tiles.append({"group": group_tag, "skin_id": skin_id, "rect": rect})
        self.animation_start_time = time.time()
        self.animation_after_id = self.root.after(SCROLL_SPEED, self.update_scroll_animation)

    def update_scroll_animation(self):
        if not self.is_animating:
            return
        self.canvas.move("tile", -28, 0)
        for tile in self.tiles:
            coords = self.canvas.coords(tile["rect"])
            if len(coords) >= 2 and coords[0] + 200 < 0:
                self.canvas.move(tile["group"], len(self.skin_order) * 200, 0)
        elapsed = (time.time() - self.animation_start_time) * 1000
        if elapsed < ANIMATION_DURATION:
            self.animation_after_id = self.root.after(SCROLL_SPEED, self.update_scroll_animation)
        else:
            self.find_winner()

    def find_winner(self):
        if not self.is_animating:
            return
        closest_tile = None
        min_diff = float('inf')
        for tile in self.tiles:
            coords = self.canvas.coords(tile["rect"])
            if len(coords) >= 2:
                tile_center = coords[0] + 75
                diff = abs(tile_center - CENTER_LINE_X)
                if diff < min_diff:
                    min_diff = diff
                    closest_tile = tile
        self.target_tile = closest_tile
        self.is_adjusting = True
        self.animation_after_id = self.root.after(SCROLL_SPEED, self.adjust_to_center)

    def adjust_to_center(self):
        if not self.is_adjusting or self.target_tile is None or not self.is_animating:
            return
        coords = self.canvas.coords(self.target_tile["rect"])
        if len(coords) >= 2:
            current_center = coords[0] + 75
            diff = CENTER_LINE_X - current_center
            if abs(diff) < 2:
                self.select_winner()
                return
            move_amount = ADJUSTMENT_SPEED if abs(diff) > ADJUSTMENT_SPEED else abs(diff)
            if diff > 0:
                self.canvas.move("tile", move_amount, 0)
            else:
                self.canvas.move("tile", -move_amount, 0)
            self.animation_after_id = self.root.after(SCROLL_SPEED, self.adjust_to_center)
        else:
            self.is_adjusting = False

    def select_winner(self):
        if self.animation_after_id is not None:
            self.root.after_cancel(self.animation_after_id)
            self.animation_after_id = None
        if self.target_tile:
            winning_skin = self.target_tile["skin_id"]
            winning_skin_data = SKINS[winning_skin]
            self.inventory.append(winning_skin_data)
            self.update_inventory()
            messagebox.showinfo("Unlocked!", f"Obtained: {winning_skin_data['name']}")
        self.is_animating = False
        self.is_adjusting = False
        self.target_tile = None
        self.update_value_displays()

    def update_inventory(self):
        self.inventory_list.delete(0, tk.END)
        for item in self.inventory:
            self.inventory_list.insert(tk.END, f"{item['name']} (€{item['value']})")
        self.update_value_displays()


    def sell_skin(self):
        selected = self.inventory_list.curselection()
        if not selected:
            return
        index = selected[0]
        item = self.inventory[index]
        sell_value = int(item["value"] * 0.75)
        self.money.set(self.money.get() + sell_value)
        del self.inventory[index]
        self.update_inventory()
        messagebox.showinfo("Sold!", f"Sold {item['name']} for €{sell_value}")
        self.update_value_displays()

    def sell_inventory(self):
        if not self.inventory:
            return
        total_value = sum(item["value"] * 0.75 for item in self.inventory)
        self.money.set(self.money.get() + total_value)
        self.inventory = []
        self.update_inventory()
        messagebox.showinfo("Sold All!", f"Sold all items for €{total_value}")
        self.update_value_displays()    

    def update_value_displays(self):
        total_value = sum(item["value"] for item in self.inventory)
        self.full_inventory_value.set(round(total_value, 2))
        self.sell_inventory_value.set(round(total_value * 0.75, 2))

    def skip_animation(self):
        self.skip_animations_enabled = not self.skip_animations_enabled
        status = "enabled" if self.skip_animations_enabled else "disabled"
        messagebox.showinfo("Skip Animation", f"Animation skipping {status}")
        if self.skip_animations_enabled:
            self.canvas.create_line(CENTER_LINE_X, 0, CENTER_LINE_X, 250, fill="#A80304", width=3, tags="center_line")
        elif self.skip_animations_enabled == False:
            self.canvas.create_line(CENTER_LINE_X, 0, CENTER_LINE_X, 250, fill="#FFD700", width=3, tags="center_line")

    def select_skin_immediately(self):
        self.canvas.delete("tile")  # Clear canvas
        case_skins = CASES[self.active_case]["skins"]
        weighted_pool = []
        for skin in case_skins:
            if skin in GOLDEN_SKINS:
                weighted_pool.extend([skin] * 1)
            else:
                weighted_pool.extend([skin] * 5)
        
        winning_skin = random.choice(weighted_pool)
        winning_skin_data = SKINS[winning_skin]
        self.inventory.append(winning_skin_data)
        self.update_inventory()
        messagebox.showinfo("Unlocked!", f"Obtained: {winning_skin_data['name']}")
        self.update_value_displays()

    def process_cheat(self):
        code = self.cheat_entry.get().strip().lower()
        if code.startswith("give_money"):
            try:
                amount = int(code.split()[-1])
                self.money.set(self.money.get() + amount)
            except ValueError:
                pass
        if code.startswith("give_money"):
            amount = int(0>code.split()[-1]) 
            messagebox.showinfo("Error", "Invalid amount.")
        elif code.startswith("give_case"):
            case_id = code.split()[-1]
            if case_id in CASES:
                self.start_case(case_id, from_cheat=True)
        elif code.startswith("give_skins"):
            skin_ids = code.split()[1:]
            for skin_id in skin_ids:
                if skin_id in SKINS:
                    self.inventory.append(SKINS[skin_id])
            self.update_inventory()
        elif code.startswith("give_all_skins"):
            for skin_id in SKINS:
                self.inventory.append(SKINS[skin_id])
                self.update_inventory()
        elif code.startswith("reset_inventory"):
            self.inventory = []
            self.update_inventory()
            
        elif code.startswith("?") or code.startswith("help"):
            messagebox.showinfo("Help", "Available cheat codes:\n"
                                     "- give_money <amount>: Gives the player the specified amount of money.\n"
                                     "- give_case <case_id>: Starts the specified case for the player.\n"
                                     "- give_skins <skin_ids>: Gives the player the specified skins.\n"
                                     "- give_all_skins: Gives the player all available skins.\n"
                                     "- reset_inventory: Resets the player's inventory.\n"
                                     "- skip_animation: Toggles the skip animation feature.\n"
                                     "- ? or help: Displays this help message.\n"
                                     "- case_id? or case_id_help: Displays the available case IDs.\n"
                                     "- skin_id? or skin_id_help: Displays the available skin IDs.")            
        elif code.startswith("case_id?") or code.startswith("case_id_help"):
            messagebox.showinfo("Case IDs", "Available case IDs:\n" + "\n".join(CASES.keys()))
        elif code.startswith("skin_id?") or code.startswith("skin_id_help"):
            messagebox.showinfo("Skin IDs", "Available skin IDs:\n" + "\n".join(SKINS.keys()))
        elif code.startswith("skip_animation"):
            self.skip_animation()
        elif code.startswith(""):
            messagebox.showerror("Error", "Invalid cheat code.\n""Type ? or help for a list of available cheat codes.")
        self.cheat_entry.delete(0, tk.END)



if __name__ == "__main__":
    root = tk.Tk()
    app = CaseOpenerApp(root)
    root.mainloop()
