# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
raw_primary = []
raw_secondary = []

with open('Data_RS126.txt', 'r') as f:
    for count, line in enumerate(f, start=1):
        if count % 2 == 0:
            raw_secondary.append(line.strip())
        else:
            raw_primary.append(line.strip())

print ("Struktur Protein Primer : " ,len(raw_primary))
print ("Struktur Protein Sekunder: " ,len(raw_secondary))

for i in range(len(raw_secondary)):
    len1 = len(raw_secondary[i])
    len2 = len(raw_primary[i])
    
    if(len1 != len2):
        print(i," ", raw_secondary[i]," ",raw_primary[i])

raw_primary.pop(109)
raw_secondary.pop(109)

count_sec = 0
count_pri = 0
for i in range(len(raw_secondary)):
    len1 = len(raw_secondary[i])
    len2 = len(raw_primary[i])
    count_sec += len1
    count_pri = count_pri + len2
    if(len1 != len2):
        print(i," ", raw_secondary[i]," ",raw_primary[i])
        
print("count secondary structure (label): ",count_sec)
print("count primary structure (fitur) : ",count_pri)

def split(sequence): 
    return [char for char in sequence]  

split_primary = []
split_secondary = []
for i in range(len(raw_primary)):
    split_primary.append(split(raw_primary[i]))
    split_secondary.append(split(raw_secondary[i]))

def orthogonal_pri(arg):
    switch = {
        'A' : np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
        'C' : np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
        'E' : np.array([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
        'D' : np.array([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
        'G' : np.array([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
        'F' : np.array([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
        'I' : np.array([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]),
        'H' : np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]),
        'K' : np.array([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]),
        'M' : np.array([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]),
        'L' : np.array([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]),
        'N' : np.array([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]),
        'Q' : np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]),
        'P' : np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]),
        'S' : np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]),
        'R' : np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]),
        'T' : np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]),
        'W' : np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]),
        'V' : np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]),
        'Y' : np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
    }
    
    return switch.get(arg)

def orthogonal_sec(arg):
    switch = {
        'H' : 0,
        'C' : 1,
        'E' : 2
    }
    
    return switch.get(arg)
for i in range(len(split_primary)):  
    seq = split_primary[i]
    for j in range(len(seq)):
        seq[j] = orthogonal_pri(seq[j])
for i in range(len(split_secondary)):  
    seq2 = split_secondary[i]
    for j in range(len(seq2)):
        seq2[j] = orthogonal_sec(seq2[j])
def target(lis):
    Y = []
    for i in range(len(lis)):
        for j  in range(len(lis[i])):
            Y.append(lis[i][j])
    return Y
y_label = target(split_secondary)
len(y_label)

def window_padding_data(size, sequence):
    num = int(size/2)
    zeros = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(len(sequence)):
        for j in range(num):
            sequence[i].append(zeros)
            sequence[i].insert(0, zeros)
            
    X = []
    temp = []

    for k in range(len(sequence)):
        for l in range(len(sequence[k])-(size-1)):
            temp = sequence[k][l:l+size]
            X.append(temp)
            temp = []

    return X
X = window_padding_data(15,split_primary)
len(X)

X = np.array(X)
y_label = np.array(y_label)
X = X.reshape(22594,15*20)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y_label, test_size = 0.10)

from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train, y_train)

from sklearn.model_selection import GridSearchCV

# defining parameter range

clf_ = SVC(kernel='rbf')
C = [0.1, 1, 10, 100, 1000]
Gamma = [1, 0.1, 0.01, 0.001, 0.0001]
grid = GridSearchCV(clf_,
            dict(C=C,
                 gamma=Gamma),
                 cv=5,
                 pre_dispatch='1*n_jobs',
                 n_jobs=1,refit = True,verbose=3)

# fitting the model for grid search
grid.fit(X_train, y_train)

print(grid.best_params_)
  
# print how our model looks after hyper-parameter tuning
print(grid.best_estimator_)

print(grid.cv_results_)

