from urllib.request import Request, urlopen
import json 
lvltab = [0,46,99,159,229,309,401,507,628,768,928,1112,1324,1567,1847,2168,2537,2961,3448,4008,4651,5389,6237,7212,8332,9618,11095,12792,14742,16982,19555,22510,25905,29805,34285,39431,45342,52132,59932,68892,79184,91006,104586,120186,138106,158690,182335,209496,240696,276536,317705,364996,419319,481720,553400,635738,730320,838966,963768,1107128,1271805,1460969,1678262,1927866,2214586,2543940,2922269,3356855,3856063,4429503,5088212,5844870,6714042,7712459,8859339,10176758,11690075,13428420,15425254,17719014,20353852,23380486,26857176,30850844,35438364,40708040,46761308,53714688,61702024,70877064,81416417,93522954,107429714,123404386,141754466,162833172,187046247,214859767,246809111,283509271,325666684,374092835,429719875,493618564,567018884,651333710,748186012,859440093,987237472,1134038112,1302667765,1496372370,1718880532,1974475291,2268076571,2605335878,2992745089,3437761413,3948950932,4536153492,5210672106]
lvldef = [46, 53, 60, 70, 80, 92, 106, 121, 140, 160, 184, 212, 243, 280, 321, 369, 424, 487, 560, 643, 738, 848, 975, 1120, 1286, 1477, 1697, 1950, 2240, 2573, 2955, 3395, 3900, 4480, 5146, 5911, 6790, 7800, 8960, 10292, 11822, 13580, 15600, 17920, 20584, 23645, 27161, 31200, 35840, 41169, 47291, 54323, 62401, 71680, 82338, 94582, 108646, 124802, 143360, 164677, 189164, 217293, 249604, 286720, 329354, 378329, 434586, 499208, 573440, 658709, 756658, 869172, 998417, 1146880, 1317419, 1513317, 1738345, 1996834, 2293760, 2634838, 3026634, 3476690, 3993668, 4587520, 5269676, 6053268, 6953380, 7987336, 9175040, 10539353, 12106537, 13906760, 15974672, 18350080, 21078706, 24213075, 27813520, 31949344, 36700160, 42157413, 48426151, 55627040, 63898689, 73400320, 84314826, 96852302, 111254081, 127797379, 146800640, 168629653, 193704605, 222508162, 255594759, 293601280, 337259307, 387409211, 445016324, 511189519, 587202560]
skills = ['','-mining', '-smithing', '-woodcutting', '-crafting', '-fishing', '-cooking']
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
        request = Request('https://www.curseofaros.com/highscores'+skills[m]+'.json?p='+str(k), headers=headers)
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
                pass
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