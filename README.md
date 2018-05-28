# multi-label-scene-classification

This repo is focus on multi-labbel scene classification and gives 2 methods. The dataset is from [here](https://suraj-deshmukh.github.io/Multi-Label-Image-Classification/).

## construct a deep learning model
This solution is mainly from [here](https://github.com/suraj-deshmukh/Multi-Label-Image-Classification), and I managed to
modify something like optimizer. But Essentially, this solution transformed multi-label  classification into binary classification.

Accuracy| Value
------- |-----
Hamming Loss| 0.139 
Subset Accuracy(Exact Match)| 0.52375

## use resnet50 model as image feature extractor
In this solution, the trained model resnet50 from keras is used as image feature extractor. Then these features are inputed to multi-label algorithms(like Classifer Chains, Random k-Labelsets, etc.)The main reason why I choose 
resnet50 is because the output dimension of other models is too high (like VGG16 or VGG19 has 1\*7\*7\*512). The output dimension
of resnet50 is just 1\*1\*1\*2048.

Accuracy |Binary Relevance|Calibrated Label Ranking| Random k-Labelsets| MLKNN
---------|-------------|----------|------|------
Hamming Loss| 0.065500 | 0.067000 | 0.058000 | 0.066500
Subset Accuracy| 0.720000 | 0.717500 | 0.762500 | 0.740000
