for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key,value,end="  ""\n")
# zip
questions = ['name', 'colour', 'shape']
answers = ['beer', 'gold', 'a circle']
for question, answer in zip(questions, answers):
    print('What is your {0}?  I am {1}.'.format(question, answer))
#  items()
Aarth = {'Abhi': 'The Coder', 'mahesh': 'The chillar',
        'venky': 'The thopper'}
for key, value in Aarth.items():
    print(key, value)

# sorted()
lis = [1, 3, 5, 6, 2, 1, 3,23]
for i in sorted(lis):
    print(i, end=" ")
print("\n")
# use of set() removes duplicates.
for i in sorted(set(lis)):
    print(i, end=" ")
# reversed
for i in reversed(range(1, 23, 3)):
    print(i)