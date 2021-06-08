from urllib.request import Request, urlopen
import json

names=["TechNus09","R E N D","OwO Heartman","OwO Hnngh","OwO Matt","OwO DaddyShark","OwO Avi","OwO Yekzer","OwO DarkSecret","OwO Messwithme","PHG Maddy","GOAT HUBES","BlueLeaf","FW Katneko","Lukami","OwO DaveDust"]

old_rankers=[["TechNus09",70879010,0,0 ],
        ["R E N D",8557125,0,0 ],
        ["OwO Heartman",233598730,0,0 ],
        ["OwO Hnngh",189712790,0,0 ],
        ["OwO Matt",1461161650,0,0 ],
        ["OwO DaddyShark",3892070,0,0 ],
        ["OwO Avi",14417080,0,0 ],
        ["OwO Yekzer",10952730,0,0 ],
        ["OwO DarkSecret",580735685,0,0 ],
        ["OwO Messwithme",36413525,0,0 ],
        ["PHG Maddy",1778275,0,0],
        ["GOAT HUBES",11009300,0,0],
        ["BlueLeaf",277605,0,0],
        ["FW Katneko",152046700,0,0],
        ["Lukami",7968745,0,0],
        ["OwO DaveDust",31606960,0,0]]

new_rankers=[["TechNus09",70879010,0,0 ],
        ["R E N D",8557125,0,0 ],
        ["OwO Heartman",233598730,0,0 ],
        ["OwO Hnngh",189712790,0,0 ],
        ["OwO Matt",1461161650,0,0 ],
        ["OwO DaddyShark",3892070,0,0 ],
        ["OwO Avi",14417080,0,0 ],
        ["OwO Yekzer",10952730,0,0 ],
        ["OwO DarkSecret",580735685,0,0 ],
        ["OwO Messwithme",36413525,0,0 ],
        ["PHG Maddy",1778275,0,0],
        ["GOAT HUBES",11009300,0,0],
        ["BlueLeaf",277605,0,0],
        ["FW Katneko",152046700,0,0],
        ["Lukami",7968745,0,0],
        ["OwO DaveDust",31606960,0,0]]


xp_gain_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


print("Searching...")
print(" ")

count=0
for k in range(25001):  
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
                new_rankers[yy][1] =fdata[i]["xp"]
                print(new_rankers[yy][0]," claimed!!")
                count=count+1
                continue
        if (count==16):
            break

for i in range(len(xp_gain_list)):
    new_xp=new_rankers[i][1]
    old_xp=old_rankers[i][1]
    xpgain=new_xp-old_xp
    new_rankers[i][2]=new_xp-old_xp
    xp_gain_list[i]=xpgain
    
sorted_xp=sorted(xp_gain_list,reverse=True)

print("--------------------------------")
print("Top WoodCutting event Rankers")
print("--------------------------------")
print("#Rank | IGN | XP gain ")
for i in range(len(sorted_xp)):
    for j in range(len(sorted_xp)):
        if new_rankers[j][2]==sorted_xp[i]:
            order=j
            break
    print("#",i+1," ",new_rankers[order][0],"  ",new_rankers[order][2])