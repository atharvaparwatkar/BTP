from rouge import Rouge

hypothesis = []
reference = []

with open('result.txt', 'r') as f:
    for line in f:
        hypothesis.append(line.rstrip('\n'))
    f.close()
i = 0
with open('sumdata/train/valid.title.filter.txt', 'r') as f:
    for line in f:
        if i < 10:
            reference.append(line.rstrip('\n'))
        i = i + 1
    f.close()

rouge = Rouge()
scores = []
for h, r in zip(hypothesis, reference):
    scores.append(rouge.get_scores(h, r))

rouge1 = []
rouge2 = []
rougel = []
for score in scores:
    rouge1.append(score[0]['rouge-1']['f'] * 100)
    rouge2.append(score[0]['rouge-2']['f'] * 100)
    rougel.append(score[0]['rouge-l']['f'] * 100)
print("Rouge-1: " + str(sum(rouge1) / len(rouge1)))
print("Rouge-2: " + str(sum(rouge2) / len(rouge2)))
print("Rouge-l: " + str(sum(rougel) / len(rougel)))
