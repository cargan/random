import random


config_dog = {
    'm': {
        'l': {
            1: ['spaniel', 'koker spaniel'],
            2: ['spaniel'],
            3: ['koker spaniel'],
        },
        's': {
            1: ['ryzenas', 'huskis'],
            2: ['huskis'],
            3: ['ryzenas']
        }
    },
    'f': {
        'l': {
            1: ['pudel', 'ziurke'],
            2: ['ziurke'],
            3: ['pudel'],
        },
        's': {
            1: ['dvarniaska', 'baltapukis'],
            2: ['dvarniaska'],
            3: ['baltapukis']
        }
    }
}


def main():
    sex = None
    while True:
        sex = input('Please enter your sex m/f: ').lower()
        if sex in ['m', 'f']:
           break

    hair = None
    while True:
        hair = input('Please enter short/long hair, s/l: ').lower()
        if hair in ['s', 'l']:
           break

    age = None
    while True:
        age = int(input('Please enter your age 0-7, 8-18, 19+; 1/2/3: '))
        if age in [1, 2, 3]:
           break

    dog = random.choice(config_dog.get(sex).get(hair).get(age))
    print ('Your dog is: {dog}'.format(dog=dog))



if __name__ == "__main__":
    main()
