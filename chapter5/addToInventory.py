# Fantasy Game Inventory -2 practice problem from Automate Boring Stuff - Chapter 5
# https://automatetheboringstuff.com/chapter5/


def displayInventory(inventory):
	totalItems = 0
	print('Inventory:')
	for k in inventory.keys():
		totalItems = totalItems + inventory[k]
		print(str(inventory[k]) + ' ' + str(k))
		
	print('Total number of items: ' + str(totalItems))

def addToInventory(items, inventory):
	for i in range(len(items)):
		item = items[i]
		inventory.setdefault(item, 0)
		currentVal = inventory[item]
		currentVal = currentVal+1
		inventory[item] = currentVal


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
toAdd = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(toAdd, inventory)
displayInventory(inventory)
