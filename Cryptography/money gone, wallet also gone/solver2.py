from Crypto.Util.number import inverse, long_to_bytes
from math import gcd

n = [80574199963463814094523829433857713147452655251365772886339787207944839676638523229780137733516503918898820274637968515502453663620903692811092520101511822087324086546997798707429218212108804233562826865487495882830673476459208802285040010345697151446745714797685081969295096625622527997959258089288866646399, 62126161889148784630727822992623951237887952211166536689485138915701984225068047432725701422931706867267128639413976367792448709181814040891796248747471384585154853466032217071097236014386972014976878342480841102053348322533676651102295543248326007579707329727289164501482478085425089737747142091711900689033, 55913610671578635514119269124851307855148519797422751256906924805793479755452446396213104488948575649600530617585880389561399479810398947165067460661253917550838240593002549325657773144054566482996416821589069834047377472742672172763569414732109739365275008982070347363777674042687851620188617992634744635491, 96190700791527452908049152727831717353374587620621214502804989411599512476703024657386885377567001075272537879139280728902312375314531694596932657244685159651966597642850854423713459536968851348514995633646545626720323319232488341878517268346847561919233783293618816559836924968946423546344779250100399692017, 135785772481403646452023886688053745096386476569346409186492432982537953099937919760693846742087319559506557964533783197899903066894586786446150727004372727229331821355640707901006478571486325057847364520273445964717174153595183669538043239873994584041881705525099193850102208760511666332599106587249853034453, 114411578685490122494903123265852724132179010102689766146333241385323713256034129115525582037738747511339274668258699872774170517125835604076670248435077071751492483920599568203911433677614721481237054615802775620271021767713330778567711158335035140417442474475206696543493053111994802432380097719753572154057, 133181964915962492008682294148359398067121185855407707780955189820102031504585307631287511862727894997811141756211130784300516979729258670628783849823624681636189436473492066960348489739683835333465002763221077420197531720884727232955954555540560494896229079726849062814267075297894722841221790619480116142459, 118310655506957492688787077479888566609635644355467850581202949679436698580851132806864390394986987511940499860070349798886095790714736639704436645211544850098491275171681277970453722298283573757458940905310957098434004076241629304979953898999759358017827131009330898949390523048849435777713025727485830791061, 108540262426516697889923154764273256552629614044442559633561174720618378654600541230352445320953446432449984287268236669247530192713049781470606776845295286167374409340696768198865463905733622653275644531685779706410929237622884295354630694740303603600803375740137056659501727860631713720014326014129832048243, 121134892647636623111508901023660861020072789928333565208758913895616650312353776820839389623556392766688429974504963103716150493272797824068387508348347848531300212000867035751555945392714069241831885446319960071226794823883968778839742553122982811095699814202648881978596777657816937873562655312973944612887, 88868543363948906092335106236877844641880447384406289836870202745919922080275495259094458240694438077103485957207541237531389508506701161814757376327922045529901072711288985828823540457065897243627860318959025468730642121553067181266811180263699250064519399310487261505403331234406038235740559014317976515191, 84336164681063682123808110268450304702110879782150085484452266924817907228077072373164679116294580427637121741226431444806982088633639306818613022674024201775036877539229388320654671474398514185925669416866987666079938164149760441694337139323666698229234337864763081366009810748271878226020782610760894086289, 111642051044543128845054925235308392881310897577861416834576877755045757187850582869975503703791838841794561999830169055043454214995857441986514087893323870474090396610632632455479089035981553193841713219512382261276480915787787612226423718597489303009080650245800003016356001618297445907583318919553402271037, 88212778155458908033607217944711570340609070098220169323011176375412822186773679810606354360045429093666038713095197376567394708365224532660769571968770630332618419113132146956046963239196291235835337068640669908635981260229917686259230791093938175180888561748453169349308673982663738487579285246952157425721, 60109806374614482820290666707663065747105619670023800831701670452641348968778676276052069973160882094868707492194463444555480365432058701923992271487269562822324049662444384315870349284982915790623645385965922606794679447286807111263887412420173542410054540473139959085996894299547843787707307042171541835603, 74957045291089689107548356922203808557174388038959874138957910249725448026943079257341007024711903288131114396044197310799822418156834278447179043044578743410847210826712545690679632245263386671859982237344989117173512421419681143447172305521745107099370030744496308674486483229713965680484382336754743087981]
e = 65537
c = 13106815051626678249752415156939731144015754719425065307574688399569549594622973499044294024312305957304981311871401801000165987879240146059201131278126452653960586384209286033024526926743619612940274502385280498531505962846023939209775526732987342373704403970051630413638349346132628254350462877597554028834

factors = [gcd(n[i], n[i+1]) for i in range(len(n)-1)]
factors.append(n[-1] // factors[-1])

m = c

for i in range(len(n)-1, -1, -1):
  p = factors[i]
  q = n[i] // p
  phi = (p-1) * (q-1)
  d = inverse(e, phi)
  m = pow(m, d, n[i])

flag = long_to_bytes(m)
print(flag.decode())