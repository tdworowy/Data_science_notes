import pandas as pd
import pyfpgrowth as fp

'''Frequent Pattern Growth Algorithm '''

transaction_set = {
    'id': [0, 1, 2, 3],
    'items': [['wickets', 'pads'],
              ['bat', 'wickets', 'pads', 'helmet'],
              ['helmet', 'pad'],
              ['bat', 'pads', 'helmet']]
}


def generate_rules(data: pd.DataFrame, support_threshold: int = 1, confidence_threshold: float = 0.3) -> tuple:
    patterns = fp.find_frequent_patterns(data['items'], support_threshold=support_threshold)
    rules = fp.generate_association_rules(patterns, confidence_threshold=confidence_threshold)

    return patterns, rules


if __name__ == '__main__':
    transaction_set = pd.DataFrame(transaction_set)
    patterns, rules = generate_rules(transaction_set)

    print('Patterns:')
    for key, value in patterns.items():
        print(f'{key}: {value}')

    print('Rules')
    for key, value in rules.items():
        print(f'{key}: {value}')
