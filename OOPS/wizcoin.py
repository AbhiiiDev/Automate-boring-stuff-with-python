class WizCoin:
    def __init__(self,gallons,sickles,knuts):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        self.gallons=gallons
        self.sickles=sickles
        self.knuts=knuts
        # : __init__() methods NEVER have a return statement.        

    def value(self):
        """The value (in knuts) of all the coins in this WizCoin object."""
        return (self.gallons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
        