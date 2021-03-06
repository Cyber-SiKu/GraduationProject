from numpy import zeros, tile, shape, mat, ones, nonzero

def read_data(file_name):
    '''
    read 2st data from filename
    :param file_name: file's name
    :return: power
    '''
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
    :param house_num: the number of home
    :param dev_num: the number of devices
    :return data_mat:  the compliant data
    :return label_mat: data_mat'label
    '''
    # MINI_INTERVAL = 1 #  TODO:not use
    file_path = "house_%d/channel_%d.dat" % (house_num, dev_num)
    data_arry = read_data(file_path)
    m = shape(data_arry)[0]
    delta = data_arry[1:m]-data_arry[0:m-1]
    data_mat = mat(delta[delta != 0])  # TODO: to use the condition >= MINI_INTERVAL or <= -MINI_INTERVAL
    m = shape(data_mat)[1]
    label_mat = mat(ones(m))
    return data_mat.transpose(), label_mat.transpose()


def test_digits(house_num, dev_num):
    '''
    test the accuracy of classify based on svm
            90% to train svm, 10% to test
            Todo : change rate 10%-10% -----> 90%-90% ---ok
    :return: the test error rate
    '''
    from numpy import vstack, hstack
    from sklearn.svm import SVC
    from sklearn.externals import joblib
    # TODO: train_rate should be    ----ok
    train_rate = 0.9 #  rate to train
    data, label = load_dev_data(1, 3)
    lenth = shape(data)[0]
    train_length = int(lenth * train_rate)
    train_data = data[0:train_length]
    train_label = label[0:train_length]
    # TODO: the test data should be  ----ok
    test_data = data[train_length:lenth]
    test_label = label[train_length:lenth]
    #for i in range(8, 10): # test channel 9, 10
    # TODO: for should be   ----ok
    for i in range(3, dev_num):  # train svm with the train_rata of data
        data, label = load_dev_data(house_num, i+1)  # tips： i start  at 0 so +1
        lenth = shape(data)[0]
        train_data = vstack((train_data, data[0: int(lenth*train_rate)]))
        train_label = hstack((train_label, label[0: int(lenth*train_rate)]))
        test_data = vstack((test_data, \
                            data[int(lenth*train_rate): int(2*lenth*train_rate)]))
        test_label = hstack((test_label, \
                            label[int(lenth * train_rate): int(2*lenth*train_rate)]))
    clf = SVC()
    clf.fit(train_data, train_label)  # train svm
    # TODO: save the train_model
    file_path = "house_%d/train_model.pkl" % house_num
    joblib.dump(clf, file_path)
    # test
    error_count = 0
    for i in range(shape(test_data)[0]):
        if abs(clf.predict([test_data[i]])[0] - test_label[i]) < 0.00001:
            error_count+=1
    print("the training error rate is: %f" % (float(error_count)/float(lenth)))
