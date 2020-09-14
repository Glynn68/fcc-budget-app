class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    # amount spent counter for chart
    self.spent = 0

  

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    return self.ledger
 

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": -amount,"description": description})
      #amount spent counter for chart
      self.spent += amount
      return True
    else:
      return False

  def get_balance(self):
    dicy = {}
    balance = 0
    for i in range (len(self.ledger)):  
      dicy = self.ledger[i]
      balance += dicy['amount']
    return balance

  def transfer(self, amount, wee):
    if self.check_funds(amount):
      self.withdraw(amount, 'Transfer to '+ wee.name)
      wee.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def check_funds(self, request):
      dicy = {}
      value = 0
      for i in range (len(self.ledger)):
        dicy = self.ledger[i]
        value += dicy['amount']
      if value < request:
        return False
      else:
        return True

  def __str__(self):
    cat_len = len(self.name)
    stars = (30 - cat_len)//2
    top_line = '*' * stars
    top_line += self.name
    remain = 30 - len(top_line)
    top_line += '*' * remain + '\n'
    dicy = {}
    items = ''
    for i in range (len(self.ledger)):
      dicy = self.ledger[i]
      desc = (dicy['description'] + 23 * ' ')[:23]
      items += desc + "{:.2f}".format(dicy['amount']).rjust(7) + '\n'
    return top_line + items + 'Total: ' + str(self.get_balance())


def create_spend_chart(categories):
  # calculate Total Spend
  total_spent = 0
  for i in categories:
    total_spent += i.spent
  
  #Calculate % spend for each category
  perc = []
  a = 0
  cat = []
  for i in categories:
    perc.append(str(10*(i.spent/total_spent))[0])
    cat.append(i.name)
    a += 1

  #create graph top half
  a = 0
  b = ""
  b += "Percentage spent by category\n"
  for y_axis in range (100, -10, -10):
    b += (str(y_axis).rjust(3) + "| ")
    for c in range (len(cat)):
      if int(perc[c]) >= int(y_axis/10):
       b += ("o  ")
      else:
       b += ("   ")
    b += "\n"
  a += 1

  # add horizontal bars in middle of graph
  b += "    ----"
  for c in range (len(cat)):
    b += "--"
  b += "\n"

  # find longest category length
  lengths = []
  for c in range(len(cat)):
    lengths.append(len(cat[c]))
  largest = max(lengths)

  #add vertical printed categories
  a = 0 
  for i in range (largest):
    b += "     "
    for c in range(len(cat)):
      if i < len(cat[c]):
        e = cat[c]
        b += e[a] + "  "
      else:
        b += "   "
    if i <= largest-2:
      b += "\n"
    a += 1
  
  return b


