import time, random, sys
inventory = []
health = ['10']
def check_inventory():
	if len(inventory) == 0:
		print("\n")
		print("You have no items.")
		print("You should look around a bit.")
	else:
		print("\n")
		print("You have the following items:")
		print("\n").join(inventory)

def check_health():
	print("\n")
	print(("My health level is:"), health[0])
	
def help():
	print("\n")
	print("""
	This game runs on two or three word commands.
	Try typing commands like 'open the chest', 'go north door', or 'run away'
	Also, try 'check my inventory'
	""")
		
def start_room():
	print("\n")
	num = 0
	print("You are in a room with an open door to the north, and a sign on the wall written in big letters: 'Say Help'")
	choice = input('>').lower()
	while num < 3:
		if choice == "go north door":
			main_room()
		elif choice == "say help":
			help()
			time.sleep(1)
			start_room()
		elif choice == "check my inventory":
			check_inventory()
			time.sleep(1)
			start_room()
		elif choice == "check my health":
			check_health()
			time.sleep(1)
			start_room()
		num += 1
		choice = input('>').lower()
		
	dead()
	sys.exit()


def dont_know():
	print("\n")
	print("I don't know how to do that.")
	
def dead():
	print("\n")
	print("You stumble around aimlessly.")
	print("You are dead.")

def dead_from_monster():
	print("You are dead.")
	
def main_room():
	locked_doors = ['go east door', 'go north door']
	print("\n")
	print("You are in a room with four doors in all directions, and a sign on the wall with small letters.")
	choice = input('>').lower()
	while choice in locked_doors and 'key' not in inventory:
		print("\n")
		print("Looks like the door is locked")
		print("Maybe there's a key somewhere...")
		choice = input('>').lower()
	if choice == "go west door":
		key_room()
	elif choice == "go north door":
		sword_room()
	elif choice == "go east door":
		gold_room()
	elif choice == "go south door":
		start_room()
	elif choice == "read the sign":
		print("\n")
		print("Move like a compass.")
		time.sleep(1)
		print("\n")
		main_room()
	elif choice == "check my inventory":
		check_inventory()
		time.sleep(1)
		main_room()
	elif choice == "check my health":
		check_health()
		time.sleep(1)
		main_room()
	else:
		dont_know()
		main_room()
				
	
def key_room():
	print("\n")
	print("You are in a room with a treasure chest, and a door to the east.")
	choice = input('>').lower()
	while choice != "go east door":
		if choice == "look at chest" and "look treasure chest":
			print("\n")
			print("Looks like I can open it")
			choice = input('>').lower()
		elif choice == "open the chest":
			print("\n")
			print("You have a key")
			inventory.append('key')
			time.sleep(1)
			key_room()
		elif choice == "say help":
			help()
			time.sleep(1)
			key_room()
		elif choice == "check my inventory":
			check_inventory()
			time.sleep(1)
			key_room()
		elif choice == "check my health":
			check_health()
			time.sleep(1)
			key_room()
		else:
			dont_know()
			choice = input('>').lower()
	if choice == "go east door":
		main_room()
		
def sword_room():

	print("\n")
	if 'sword' in inventory:
		print("You are in a room with a door to the south, also a painting is hanging on the wall.")
	else:
		print("You are in a room with a door to the south, also a painting and a sword are hanging on the wall.")
	choice = input('>').lower()
	while choice != "go south door":
		if choice == "look at sword":
			print("\n")
			print("Looks like I can grab it")
			choice = input('>').lower()
		elif choice == "look at painting":
			print("\n")
			print("Maybe there's something more interesting to look at...")
			choice = input('>').lower()
		elif choice == "grab the sword":
			print("\n")
			print("You have a sword")
			inventory.append('sword')
			time.sleep(1)
			sword_room()
		elif choice == "inventory":
			check_inventory()
		elif choice == "say help":
			help()
			time.sleep(1)
			sword_room()
		elif choice == "check my inventory":
			check_inventory()
			time.sleep(1)
			sword_room()
		elif choice == "check my health":
			check_health()
			time.sleep(1)
			sword_room()
		else:
			dont_know()
			choice = input('>').lower()
	if choice == "go south door":
		main_room()
		
		
def gold_room():
	print("\n")
	print("You are in a room with a pot of gold...")
	time.sleep(1)
	print("But, it's guarded by a large monster!!!")
	print("He looks like we wants to fight over the gold.")
	choice = input('>').lower()
	while choice != "run away":
		if choice == "fight the monster":
			fight()
		elif choice == "look at monster":
			print("\n")
			print("He looks hungry")
			choice = input('>').lower()
		elif choice == "say help":
			help()
			time.sleep(1)
			gold_room()
		elif choice == "check my inventory":
			check_inventory()
			time.sleep(1)
			gold_room()
		elif choice == "check my health":
			check_health()
			time.sleep(1)
			gold_room()
		else:
			dont_know()
			choice = input('>').lower()
	if choice == "run away":
		main_room()
	
	
def fight():
	print("\n")
	print("You are in a fight with the monster.")
	print("You can choose to 'strike' or 'run away'")
	
	if 'sword' in inventory:
		monHealth = 10
	else:
		monHealth = 20
		
	choice = input('>').lower()
	
	while choice == 'strike':
		strike = random.randint(0,10)
		monHealth -= strike
		print("You strike the monster")
		time.sleep(1)
		if monHealth <= 0:
			print("The Monster is Defeated!")
			print("The Gold is yours!")
			print("Congratulations, you win!")
			print("\n")
			sys.exit()
		else:
			print("Monster's health is", monHealth)
		print("Monster strikes back.")
		time.sleep(1)
		strike = random.randint(0,10)
		health[0] = strike
		if health[0] <= 0:
			print("You have been defeated.")
			dead_from_monster()
			print("Game Over.")
			time.sleep(1)
			sys.exit()
		else:
			print("Your health is", health[0])
		choice = input('>').lower()	
		
	if choice == "run away":
		main_room()
			
	else:
		dont_know()
		
		
	
start_room()