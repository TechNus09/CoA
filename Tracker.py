from urllib.request import Request, urlopen
import json


names=["TechNus09","R E N D","OwO Heartman","OwO Hnngh","OwO Matt","OwO DaddyShark","OwO Avi","OwO Yekzer","OwO DarkSecret","OwO Messwithme"]

int_rankers=[{"ign": "TechNus09","xp": 70879010,"xp gain":0,"rank": 382,"Erank":0 },
        {"ign": "R E N D","xp": 8557125,"xp gain":0,"rank": 3543,"Erank":0 },
        {"ign": "OwO Heartman","xp": 233598730,"xp gain":0,"rank": 61,"Erank":0 },
        {"ign": "OwO Hnngh","xp": 189712790,"xp gain":0,"rank": 78,"Erank":0 },
        {"ign": "OwO Matt","xp": 1461161650,"xp gain":0,"rank": 5,"Erank":0 },
        {"ign": "OwO DaddyShark","xp": 3892070,"xp gain":0,"rank": 7001,"Erank":0 },
        {"ign": "OwO Avi","xp": 14417080,"xp gain":0,"rank": 2141,"Erank":0 },
        {"ign": "OwO Yekzer","xp": 10952730,"xp gain":0,"rank": 2802,"Erank":0 },
        {"ign": "OwO DarkSecret","xp": 580735685,"xp gain":0,"rank": 12,"Erank":0 },
        {"ign": "OwO Messwithme","xp": 36413525,"xp gain":0,"rank": 733,"Erank":0 }]
xp_gain_list=[]        

old_rankers=int_rankers
new_rankers=int_rankers

maxi=old_rankers[0]["rank"]
mini=old_rankers[0]["rank"]

def getLimit (jon,max,min):
    for i in range(len(int_rankers)):
        if (max < jon[i]["rank"]):
            max = jon[i]["rank"]
            continue
        if (min > jon[i]["rank"]):
            min = jon[i]["rank"] 
            continue
    return max,min

print("min is ",getLimit(int_rankers,maxi,mini)[1])
print("max is ",getLimit(int_rankers,maxi,mini)[0])

maxi=(getLimit(int_rankers,maxi,mini)[0] // 20 ) 
mini=(getLimit(int_rankers,maxi,mini)[1] // 20 ) 

print("page min is ",mini)
print("page max is ",maxi)

for k in range(mini,maxi+1):  
        url='https://www.curseofaros.com/highscores-woodcutting.json?p='+str(k)
        headers = {'User-Agent': 'Mozilla/5.0'}        
        request = Request(url, headers=headers)
        html = urlopen(request).read()       
        data = html.decode("utf-8")        
        fdata = json.loads(data)
        for i in range(0,20): 
            j = 20 * k + i + 1
            #check names get rank
            if fdata[i]["name"] in names :
                yy=names.index(fdata[i]["name"])
                new_rankers[yy]["rank"] = j
                new_rankers[yy]["xp"] =xp=fdata[i]["xp"]
                print(new_rankers[yy]["ign"]," claimed!!")
                continue
        continue
    
print(new_rankers)

for i in range(len(new_rankers)):
    new_xp=new_rankers[i]["xp"]
    old_xp=old_rankers[i]["xp"]
    new_rankers[i]["xp gain"]=new_xp-old_xp
    xpgain=new_xp-old_xp
    xp_gain_list.append(xpgain)
    
sorted_xp=sorted(xp_gain_list)

for i in range(len(sorted_xp)):
    for j in range(len(sorted_xp)):
        if new_rankers[j]["xp gain"]==sorted_xp[i]:
            order=j
            break
    print("#",i+1," ",new_rankers[order]["ign"],"  ",new_rankers[order]["xp gain"])