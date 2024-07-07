
number = int(float(input('Enter a number: ')))

if number % 2 == 0:
    print(number, ' is even number')
else:
    print(number, ' is odd number')


indian = ['samosa', 'daal', 'naan']
chinese = ['egg roll', 'pot sticker', 'fried rice']
italian = ['pizza', 'paste', 'risotto']

dish = input('Enter your favourite cuisine --> ')
if dish in indian:
    message = 'You have entered an Indian dish'
    print(message)
elif dish in chinese:
    message = 'You have entered a Chinese dish'
    print(message)
elif dish in italian:
    message = 'You have entered an Italian dish'
    print(message)
else:
    print('Based on the little knowledge I have, I do not know which cuisine is burger')

