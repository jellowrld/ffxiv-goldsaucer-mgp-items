n='Angel Wings'
m='Gold Paper Parasol'
l='Manderville Barding'
k='False Spectacles'
j='Gambler Barding'
i='Lexen Tails'
h='Great Lengths'
g='Curls'
f='Pony Tails'
e='Mama Automaton'
d='Unlucky Rabbit'
c='Piggy'
b='Wind-Up Nero tol Scaeva'
a='Heavy Hatchling'
Z='Black Coeurl'
Y='Zu Hatchling'
X='Water Imp'
W='/sheathe'
V='/draw'
U='Bees Knees'
T='Gold Dance'
S='Thav Dance'
R='/biggrin'
Q='Blackjack Identification Key'
P='Sabotender Emperador Horn'
O='Fenrir Horn'
N='Typhon Horn'
M='Korpokkur Kolossus Horn'
L='Archon Throne'
K='Pod 602 Identification Key'
J='Adamantoise Whistle'
D='Total:\t{:,}'
C='MGP'
B=sum
A=print
E={J:200000,K:300000,L:750000,M:750000,N:750000,O:1000000,P:2000000,Q:4000000}
F={R:20000,S:80000,T:80000,U:80000,V:100000,W:100000}
G={X:10000,Y:10000,Z:20000,a:20000,b:30000,c:30000,d:30000,e:30000}
H={f:8000,g:9600,h:30000,i:50000}
I={j:20000,k:100000,l:150000,m:200000,n:500000}
all={J:200000,K:300000,L:750000,M:750000,N:750000,O:1000000,P:2000000,Q:4000000,R:20000,S:80000,T:80000,U:80000,V:100000,W:100000,X:10000,Y:10000,Z:20000,a:20000,b:30000,c:30000,d:30000,e:30000,f:8000,g:9600,h:30000,i:50000,j:20000,k:100000,l:150000,m:200000,n:500000}
def o():A('Gold Saucer Item Lookup');A('---------------');A('Hello there!');A()
def p():A('Which would you like to view?');A('-----------------------------');A('Mounts:\t\tDisplays list of mounts and their MGP cost');A('Emotes:\t\tDisplays list of emotes and their MGP cost');A('Minions:\tDisplays list of minions and their MGP cost');A('Hair:\t\tDisplays list of hairstyles and their MGP cost');A('Others:\t\tDisplays list of other things and their MGP cost');A('Total:\t\tDisplays combined total of all GS items');A('Exit:\t\tExit program');A()
def q(mounts):
	E=mounts
	for(F,G)in E.items():A(f"{F}:\t{G}")
	A(D.format(B(E.values())),C)
def r(emotes):
	D=emotes
	for(E,F)in D.items():A(f"{E}:\t{F}")
	A('Total:\t\t{:,}'.format(B(D.values())),C)
def s(minions):
	E=minions
	for(F,G)in E.items():A(f"{F}:\t{G}")
	A(D.format(B(E.values())),C)
def t(hairstyles):
	E=hairstyles
	for(F,G)in E.items():A(f"{F}:\t{G}")
	A(D.format(B(E.values())),C)
def u(others):
	E=others
	for(F,G)in E.items():A(f"{F}:\t{G}")
	A(D.format(B(E.values())),C)
def v(all):
	for(B,C)in all.items():A(f"{B}:\t{C}")
def w(mounts,emotes,minions,hairstyles,others):D=B(mounts.values());D+=B(emotes.values());D+=B(minions.values());D+=B(hairstyles.values());D+=B(others.values());A('Grand total: {:,}'.format(D),C)
def x():
	o()
	while True:
		p();B=input('Command: ')
		if B.lower()=='mounts':q(E)
		elif B.lower()=='emotes':r(F)
		elif B.lower()=='minions':s(G)
		elif B.lower()=='hair':t(H)
		elif B.lower()=='others':u(I)
		elif B.lower()=='total':v(all);w(E,F,G,H,I)
		elif B.lower()=='exit':break
		else:A('Invalid command\n')
		A()
	A('GG, Have Fun farming.')
if __name__=='__main__':x()
