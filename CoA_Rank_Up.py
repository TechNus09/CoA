from urllib.request import Request, urlopen
import json 
lvltab = [0,46,99,159,229,309,401,507,628,768,928,1112,1324,1567,1847,2168,2537,2961,3448,4008,4651,5389,6237,7212,
8332,9618,11095,12792,14742,16982,19555,22510,25905,29805,34285,39431,45342,52132,59932,68892,79184,91006,104586,
120186,138106,158690,182335,209496,240696,276536,317705,364996,419319,481720,553400,635738,730320,838966,963768,
1107128,1271805,1460969,1678262,1927866,2214586,2543940,2922269,3356855,3856063,4429503,5088212,5844870,6714042,
7712459,8859339,10176758,11690075,13428420,15425254,17719014,20353852,23380486,26857176,30850844,35438364,40708040,
46761308,53714688,61702024,70877064,81416417,93522954,107429714,123404386,141754466,162833172,187046247,214859767,
246809111,283509271,325666684,374092835,429719875,493618564,567018884,651333710,748186012,859440093,987237472,
1134038112,1302667765,1496372370,1718880532,1974475291,2268076571,2605335878,2992745089,3437761413,3948950932,
4536153492,5210672106]
lvldef = [46, 53, 60, 70, 80, 92, 106, 121, 140, 160, 184, 212, 243, 280, 321, 369, 424, 487, 560, 643, 738, 
848, 975, 1120, 1286, 1477, 1697, 1950, 2240, 2573, 2955, 3395, 3900, 4480, 5146, 5911, 6790, 7800, 8960, 
10292, 11822, 13580, 15600, 17920, 20584, 23645, 27161, 31200, 35840, 41169, 47291, 54323, 62401, 71680, 82338,
94582, 108646, 124802, 143360, 164677, 189164, 217293, 249604, 286720, 329354, 378329, 434586, 499208, 573440,
658709, 756658, 869172, 998417, 1146880, 1317419, 1513317, 1738345, 1996834, 2293760, 2634838, 3026634, 3476690,
3993668, 4587520, 5269676, 6053268, 6953380, 7987336, 9175040, 10539353, 12106537, 13906760, 15974672, 18350080,
21078706, 24213075, 27813520, 31949344, 36700160, 42157413, 48426151, 55627040, 63898689, 73400320, 84314826,
96852302, 111254081, 127797379, 146800640, 168629653, 193704605, 222508162, 255594759, 293601280, 337259307,
387409211, 445016324, 511189519, 587202560]
skis = ['','-mining', '-smithing', '-woodcutting', '-crafting', '-fishing', '-cooking']
skils = ['combat','mining', 'smithing', 'woodcutting', 'crafting', 'fishing', 'cooking']
results = [
        {
            'skill': 'a','rank': 0,'xp': 0,'lvl': 0,'lvl%': 0
        },
        {
            'skill': 'a','rank': 0,'xp': 0,'lvl': 0,'lvl%': 0
        },
        {
            'skill': 'a','rank': 0,'xp': 0,'lvl': 0,'lvl%': 0
        },
        {
            'skill': 'a','rank': 0,'xp': 0,'lvl': 0,'lvl%': 0
        },
        {
            'skill': 'a','rank': 0,'xp': 0,'lvl': 0,'lvl%': 0
        },
        {
            'skill': 'a','rank': 0,'xp': 0,'lvl': 0,'lvl%': 0
        },
        {
            'skill': 'a','rank': 0,'xp': 0,'lvl': 0,'lvl%': 0
        },
]
combat={"bat" : 8 ,"slime" : 16 ,"fishing spider" : 38,"mashroom" : 46,"forest spider" : 55 ,"forest bat": 60 ,"snow bat" : 125 ,
"ice slime": 165 ,"snowman" : 210 ,"ice spider" : 250 ,"skeletal snake" : 300  ,"cave spider" : 350 ,"skeletal bat" : 385 ,
"sapphire scarab" : 400,"cave bat" : 560 ,"scorpion" : 700 ,"ice fiend" : 850 ,"raptor" : 900 ,"ruby scarab" : 1000 ,
"forest fiend" : 1080 ,"desert raptor" : 1850 ,"rock fiend" : 2000 ,"giant hornet" : 2100 ,"luminant slime" : 2200 ,
"ancient bat" : 2400 ,"ice raptor" : 2750 ,"arosite scarab" : 2850 ,"spectral flame" : 2700 ,"cactus soldier" : 2800 ,
"phantom flame" : 2900 ,"spectral fiend" : 3100 ,"phantom fiend" : 3600 ,"ancient cyclops" : 4000 ,"anubis" : 4000 ,
"magnetite scarab" : 4250 ,"golemite bat" : 4400 ,"golemite fiend" : 5270 ,"poltergeist" : 250 ,"anubis elite" : 7500 ,
"baby dragon" : 5750 ,"gold snake" : 1000 ,"brown snake" : 1000 ,"purple snake" : 1000 ,"sandstone golem" : 11500 ,
"cursed totem" : 1 ,"war bat" : 1200 ,"rock demon" : 10000 , "spinus" : 8500 ,"ancient war bat" : 12000 ,
"ice Demon" : 16500 ,"reanimated soul" : 1000 ,"golem" : 22500 ,"umbra" : 24000 ,"mummy" : 20000 }
mining={"tinO": 10, "copperO": 10, "IronO" : 50,"saltO": 80, "coalO": 115, "silverO": 135, "crimsteelO": 350,
 "goldO": 400, "pinksaltO" : 500, "mythanO": 650, "sandstoneO": 1100, "cobaltO": 1200, "varaxiumO": 1800, "blacksaltO": 2500}
smelting ={ "BronzeB" : 24, "ironB" : 8,	"steelB" : 14 , "crimsteelB" : 25,
"silverB" : 50,"goldN" : 60,"goldB" : 60,"mythanB" : 100,"cobaltB" : 200,"varaxiteB" : 350}
smithing ={ "BronzeB" : 5, "ironB" : 14,"steelB" : 20 , "crimsteelB" : 130,
"silverB" : 1000,"goldB" : 20000,"mythanB" : 5000,"cobaltB" : 15000,"varaxiteB" : 20000}
woodcutting={"pine": 10,"deadlog": 20,"birch": 50,"applewood": 115,"willow": 350,"oak": 475,
"chestnut": 650,"maple": 1200,"Olive": 1800,"palm": 2600}
crafting={"accuracyRelic":3 ,"guardingRelic":8 ,"healRelic":18 ,"wealthRelic":40 ,"powerRelic":105 ,"natureRelic":200 ,
"fireRelic":425 ,"damageRelic":900 ,"leechRelic":1400 ,"expRelic":1850 ,"cursedRelic":2750}
fishing={"anchovies":10,"goldfish":20,"mackerel":50,"squid":115,"sardine":375,"eel":500,"anglerfish":625,
"trout":750,"jellyfish":900,"bass":1350,"herringbone":1700,"tuna":2000,"lobster":3500,"sea turtle":6500,
"manta ray":9500,"shark":14500,"orca":29500,"giant squid":55000}
cooking={"anchovies":10,"mackerel":50,"squid":115,"sardine":375,"eel":500,"anglerfish":30,
"trout":750,"bass":1350,"tuna":2000,"lobster":3500,"sea turtle":6500,
"manta ray":9500,"shark":13500,"orca":22500,"giant squid":41500}
miningresc={"tinO","copperO","IronO","saltO","coalO","silverO","crimsteelO",
"goldO","pinksaltO","mythanO","sandstoneO","cobaltO","varaxiumO","blacksaltO"}
smithingresc ={"BronzeB","ironB","steelB","crimsteelB","silverB","goldN",
"goldB","mythanB","cobaltB","varaxiteB"}
woodcuttingresc={"pine","deadlog","birch","applewood","willow","oak","chestnut",
"maple","Olive","palm"}
craftingresc={"accuracyRelic","guardingRelic","healRelic","wealthRelic",
"powerRelic","natureRelic","fireRelic","damageRelic","leechRelic","expRelic",
"cursedRelic"}
fishingresc={"anchovies","goldfish","mackerel","squid","sardine","eel","anglerfish",
"trout","jellyfish","bass","herringbone","tuna","lobster","sea turtle","manta ray",
"shark","orca","giant squid"}
cookingresc={"anchovies","mackerel","squid","sardine","eel","anglerfish","trout",
"bass","tuna","lobster","sea turtle","manta ray","shark","orca","giant squid"}
combatresc={"bat","slime","fishing spider","mashroom","forest spider","forest bat",
"snow bat","ice slime","snowman","ice spider",
"skeletal snake","cave spider","skeletal bat","sapphire scarab","cave bat","scorpion",
"ice fiend","raptor","ruby scarab",
"forest fiend","desert raptor","rock fiend","giant hornet","luminant slime",
"ancient bat","ice raptor","arosite scarab",
"spectral flame","cactus soldier","phantom flame","spectral fiend","phantom fiend",
"ancient cyclops","anubis",
"magnetite scarab","golemite bat","golemite fiend","poltergeist","anubis elite",
"baby dragon","gold snake","brown snake",
"purple snake","sandstone golem","cursed totem","war bat","rock demon","spinus",
"ancient war bat","ice Demon","reanimated soul",
"golem","umbra","mummy"}
skills=["combat", "mining", "smithing", "woodcutting", "crafting", "fishing", "cooking"]
skillss={"combat": combatresc, "mining": miningresc, "smithing":smithingresc, "woodcutting":woodcuttingresc, "crafting": craftingresc, "fishing":fishingresc, "cooking":cookingresc}
skillsss={"combat": combat, "mining": mining, "smithing":smithing, "woodcutting":woodcutting, "crafting": crafting, "fishing":fishing, "cooking":cooking}
name = input('type ur name : ')
while True :
    b = input('how many ranks u wanna be the search limit :')
    if b.isdecimal():
        n = (int(b) // 20) +1
        break
print('searching .....')
print(name)
totalxp = 0
totalrank = 0
tperc = 0
tlvl = 0
generalrank = 0
totalperc = 0
totallvl = 0
TOT = 0
for m in range(0,7) :
    results[m]['skill'] = skils[m]
    for k in range(0,n):  
        headers = {'User-Agent': 'Mozilla/5.0'}        
        request = Request('https://www.curseofaros.com/highscores'+skis[m]+'.json?p='+str(k), headers=headers)
        html = urlopen(request).read()       
        data = html.decode("utf-8")        
        fdata = json.loads(data)
        for i in range(0,20): 
            j = 20 * k + i + 1
            #check names get rank
            if fdata[i]["name"] == name :
                print('ur rank in '+skils[m]+' is ',j)
                results[m]['rank'] = j
                print('ur xp in '+skils[m]+' is ',fdata[i]["xp"])
                results[m]['xp'] = fdata[i]["xp"]
                pass
                #get lvl % from xp
                for l in range(120):
                    if (fdata[i]["xp"] > lvltab[l]):
                        lvl = l+1
                        results[m]['lvl'] = lvl
                        a = round((((fdata[i]["xp"] - lvltab[l]) / lvldef[l])*100),2)
                        results[m]['lvl%'] = a
                    else :
                        break
                print('ur lvl is ',lvl,'-',a,'%')
                print("----------------------------------------------")
                break
            else:
                continue
#print(results)
u=0
for w in range (0,7) :
        if (results[w]['xp']!=0) :
            u +=1
for d in range(0,7) :
    totalxp += results[d]['xp']
    totalrank += results[d]['rank']
    tperc += results[d]['lvl%']
    tlvl +=results[d]['lvl']
    
TOT = ((tperc / 100) + tlvl) / u
totallvl = TOT // 1
totalperc = round((TOT % 1),2)
#print(results)
print('ur total xp is ',totalxp)
print('ur total lvl is ',tlvl)
print('ur average lvl is ',totallvl,'-',totalperc,'%')
print("----------------------------------------------")
while True :
    print("combat - mining - smithing - woodcutting - crafting - fishing - cooking")
    while True :
        skill=input("choose a skill :  ")
        if any(skill.lower() in word for word in skills):
            skill=skill.lower()
            break
        else:
            print("skill doesn't exist or typed wrong")
    #get lvl
    ss=0
    for ii in range(7):
        if results[ii]['skill']==skill:
            ss=ii
    lv=results[ss]['lvl']
    per=results[ss]['lvl%']
    #get target lvl
    while True :
        nlv=int(input("whats your target lvl :  "))
        if nlv in range(1,121) :
            break
        else:
            print("target lvl must be between 2 and 120")
    #get target %)
    while True :
        nper=float(input("whats your target lvl % (exemple: 0.0/0.9/40.9/100.0):  "))
        if (per*100) in range(10001) :
            break
        else:
            print("% must be in form of 'xx.x' from 0.0 to 100.0")
    #get lvling up resource
    print(skill.lower() +" resources are : ",skillss[skill])
    while True :
        resc = input("what resource you wanna use to lvl up :  ")
        if any(resc in word for word in skillss[skill]):
            break
        else:
            print("resource doesn't exist or typed wrong")
    #calculating......
    def getxp( lv, nlv, per, nper ):
        XPneeded=0
        lvltab = [0,46,99,159,229,309,401,507,628,768,928,1112,1324,1567,1847,2168,2537,2961,3448,4008,4651,5389,6237,7212,8332,9618,11095,12792,14742,16982,19555,22510,25905,29805,34285,
        39431,45342,52132,59932,68892,79184,91006,104586,120186,138106,158690,182335,209496,240696,276536,317705,364996,419319,481720,553400,635738,730320,838966,963768,1107128,1271805,
        1460969,1678262,1927866,2214586,2543940,2922269,3356855,3856063,4429503,5088212,5844870,6714042,7712459,8859339,10176758,11690075,13428420,15425254,17719014,20353852,23380486,
        26857176,30850844,35438364,40708040,46761308,53714688,61702024,70877064,81416417,93522954,107429714,123404386,141754466,162833172,187046247,214859767,246809111,283509271,325666684,
        374092835,429719875,493618564,567018884,651333710,748186012,859440093,987237472,1134038112,1302667765,1496372370,1718880532,1974475291,2268076571,2605335878,2992745089,3437761413,
        3948950932,4536153492,5210672106]
        lvldef = [46, 53, 60, 70, 80, 92, 106, 121, 140, 160, 184, 212, 243, 280, 321, 369, 424, 487, 560, 643, 738, 848, 975, 1120, 1286, 1477, 1697, 1950, 2240, 2573, 2955, 3395, 3900, 
        4480, 5146, 5911, 6790, 7800, 8960, 10292, 11822, 13580, 15600, 17920, 20584, 23645, 27161, 31200, 35840, 41169, 47291, 54323, 62401, 71680, 82338, 94582, 108646, 124802, 143360, 
        164677, 189164, 217293, 249604, 286720, 329354, 378329, 434586, 499208, 573440, 658709, 756658, 869172, 998417, 1146880, 1317419, 1513317, 1738345, 1996834, 2293760, 2634838, 3026634, 
        3476690, 3993668, 4587520, 5269676, 6053268, 6953380, 7987336, 9175040, 10539353, 12106537, 13906760, 15974672, 18350080, 21078706, 24213075, 27813520, 31949344, 36700160, 42157413, 
        48426151, 55627040, 63898689, 73400320, 84314826, 96852302, 111254081, 127797379, 146800640, 168629653, 193704605, 222508162, 255594759, 293601280, 337259307, 387409211, 445016324, 
        511189519, 587202560]
        minxp= lvltab[lv-1] + (lvldef[lv-1]*(per/100))
        bigxp= lvltab[nlv-1] + (lvldef[nlv-1]*(nper/100))
        XPneeded = round(bigxp - minxp)
        return XPneeded
    rescneeded=round(getxp( lv, nlv, per, nper )/skillsss[skill][resc])
    invneeded=round(rescneeded/36)
    print("you need around ",rescneeded," of "+resc,"( ",invneeded," inventory)")
    print("---------------------------------------------------------------")
    while True:
        next=input("type 'again' to try again or 'quit' to quit the program: ")
        print("---------------------------------------------------------------")
        if  ((next.lower()=="again") or(next.lower()=="quit")) :
            break
        else:
            continue
    if (next.lower()=="again") :
        continue
    elif (next.lower()=="quit") :
        break