import pyinputplus as pyip

while True:
    prompt = 'Wanna know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break
print('Exactly. Have a nice day :)')
