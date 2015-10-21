# Comma code practice problem from Automate Boring Stuff - Chapter 4
# https://automatetheboringstuff.com/chapter4/

def getStringSeparator(currentIdx, totalLength):
	if currentIdx==0:
		return ''
	elif totalLength-currentIdx > 1:
		return ', '
	else:
		return ' and '

def commaSeparate(args):
	value = '';
	totalLength = len(args)
	for i in range(totalLength):
		value = value+getStringSeparator(i, totalLength) +args[i]

	return value;

print(commaSeparate(['apples', 'bananas', 'tofu', 'cats']))