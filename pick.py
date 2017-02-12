import sys
import random


config_cats = {
    'answer': 'Your cat is: {}',
    'title': 'Please make your selection to get your Cat',
    'questions': {
        'Please enter your sex m/f: ': ['m', 'f'],
    },
    'data': {
        'm': ['rusu melynoji', 'abisinija'],
        'f': ['pudel', 'ziurke']
    }
}


config_dog = {
    'answer': 'Your dog is: {}',
    'title': 'Please make your selection to get your Dog',
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


available_configs = {
    'cats': config_cats,
    'dogs': config_dog,
    'default': config_dog
}


def main(config):
    result = config['data']
    print (config['title'])
    for question, allowed_values in config['questions'].items():
        while True:
            value = input(question).lower()
            if value in allowed_values:
               result = result[value]
               break

    item = random.choice(result)
    print (config['answer'].format(item))




if __name__ == "__main__":
    config = available_configs['default']
    if len(sys.argv) == 2:
        param = sys.argv[1]
        if param in available_configs:
            config = available_configs[param]

    main(config)
