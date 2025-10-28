from itertools import combinations

# Input dataset (list of transactions)
dataset = [
    ['A', 'B', 'C'],
    ['A', 'C', 'D'],
    ['B', 'C', 'E'],
    ['A', 'B', 'C', 'E'],
    ['B', 'E']
]

print("Dataset:")
for i, t in enumerate(dataset, 1):
    print(f"Transaction {i}: {t}")

min_support = int(input("\nEnter minimum support count: "))

c2 = []
items = sorted({item for transaction in dataset for item in transaction})
for pair in combinations(items, 2):
    c2.append(pair)

support_count = {}
for pair in c2:
    count = sum(1 for transaction in dataset if set(pair).issubset(transaction))
    support_count[pair] = count

frequent_2_itemsets = {pair: count for pair, count in support_count.items() if count >= min_support}

print("\nCandidate 2-Itemsets with Support Count:")
for pair, count in support_count.items():
    print(f"{pair}: {count}")

print("\nFrequent 2-Itemsets (Support ≥", min_support, "):")
for pair, count in frequent_2_itemsets.items():
    print(f"{pair}: {count}")

if not frequent_2_itemsets:
    print("No frequent 2-itemsets found for the given support.")
    '''Theory:

The Apriori algorithm is a fundamental algorithm in data mining used to discover frequent itemsets in transactional datasets and to derive association rules.
It uses a bottom-up approach, where frequent subsets are extended one item at a time, and groups of candidates are tested against the dataset.

Key Concepts:

Itemset: A collection of one or more items.

Support: The number of transactions in which an itemset appears.

Frequent Itemset: An itemset whose support is greater than or equal to the user-defined minimum support count.

Apriori Property: All non-empty subsets of a frequent itemset must also be frequent.

Algorithm Steps:

Scan the dataset and find all possible 2-item combinations.

Count the support (occurrence) of each 2-itemset.

Compare each support count with the minimum support count.

Select and output those 2-itemsets whose support ≥ minimum support'''
