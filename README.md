# InputPowertools
> Eliminate the annoyances of getting input or building a cli in python!
## Prolog
I love using **c**ommand **l**ine **i**nterfaces and I think most people like building these small tools as well, but its really annoying to have to build the interface between the user and your program, hence I build this python package to take care of this part for you.
## Examples
### Intro
#### input()
##### Alpha
```
>>> print(f"Result: {input('Type your name:', Mode.ALPHA)}")

Type your name:  >? 123
🛑 Please enter a value that is completely alphabetic (no punctuation, numbers, emojis or nothing)...
Type your name:  >? Malte
Result: Malte
```
##### Numeric
```
>>> print(f"Result: {input('How old are you:', Mode.NUMERIC, domain=lambda x: x % 1 == 0)}")

How old are you:  >? 😀
🛑 Please enter a number...
How old are you:  >? 13.5
🛑 Please enter a value that fits the answers domain...
How old are you:  >? 16
Result: 16
```
##### Options
```
>>> print(f"Result: {input(
    'Are you a what kind of person are you?',
     Mode.OPTIONS,
     options=['Cat person', 'Dog person', 'Bird person']
)}")

Are you a what kind of person are you? 
1 -> Cat person
2 -> Dog person
3 -> Bird person
Select option [1-3]:  >? Though question
🛑 Please enter a number...
Select option [1-3]:  >? 0
🛑 Please enter a value that fits the answers domain...
Select option [1-3]:  >? 4
🛑 Please enter a value that fits the answers domain...
Select option [1-3]:  >? 2
Result: (1, 'Dog person')
```
#### Defaults
##### Just pressing enter
```
>>> print(f"Result: {input('Type your name:', Mode.ALPHA, default='Hannes')}")

Type your name: (Hannes) >? 
Result: Hannes
```
##### Typing something else
```
>>> print(f"Result: {input('Type your name:', Mode.ALPHA, default='Hannes')}")

Type your name: (Hannes) >? Malte
Result: Malte
```
#### Confirm
```
>>> print(f"Result: {input('Type your name:', Mode.ALPHA, confrim=True)}")

Type your name:  >? Malte
Do you want to select "Malte"? 
1 -> yes
2 -> no
Select option [1-2]: (2) >? 1
Result: Malte
```

