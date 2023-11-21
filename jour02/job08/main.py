print(""" 
Veuillez entrer les longueurs des 3 côtés 
(en séparant ces valeurs à l'aide de virgules) :""") 
a, b, c = eval(input()) 
 
if a < (b+c) and b < (a+c) and c < (a+b) : 
	print("Ces trois longueurs déterminent bien un triangle.") 
else: 
	print("Il est impossible de construire un tel triangle !") 
	exit()		
  
f = 0 
if a == b and b == c : 
	print("Ce triangle est équilatéral.") 
	f = 1 
elif a == b or b == c or c == a : 
	print("Ce triangle est isocèle.") 
	f = 1 
if a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b : 
	print("Ce triangle est rectangle.") 
	f = 1 
if f == 0 : 
	print("Ce triangle est quelconque.")