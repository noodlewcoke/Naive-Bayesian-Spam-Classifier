import numpy as np 
import re

# with open('SMSSpamCollection', 'r') as f:
#     raw_data = f.read()
#     f.close()

# data = raw_data.split('\n')

# counter = 0
# for i in range(len(data)):
#     D = data[i*counter: i*counter+50]
#     for row in D:
#         d = re.findall(r"[\w']+", row)
#         print(d)
#         t, s = d[0], d[1:]
#         print(t, s)
#         break
#     break
#     counter += 50


def distributer(data):
    # data = raw_data.split('\n')
    v_count = 0
    ham_multi, spam_multi = dict(), dict()
    ham_ber, spam_ber = dict(), dict()
    n_ham, n_spam = 0, 0
    for i,row in enumerate(data):
        d = re.findall(r"[\w']+", row)
        if d[0]=='ham':
            n_ham += 1

            for j in set(d[1:]):
                if not j in ham_multi.keys(): 
                    ham_multi[j]=0
                else:
                    ham_multi[j]+=1
                if not j in ham_ber.keys():
                    ham_ber[j]=1
                else:
                    ham_ber[j] += 1
                if not j in spam_multi.keys(): 
                    spam_multi[j]=0
                if not j in spam_ber.keys():
                    spam_ber[j]=0
        elif d[0]=='spam':
            n_spam += 1
            for j in set(d[1:]):
                if not j in spam_multi.keys(): 
                    spam_multi[j]=0
                else:
                    spam_multi[j]+=1
                if not j in spam_ber.keys():
                    spam_ber[j]=1
                else:
                    spam_ber[j] += 1
                if not j in ham_multi.keys(): 
                    ham_multi[j]=0
                if not j in ham_ber.keys():
                    ham_ber[j]=0
    return ham_ber, ham_multi, spam_ber, spam_multi, n_ham, n_spam
    #     else:
    #         print('Incorrect ifelse for row: {}'.format(row))
    # print(ham_ber['until'])


if __name__ == '__main__':
    with open('SMSSpamCollection', 'r') as f:
        raw_data = f.read()
        f.close()
    raw_data = raw_data.strip()
    distributer(raw_data)