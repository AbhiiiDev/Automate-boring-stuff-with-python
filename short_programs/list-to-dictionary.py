def add_to_inventory(inv,dragon_loot):
   for item in dragon_loot:
      inv[item]=inv.setdefault(item,0)+1
   return inv

# set_default and get() : both works same , just one returns and other changes 

inv = {'gold coin': 42, 'rope': 1}
print('inventory earlier: ',inv)
dragon_loot = ['gold coin', 'dagger', 'gold coin','ruby', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
print('inventory now: ',inv)