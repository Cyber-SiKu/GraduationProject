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
    TODO: there not delete the data which is >= MINI_INTERVAL or <= -MINI_INTERVAL
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

