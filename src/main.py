from rich import print_json
import json

def printjson(value: object) -> None:
    print_json(json.dumps(value))



class Partition:
    def __init__(self) -> None:
      pass  

class Page:
    def __init__(self, width: int, height: int, border: str="#") -> None:
        self.width = width
        self.height = height

        self.setup_screen(border)
    
    def setup_screen(self, border_char: str) -> None:

        self.display = [[border_char] * self.width] + [[border_char] + [" "] * (self.width-2) + [border_char]] * (self.height-2) + [[border_char] * self.width]


        # printjson(self.display)
    
    def render(self, **kwargs) -> None:
        for layer in self.display:
            print("".join(layer))

