from person import Person
from hat import Hat
from names import NAMES

hat = Hat(names=NAMES)

for name in NAMES:
    #print(name.__dict__)
    hat.pick_name(name=name)