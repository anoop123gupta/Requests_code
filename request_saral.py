import requests
import json

def course_list():
		url="http://saral.navgurukul.org/api/courses"
		req=requests.get(url)
		data=req.json()
		num=1
		for i in data:
			for j in data[i]:
				print(num,j['name'])
				num+=1
# course_list()


def course_id():
	id_list=[]
	url="http://saral.navgurukul.org/api/courses"
	req=requests.get(url)
	data=req.json()
	for i in data:
		for j in data[i]:
			id_list.append(j['id'])
	return(id_list)
# course_id()

# user=int(input("Enter a number of courses "))
def name_of_data(user):
	a=course_id()
	b=len(a)
	# print(b)
	number_list=[]
	for i in range(1,b+1):
		number_list.append(i)
	# print(number_list)

	for i in number_list:
		if i==user:
			pre=a[i-1]
			# print(pre)
			api=requests.get('http://saral.navgurukul.org/api/courses/'+str(pre)+'/exercises')
			# print(api)
			api_data=api.json()
			# print(api_data)
			
			for i in api_data:
				num=1
				for j in api_data[i]:
					# print(j)
					print(num,j['name'])
					num+=1
					child=j['childExercises']
					for m in child:
						print('	',m['name'])
						# num+=1
# name_of_data(user)

def menu(user):  # slug 
	a=course_id()
	b=len(a)
	# print(b)
	number_list=[]
	slug_list=[]
	for i in range(1,b+1):
		number_list.append(i)
	# print(number_list)

	for i in number_list:
		if i==user:
			pre=a[i-1]
			# print(pre)
			api=requests.get('http://saral.navgurukul.org/api/courses/'+str(pre)+'/exercises')
			# print(api)
			api_data=api.json()
			# print(api_data)
			
			for i in api_data:
				num=1
				for j in api_data[i]:
					# print(j)
					slug_list.append(num)
					slug_list.append(j['slug'])
					num+=1
				# print(slug_list)
				child=j['childExercises']
				for m in child:
					slug_list.append(num)
					slug_list.append(m['slug'])
					num+=1
	return(slug_list)
# menu(user)
# user0=int(input("input any number you want open content"))
def content(user0,choice):
	a=course_id()
	z=menu(user)
	# print(z)
	b=len(a)
	# print(b)
	number_list=[]
	slug_list=[]
	for i in range(1,b+1):
		number_list.append(i)
	# print(number_list)

	for i in number_list:
		if i==user0:
			pre=a[i-1]
	find=menu(user)
	# print(find)
	
	for i in range(len(find)):
		if choice == find[i]:
			new= requests.get("http://saral.navgurukul.org/api/courses/"+str(pre)+"/exercise/getBySlug?slug="+find[i+1])
			# print(new)
			t=new.json()
			print(t['content'])
# content(user,user0)


course_list()
print('')
user = int(input("any number you want chek course "))
name_of_data(user)
print('')
choice=int(input("input any number you want open content "))
content(user,choice)
Next = choice
while True:

	what=input("Enter n/p/up  ")
	if what=='up':
		course_list()
		print('')
		user = int(input("any number you want chek course "))
		name_of_data(user)
		print('')
		choice=int(input("input any number you want open content "))
		content(user,choice)

	elif what=='n':
		content(user,Next+1)
		Next+=1

	elif what=='p':
		content(user,Next-1)
		Next-=1
	else:
		break