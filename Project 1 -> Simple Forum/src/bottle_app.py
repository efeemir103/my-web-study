from bottle import route, run, request, template, static_file, get, os, default_app, debug
from hashlib import sha256
import os, json, requests, secrets

starter_currency={"USD":1000}

supported_currencies={
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

currencies_list={
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
        self.users_dict = {}
        self.user_balances = {}
        self.loggedInUsers = {}
        self.folder = folder

    def save_exists(self):
        return os.path.isfile(os.path.join(self.folder,"accounts.json")) and os.path.isfile(os.path.join(self.folder,"balances.json"))

    def load(self):
        with open(os.path.join(self.folder,"accounts.json"),"r") as data:
            self.users_dict.update(dict(json.load(data)))
        with open(os.path.join(self.folder,"balances.json"),"r") as data:
            self.user_balances.update(dict(json.load(data)))

    def save(self):
        with open(os.path.join(self.folder,"accounts.json"),"w+") as data:
            json.dump(self.users_dict,data,indent=4)
        with open(os.path.join(self.folder,"balances.json"),"w+") as data:
            json.dump(self.user_balances,data,indent=4)

    def new_account(self,name,username,password):#Create new user with uid, name, username and balance
        uid=secrets.token_hex(16)
        self.users_dict.update({uid:{"name":name,"username":username,"password":password}})
        self.users_dict.update({uid:currencies_list.copy()})
        self.users_dict.update(starter_currency.copy())

    def remove_user(self,uid):
        del self.users_dict[uid]

    def get_uid(self,username):
        for key,value in self.users_dict:
            if value["username"] == username:
                return key
        return "error - user not found"

    def exchange(self,sender,base,amount,to):#Currency exchange
        if self.users_dict.get(sender).get("Balances").get(base)>amount:
            self.users_dict.get(sender).get("Balances").update(base,self.users_dict.get(sender).get("Balances").get(base)-amount)
            self.users_dict.get(sender).get("Balances").update(to,self.users_dict.get(sender).get("Balances").get(to)+amount*self.convert(base,to))

    def trade(self,sender,reciever,amount,currency):#Send money between accounts
        if self.users_dict.get(sender).get("Balances").get(currency)>amount:
            self.users_dict.get(sender).get("Balances").update(currency,self.users_dict.get(sender).get("Balances").get(currency)-amount)
            self.users_dict.get(reciever).get("Balances").update(currency,self.users_dict.get(reciever).get("Balances").get(currency)+amount)


db=Database("database")

def convert(self,base,to):#convertes a base currency to target currency
    if base == to:
        return 1
    else:
        url="https://api.exchangeratesapi.io/latest?base="+base
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        rates = parsed["rates"]
        return rates[to]

def get_rates(base):#Returns rates as dict
    url = "https://api.exchangeratesapi.io/latest?base="+base
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    rates = dict(parsed["rates"])
    if base in rates:
        del rates[base]
    for y,x in rates.items():
        rates[y]=1/x
    return rates

@route('/')
def index():
    return template('index', curr_names=supported_currencies)

@route('/index')
def index():
    return template('index', curr_names=supported_currencies)

@route('/index.html')
def index():
    return template('index', curr_names=supported_currencies)

@route('/rates/<base>')
def index(base):
    return template('currency_rates', base=base, rates=get_rates(base), supported_currencies=supported_currencies)

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

debug(True)
app = default_app()
if __name__=="__main__":
    if db.save_exists():
        db.load()
    run()
    db.save()
