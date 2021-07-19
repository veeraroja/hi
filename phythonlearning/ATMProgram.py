#program on ATM mechine
pin , cash = input('please enter pin no. and cash').split ('@')
print ('pin and cash are:',pin,cash)
cashValue = int (cash)
atmAmount = 50000
remainingAmount = atmAmount - cashValue
print ('take your cash',cash,remainingAmount,sep="->")