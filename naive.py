
data = [
    ['sunny', 'no'],
    ['sunny', 'no'],
    ['overcast', 'yes'],
    ['rainy', 'yes'],
    ['rainy', 'yes'],
    ['rainy', 'no'],
    ['overcast', 'yes'],
    ['sunny', 'no'],
    ['sunny', 'yes'],
    ['rainy', 'yes'],
    ['sunny', 'yes'],
    ['overcast', 'yes']
]

total = len(data)
play_yes = sum(1 for row in data if row[1] == 'yes')
play_no = sum(1 for row in data if row[1] == 'no')

p_yes = play_yes / total
p_no = play_no / total

print("== Priors ==")
print(f"P(play=yes) = {p_yes:.4f}")
print(f"P(play=no)  = {p_no:.4f}\n")

outlooks = ['sunny', 'overcast', 'rainy']
counts_yes = {o: 0 for o in outlooks}
counts_no = {o: 0 for o in outlooks}

for row in data:
    outlook, play = row
    if play == 'yes':
        counts_yes[outlook] += 1
    else:
        counts_no[outlook] += 1

print("== Conditional Probabilities P(outlook | play=...) ==")
for o in outlooks:
    p_o_yes = counts_yes[o] / play_yes if play_yes != 0 else 0
    p_o_no = counts_no[o] / play_no if play_no != 0 else 0
    print(f"P({o} | yes) = {p_o_yes:.4f}\tP({o} | no) = {p_o_no:.4f}")
print()

outlook_input = input("Enter outlook (sunny/overcast/rainy): ").lower()

p_outlook_yes = (counts_yes[outlook_input] / play_yes) * p_yes if play_yes != 0 else 0
p_outlook_no = (counts_no[outlook_input] / play_no) * p_no if play_no != 0 else 0

print("\n== Posterior Numerators (unnormalized) ==")
print(f"P({outlook_input} | yes) * P(yes) = {p_outlook_yes:.6f}")
print(f"P({outlook_input} | no)  * P(no)  = {p_outlook_no:.6f}")

total_prob = p_outlook_yes + p_outlook_no
if total_prob > 0:
    p_yes_given_outlook = p_outlook_yes / total_prob
    p_no_given_outlook = p_outlook_no / total_prob
else:
    p_yes_given_outlook = p_no_given_outlook = 0

print("\n== Posterior (normalized) ==")
print(f"P(play=yes | {outlook_input}) = {p_yes_given_outlook:.6f}")
print(f"P(play=no | {outlook_input})  = {p_no_given_outlook:.6f}\n")


if p_yes_given_outlook > p_no_given_outlook:
    print(f"The players are NOT likely to play.")
else:
    print(f"The players are likely to play.")
'''The Naïve Bayes Classifier is a probabilistic classification algorithm based on Bayes’ Theorem.
It is called “naïve” because it assumes that the attributes (features) are independent of each other given the class label
'''