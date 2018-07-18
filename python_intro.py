i = 10

if i > 0 :
    print("Hello Django Girls.")


def hi(name):
    print('Hi ' + name + '!')

hi('Ola')
hi('Sonja')
hi('Me')

girls = ['Rachel', 'Monica', 'Poebe', 'Ola', 'You']

for name in girls:
    hi(name)

for i in range(1, 6):
    print(i)
