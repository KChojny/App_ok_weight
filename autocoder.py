from random import randrange, choice


#główne funkcje liczące indeksy

#funkcja body mass index - wskaźnik masy ciała
def BMI(mass, height):
	return (mass / (height / 100) ** 2)

#funkcja body adiposity - wskaźnik otłuszczenia ciała
def BAI(height, hips):
	return ((100 * (hips / 100)) / ((height / 100) * (height / 100) ** 0.5) - 18)

#funkcja waist-height ratio - stosunek talia-wzrost
def WHTR(height, waist):
	return (waist / height * 100)

#funkcja waist-hip ratio - stosunek talia-biodra
def WHR(waist, hips):
	return (waist / hips)

# funkcja metody YMCA
def YMCA(mass, circumference, gender):
	if(gender == 'male'):
		index = 98.42
	else:
		index = 76.76
	return ((1.634 * circumference - 0.1804 * mass - index) / (2.2 * mass) * 100)

#funkcje korygujące wartości indeksów pod funkcje standaryzujące
#funkcje robiące przesuniecia ze względu na wiek czy płeć

#funkcja korygyjąca wartość BMI
def XBMI(mass, height, age):
	num_age = (min(age, 64) - 15) // 10
	return (BMI(mass, height)) - num_age

#funkcja korygująca wartość BAI
def XBAI(height, hips, age, gender):
	num_age= (min(age, 79) - 20) // 20
	num_gender = (12 if gender == 'female' else 0)
	return BAI(height, hips) - num_age - num_gender

#funkcja korygująca wartość WHTR
def XWHTR(height, waist, gender):
	num = WHTR(height, waist)
	if(gender == 'female' or num <= 47.5):
		return num
	elif(num >= 53):
		return (num + 4)
	else:
		return ((num - 46) * 3 / 7 + 46)

#funkcja korygująca wartość WHR
def XWHR(waist, hips, gender):
	num_gender = (0.2 if gender == 'female' else 0)
	return (WHR(waist, hips) + num_gender)

#funkcja korygująca wartość YMCA
def XYMCA(mass, circumference, age, gender):
	num_age = (min(age, 79) - 20) // 20
	num_gender = (12 if gender == 'female' else 0)
	return YMCA(mass, circumference, gender) - num_age - num_gender



#funkcje walidujące indeksy uwzględniające wiek i płeć i standaryzowane pod jednakową ocene sylwetki
#wartości: 0 - skrajna niedowaga, 1 - prawidłowa waga, 2 - skrajna otyłość
#wszystkie indeksy  są w zakresie od 0 do 2, prócz WHR jest od 0 do 1
#będą 2 indeksy YMCA: masa i obwód pasa, masa i obwód talii

#funkcja standaryzowanej wartości BMI
def STD_BMI(mass, height, age):
	bmi = XBMI(mass, height, age)
	std_bmi = 1
	if(bmi >= 40):
		std_bmi = 2
	elif(bmi >= 30):
		std_bmi = 1.5 + (bmi - 30) * 0.1
	elif(bmi >= 25):
		std_bmi = 1.25 + (bmi - 25) * 0.05
	elif(bmi >= 21.75):
		std_bmi = 1 + (bmi - 21.75) * (1 / 13)
	elif(bmi >= 18.5):
		std_bmi = 0.75 + (bmi - 18.5) * (1 / 13)
	elif(bmi >= 17):
		std_bmi = 0.5 + (bmi - 17) * (1 / 6)
	elif(bmi >= 16):
		std_bmi = (bmi - 16) * 0.5
	else:
		std_bmi = 0
	return std_bmi

#funkcja standaryzacji wartości BAI
def STD_BAI(height, hips, age, gender):
	bai = XBAI(height, hips, age, gender)
	std_bai = 1
	if(bai >= 27):
		std_bai = 2
	elif(bai >= 21):
		std_bai = 1.25 + (bai - 21) * 0.125
	elif(bai >= 15):
		std_bai = 1 + (bai - 15) * (1 / 24)
	elif(bai >= 9):
		std_bai = 0.75 + (bai - 9) * (1 / 24)
	elif(bai >= 3):
		std_bai	= (bai - 3) * 0.125
	else:
		std_bai = 0
	return std_bai

#funkcja standaryzacji wartośći WHTR
def STD_WHTR(height, waist, gender):
	whtr = XWHTR(height, waist, gender)
	std_whtr = 1
	if(whtr >= 58):
		std_whtr = 2
	elif(whtr >= 54):
		std_whtr = 1.5 + (whtr - 54) * 0.125
	elif(whtr >= 49):
		std_whtr = 1.25 + (whtr - 49) * 0.05
	elif(whtr >= 47.5):
		std_whtr = 1 + (whtr - 47.5) * (1 / 6)
	elif(whtr >= 46):
		std_whtr = 0.75 + (whtr - 46) * (1 / 6)
	elif(whtr >= 42):
		std_whtr = 0.5 + (whtr - 42) * (1 / 16)
	elif(whtr >= 35):
		std_whtr = (whtr - 35) * (1/12)
	else:
		std_whtr = 0
	return std_whtr

#funkca standaryzacji wartości WHR
def STD_WHR(waist, hips, gender):
	whr = XWHR(waist, hips, gender)
	whr = max(min(whr,1.5),0.5)
	return abs((whr - 1) * 2)

#funkcja standaryzacji wartości YMCA
def STD_YMCA(mass, circumference, age, gender):
	ymca = XYMCA(mass, circumference, age, gender)
	std_ymca = 1
	if(ymca >= 27):
		std_ymca = 2
	elif(ymca >= 21):
		std_ymca = 1.25 + (ymca - 21) * 0.125
	elif(ymca >= 15):
		std_ymca = 1 + (ymca - 15) * (1 / 24)
	elif(ymca >= 9):
		std_ymca = 0.75 + (ymca - 9) * (1 / 24)
	elif(ymca >= 3):
		std_ymca = (ymca - 3) * 0.125
	else:
		std_ymca = 0
	return std_ymca



#funkcje kwalifikujące osoby i grupy osób poprzez wiliczone indeksy
#funkcja sprawdzająca kwalifikującą osobę
#funkcja wypisuje wszsytkie indeksy w celu sprawdzania ich poprawności
def PERSON_RATING():
	print('Wpisz wagę w kg')
	mass = int(input())

	print('Wpisz wzrost w cm')
	height = int(input())

	print('Wpisz obwód talii w cm')
	waist = int(input())

	print('Wpisz obwód bioder w cm')
	hips = int(input())

	print('Wpisz wiek')
	age = int(input())

	print('Wpisz płeć: male, female')
	gender = input()

	print('')

	print('BMI')
	print(round(BMI(mass, height), 2))
	print(round(STD_BMI(mass, height, age), 2))

	print('BAI')
	print(round(BAI(height, hips), 2))
	print(round(STD_BAI(height, hips, age, gender), 2))

	print('WHTR')
	print(round(WHTR(height, waist), 2))
	print(round(STD_WHTR(height, waist, gender), 2))

	print('WHR')
	print(round(WHR(waist, hips), 2))
	print(round(STD_WHR(waist, hips, gender), 2))

	print('YMCA - waist')
	print(round(YMCA(mass, waist, gender), 2))
	print(round(STD_YMCA(mass, waist, age, gender), 2))

	print('YMCA - hips')
	print(round(YMCA(mass, hips, gender), 2))
	print(round(STD_YMCA(mass, hips, age, gender), 2))

	print('')
	print('Twoja klasyfikacja')
	clas = PERSON_CLAS(mass, height, waist, hips, age, gender)
	mark = ''
	if(clas < 2.5):
		mark = 'Jesteś wygłodzony'
	elif(clas < 3.75):
		mark = 'Masz niedowagę'
	elif(clas < 6.25):
		mark = 'Masz odpowiednią wagę'
	elif(clas < 8):
		mark = 'Masz nadwagę'
	else:
		mark = 'Jesteś otyły'
	print(round(clas, 2))
	print(mark)


#funkcja kwalifikująca osobę
def PERSON_CLAS(mass, height, waist, hips, age, gender):
	return STD_BMI(mass, height, age) + STD_BAI(height, hips, age, gender) + STD_WHTR(height, waist, gender) + STD_WHR(waist, hips, gender) + STD_YMCA(mass, waist, age, gender) + STD_YMCA(mass, hips, age, gender)

#funkcja oceny grupy
def GROUP_RATING(persons, ok_weight, not_ok_weight, below_ok_weight, emaciation, underweight, above_ok_weight, overweight, obesity):
	mark = ''
	if(ok_weight >= (0.9 * persons)):
		mark += 'Bardzo dobra ocena grupy w ocenie wagi\nPonad 90% osób w grupie ma prawidłową wagę\n'
	elif(ok_weight >= (0.7 * persons)):
		mark += 'Dobra ocena grupy w ocenie wagi\nPonad 70% osób w grupie ma prawidłową wagę\n'
	elif(ok_weight >= (0.5 * persons)):
		mark += 'Dostateczna ocena grupy w ocenie wagi\nPonad 50% osób w grupie ma prawidłową wagę\n'
	else:
		mark += 'Zła ocena grupy w ocenie wagi\nPoniżej 50% osób w grupie ma prawidłową wagę\n'

	if(below_ok_weight > above_ok_weight):
		mark += 'Więksość osób z nieprawidłową wagą jest poniżej normy\n'
		if(emaciation > underweight):
			mark += 'Większość osób z poniżej normy jest wygłodzona\n'
		elif(emaciation < underweight):
			mark += 'Większość osób z poniżej normy ma niedowagę\n'
		else:
			mark += 'Większość osób jest wygłodzona lub ma niedowagę\n'

	elif(below_ok_weight < above_ok_weight):
		mark += 'Więksość osób z nieprawidłową wagą jest powyżej normy\n'
		if(obesity > overweight):
			mark += 'Większość osób z powyżej normy jest otyła\n'
		elif(obesity < overweight):
			mark += 'Większość osób z powyżej normy ma nadwagę\n'
		else:
			mark += 'Większość osób jest otyła lub ma nadwagę\n'

	else:
		mark += 'Więkość osób ma problemy z niedowagą lub ma nadwagą\n'

	return mark

#funkcja klasyfikująca grupę
def GROUP_CLAS(persons):
	list = []
	for x in range(persons): #nadanie losowych wartości
		mass = randrange(30, 150, 1)
		height = randrange(150, 210, 1)
		waist = randrange(50, 150, 1)
		hips = randrange(50, 150, 1)
		age = randrange(15, 100, 1)
		gender = choice(['male', 'female'])
		clas = PERSON_CLAS(mass, height, waist, hips, age, gender)
		list.append(clas)

	list.sort()
	#liczba osób z danym wynikiem
	emaciation = len([x for x in list if x <= 2.5])
	underweight =  len([x for x in list if x <= 3.75 and x >= 2.5])
	ok_weight =  len([x for x in list if x <= 6.25 and x >= 3.75])
	overweight =  len([x for x in list if x <= 8 and x >= 6.25])
	obesity =  len([x for x in list if x >= 8])
	below_ok_weight = emaciation + underweight
	above_ok_weight = overweight + obesity
	not_ok_weight = below_ok_weight + above_ok_weight

	mark = GROUP_RATING(persons, ok_weight, not_ok_weight, below_ok_weight, emaciation, underweight, above_ok_weight, overweight, obesity)

	print(
f'''
Ilość osób w grupie: {persons}

Ilość osób z prawidłową wagą: {ok_weight}
Ilość osób z nieprawidłową wagą: {not_ok_weight}

Klasyfikacja nieprawidłowości

-poniżej normy: {below_ok_weight}
--wygłodzenie: {emaciation}
--niedowaga: {underweight}

-powyżej normy: {above_ok_weight}
--nadwaga: {overweight}
--otyłość: {obesity}

{mark}
'''
	)

#początek programu
while(True):
	print(
f'''
PROGRAM OCENIANIA WAGI DLA OSOBY LUB GRUP
1 - ocena wagi dla osoby
2 - ocena wagi dla grupy osób
3 - wyjście
'''
)

	x = input()
	if(x == '1'):
		PERSON_RATING()
		continue
	elif(x == '2'):
		print('Wpisz ile ma być ludzi w grupie')
		num = int(input())
		GROUP_CLAS(num)
		continue
	elif(x == '3'):
		break
