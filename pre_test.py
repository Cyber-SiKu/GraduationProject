'''
TODO:  2.  test the accuracy of classify based on svm \
            90% to train svm, 10% to test
            at first use 10 to train for quickly
'''
from numpy import mat, shape

def read_data(file_name):
    '''
    read 2st data from filename
    :param file_name: file's name
    :return: power
    '''
    from numpy import zeros
    fr = open(file_name)
    array_lines = fr.readlines()
    number_lines = len(array_lines)
    return_mat = zeros(number_lines)
    index = 0
    for line in array_lines:
        line = line.strip()
        list_line = line.split(' ')
        return_mat[index] = list_line[1]
        index += 1
    return return_mat


def load_dev_data(house_num=1, dev_num=9):
    '''
    load data from file "house_%d/channel_%d.dat" % (house_num, dev_num)
    calculate delta(change data) as data[i+1] - data[i],\
    at the asame time remove the non-compliant data
    TODO: to delete the data which is >= MINI_INTERVAL or <= -MINI_INTERVAL
    :param house_num: the number of home
    :param dev_num: the number of devices
    :return data_mat:  the compliant data
    :return label_mat: data_mat'label
    '''
    from numpy import ones
    # MINI_INTERVAL = 1 #  TODO: use the number to filter data
    file_path = "house_%d/channel_%d.dat" % (house_num, dev_num)
    data_arry = read_data(file_path)
    m = shape(data_arry)[0]
    delta = data_arry[1:m]-data_arry[0:m-1]
    data_mat = mat(delta[delta != 0])
    m = shape(data_mat)[1]
    label_mat = mat(dev_num * ones(m))
    return data_mat.transpose(), label_mat

def test_digits():
    '''
    test the accuracy of classify based on svm
            90% to train svm, 10% to test
            Todo : change rate 10%-10% -----> 90%-90%
    :return: the test error rate
    '''
    from numpy import ravel, vstack, hstack, array
    from sklearn.svm import SVC
    from sklearn.externals import joblib
    dev_numders = 20    # the number of devices
    train_rate = 0.01
    # TODO: train_rate should be
    # train_rate = 0.9 #  rate to train
    data, label = load_dev_data(1, 8)
    lenth = shape(data)[0]
    train_data = data[0:int(lenth * train_rate)]
    train_label = label[:, 0:int(lenth * train_rate)]
    # follw two lines just test for quickly
    test_data = data[int(lenth * train_rate): int(2 * lenth * train_rate)]
    test_label = label[:, int(lenth * train_rate): int(2 * lenth * train_rate)]
    # TODO: the test data should be
    # test_data = vstack((test_data, data[int(lenth*train_rate): lenth]))
    # test_label = hstack(test_label, label[int(lenth*train_rate): lenth])
    for i in range(8, 10): # test channel 9, 10
    # TODO: for should be
    # for i in range(2, dev_numders):  # train svm with the train_rata of data
        data, label = load_dev_data(1, i+1)  # tips： i start  at 0 so +1
        lenth = shape(data)[0]
        train_data = vstack((train_data, data[0: int(lenth*train_rate)]))
        train_label = hstack((train_label[0], label[:, 0: int(lenth*train_rate)]))
        # follw two lines just test for quickly
        test_data = vstack((test_data, \
                            data[int(lenth*train_rate): int(2*lenth*train_rate)]))
        test_label = hstack((test_label, \
                            label[:, int(lenth * train_rate): int(2*lenth*train_rate)]))
        # TODO: the test data should be
        # test_data = vstack((test_data, data[int(lenth*train_rate): lenth]))
        # test_label = hstack(test_label, label[int(lenth*train_rate): lenth])
    clf = SVC()
    clf.fit(train_data, ravel(train_label))  # train svm
    # TODO: save the train_model
    # joblib.dump(clf, 'train_model.pkl')
    # test
    error_count = 0
    for i in range(shape(test_data)[0]):
        if abs(clf.predict(test_data[i])[0] - array(test_label)[0][i]) < 0.00001:
            error_count+=1
    print("error: %f" % (float(error_count)/float(lenth)))

