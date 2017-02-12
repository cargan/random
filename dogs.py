import random


config_dog = {
    'questions': {
        'Please enter your sex m/f: ': ['m', 'f'],
        'Please enter short/long hair, s/l: ': ['s', 'l'],
        'Please enter your age 0-7, 8-18, 19+; 1/2/3: ': ['1', '2', '3']
    },
    'data': {
        'm': {
            'l': {
                '1': ['spaniel', 'koker spaniel'],
                '2': ['spaniel'],
                '3': ['koker spaniel'],
            },
            's': {
                '1': ['ryzenas', 'huskis'],
                '2': ['huskis'],
                '3': ['ryzenas']
            }
        },
        'f': {
            'l': {
                '1': ['pudel', 'ziurke'],
                '2': ['ziurke'],
                '3': ['pudel'],
            },
            's': {
                '1': ['dvarniaska', 'baltapukis'],
                '2': ['dvarniaska'],
                '3': ['baltapukis']
            }
        }
    }
}


def main(config):
    result = config['data']
    for question, allowed_values in config['questions'].items():
        while True:
            value = input(question).lower()
            if value in allowed_values:
               result = result[value]
               break

    dog = random.choice(result)
    print ('Your dog is: {dog}'.format(dog=dog))



if __name__ == "__main__":
    main(config_dog)
