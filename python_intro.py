#print('Hello, Django guys!')

# if 5 > 2:
#     print('5 is indeed greater than 2')
# else:
#     print('5 is not greater than 2')
#     

'''
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')
'''

# volume 값을 바꿔보세요
'''
volume = 20
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")
'''

def hi(name):
	print("Hi " + name + " ! ")

#hi("tykim")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls:
	hi(name)
	print('Next girl')
