import numpy as np 
from data_handler import distributer
import re


def bernoulli_nbc(doc, ham, spam, n_ham, n_spam, dic):
    p_ham, p_spam = 1.0, 1.0
    for s in dic:
        if s in ham.keys(): 
            p_h = (ham[s]+1)/(n_ham+2)
        else:
            p_h = 1/(n_ham+2)
        if s in spam.keys():
            p_s = (spam[s]+1)/(n_spam+2)
        else:
            p_s = 1/(n_spam+2)
        if s in doc:
            p_ham *= p_h
            p_spam *= p_s
        else:
            p_ham *= (1-p_h)
            p_spam *= (1-p_s)
    t = max(p_ham, p_spam)
    if t == p_ham:
        return 'ham'
    elif t == p_spam:
        return 'spam'


if __name__ == "__main__":
    with open('SMSSpamCollection', 'r') as f:
        raw_data = f.read()
        f.close()
    raw_data = raw_data.strip()
    data = raw_data.split('\n')
    dic = re.findall(r"[\w']+", raw_data)

    # k-fold cross validation
    fold_size = 100
    acc = list()

    for i in range(0, len(data), fold_size):
        test_data = data[i:i+fold_size]
        train_data = data[0:i] + data[(i+fold_size):]
        if len(test_data)<30:
            break
        # Bernoulli Naive Bayesian distributions
        ham_ber, _, spam_ber, _, n_ham, n_spam = distributer(train_data)
        f_acc = list()
        for t in test_data:
            row = re.findall(r"[\w']+", t)
            truth = row[0]
            c_map = bernoulli_nbc(row[1:], ham_ber, spam_ber, n_ham, n_spam, dic)
            if c_map == truth:
                f_acc.append(1)
                acc.append(1)
            else:
                f_acc.append(0)
                acc.append(0)
            
        print('Accuracy for episode {} is: {}'.format(i/fold_size, sum(f_acc)/len(f_acc)))
            
    print('Final Accuracy for fold size {} is: {}'.format(fold_size, sum(acc)/len(acc)))

