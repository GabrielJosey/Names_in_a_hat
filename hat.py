from operator import attrgetter
import random
from person import Person

class Hat:
	def __init__(self, names: [Person]):
		self.names = names
	
	def sort_names(self, names: [Person]):
		names = names.sort(key=attrgetter('married'), reverse = True)
		self.names = names 
	
	def pick_name(self, name: Person):
		to_give_to = random.choice(self.names)
		# self.names.remove(to_give_to)
		giver = name.name
		print(f"{giver} is giving to {to_give_to.name}")