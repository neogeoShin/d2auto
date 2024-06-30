import pyautogui
import json

def item_pick(item, x1, y1):
    #match = [u'\ud032', u'\ud033', u'\ud034']
    match = ["모너크"]
    for ii in item:
        if any(s in ii[1] for s in match) and ii[2] > 0.01:
            coordinates_set = ii[0]
            xx = (int(ii[0][0][0]) + int(ii[0][1][0])) / 2 + x1
            yy = (int(ii[0][0][1]) + int(ii[0][2][1])) / 2 + y1
            pyautogui.moveTo(xx, yy)
            #pyautogui.click(x=xx, y=yy)
            pyautogui.click()
            print(f"{ii[1]} {xx} {yy} clicked\n")

# item name parser for picking candidate
class ItemPick:
    
    def __init__(self, json_location):
        self.json_location = json_location
        self.pick_items = []
        f = None
        try:
            f = open(json_location, "rb")
        except IOError:
            print(f"Couldn't open the file {json_location}!")
        try:
            self.item_dict = json.load(f)
        except ValueError as e:
            print(f"Error to load {json_location}!")
            self.item_dict = []

    def printout(self):
        print( self.item_dict )

    def pick(self, item):
        pass

    def itemparse(self):
        match = [u'\ud032', u'\ud033', u'\ud034']
        for l in self.item_dict:
            for t in l.items():
                if t[0] == "koKR":
                    if any(s in t[1] for s in match):
                        continue
                    else:
                        self.pick_items.insert(-1, t[1])

picker = ItemPick(r"C:\Program Files (x86)\Diablo II Resurrected\mods\comg\comg.mpq\data\local\lng\strings\item-names.json")
picker.itemparse() 

