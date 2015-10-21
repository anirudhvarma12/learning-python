# Fantasy Game Inventory -1 practice problem from Automate Boring Stuff - Chapter 5
# https://automatetheboringstuff.com/chapter5/

def displayInventory(inventory):
	totalItems = 0
	print('Inventory:')
	for k in inventory.keys():
		totalItems = totalItems + inventory[k]
		print(str(inventory[k]) + ' ' + k)

	print('Total number of items: ' + str(totalItems))

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
displayInventory(inventory)
