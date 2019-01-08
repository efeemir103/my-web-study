from bottle import route, run, request, template, static_file, os, default_app, debug
from hashlib import sha256
import os, json, requests

supportedCurrencies={
"EUR":"Euro",
"USD":"US dollar",
"JPY":"Japanese yen",
"BGN":"Bulgarian lev",
"CZK":"Czech koruna",
"DKK":"Danish krone",
"GBP":"Pound sterling",
"HUF":"Hungarian forint",
"PLN":"Polish zloty",
"RON":"Romanian leu",
"SEK":"Swedish krona",
"CHF":"Swiss franc",
"ISK":"Icelandic krona",
"NOK":"Norwegian krone",
"HRK":"Croatian kuna",
"RUB":"Russian rouble",
"TRY":"Turkish lira",
"AUD":"Australian dollar",
"BRL":"Brazilian real",
"CAD":"Canadian dollar",
"CNY":"Chinese yuan renminbi",
"HKD":"Hong Kong dollar",
"IDR":"Indonesian rupiah",
"ILS":"Israeli shekel",
"INR":"Indian rupee",
"KRW":"South Korean won",
"MXN":"Mexican peso",
"MYR":"Malaysian ringgit",
"NZD":"New Zealand dollar",
"PHP":"Philippine piso",
"SGD":"Singapore dollar",
"THB":"Thai baht",
"ZAR":"South African rand"
}

currenciesList={
"EUR": 0,
"USD": 0,
"JPY": 0,
"BGN": 0,
"CZK": 0,
"DKK": 0,
"GBP": 0,
"HUF": 0,
"PLN": 0,
"RON": 0,
"SEK": 0,
"CHF": 0,
"ISK": 0,
"NOK": 0,
"HRK": 0,
"RUB": 0,
"TRY": 0,
"AUD": 0,
"BRL": 0,
"CAD": 0,
"CNY": 0,
"HKD": 0,
"IDR": 0,
"ILS": 0,
"INR": 0,
"KRW": 0,
"MXN": 0,
"MYR": 0,
"NZD": 0,
"PHP": 0,
"SGD": 0,
"THB": 0,
"ZAR": 0
}

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

class Database:
  def __init__(self,folder):
    self.users={}
    self.loggedInUsers={}
    self.folder=folder
  
  def save(self):
    with open(os.path.join(self.folder,"users.json"),"w+") as data:
      json.dump(self.users,data,indent=4)
  
  def load(self):
    with open(os.path.join(self.folder,"users.json"),"r") as data:
      self.users.update(dict(json.load(data)))
  
  def new_user(self,username,password,name):
    self.users.update(dict(username,{"Name":name,"Password":password,"Balances":currenciesList.copy()}))
  
  def remove_user(self,username):
    del self.users[username]
  
  def convert(self,base,to):
    if(base==to):
        return 1
    else:
      url="https://api.exchangeratesapi.io/latest?base="+base
      response = requests.get(url)
      data = response.text
      parsed = json.loads(data)
      rates = parsed["rates"]
      return rates[to]
  
  def exchange(self,sender,base,amount,to):
    if self.users.get(sender).get("Balances").get(base)>amount:
      self.users.get(sender).get("Balances").update(base,self.users.get(sender).get("Balances").get(base)-amount)
      self.users.get(sender).get("Balances").update(to,self.users.get(sender).get("Balances").get(to)+amount*self.convert(base,to))
  
  def trade(self,sender,reciever,amount,currency):
    if self.users.get(sender).get("Balances").get(currency)>amount:
      self.users.get(sender).get("Balances").update(currency,self.users.get(sender).get("Balances").get(currency)-amount)
      self.users.get(reciever).get("Balances").update(currency,self.users.get(reciever).get("Balances").get(currency)+amount)