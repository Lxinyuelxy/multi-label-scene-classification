import numpy as np
import h5py
from sklearn.model_selection import train_test_split

num_classes = 5
class_labels = ['desert', 'mountains', 'sea', 'sunset', 'trees']

def load_dataset():
    f = h5py.File('../dataset.h5', "r")
    X = np.array(f["X"][:])
    y = np.array(f["y"][:])
    x_train , x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=100)
    return x_train, x_test, y_train, y_test

if __name__ == '__main__':
    x_train, x_test, y_train, y_test = load_dataset()
    print('x_train.shape: ', x_train.shape)
    print('y_train.shape: ', y_train.shape)
    print('x_test.shape: ', x_test.shape)
    print('y_test.shape: ', y_test.shape)