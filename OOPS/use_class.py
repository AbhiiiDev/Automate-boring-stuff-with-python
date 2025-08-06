import wizcoin

purse=wizcoin.WizCoin(5,3,4)
print(purse)
print('G: ',purse.gallons,'S: ',purse.sickles,'K: ',purse.knuts)
print('total value: ',purse.value())