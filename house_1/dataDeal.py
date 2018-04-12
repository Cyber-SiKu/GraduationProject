#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy


def readData(fileName):
    '''
    从文件中读取数据
    :param fileName:文件名
    :return: Mat 二维数组 [:,0]-t [:,1]-value
    '''
    fr = open(fileName)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = numpy.zeros((numberOfLines, 2))
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split(' ')
        returnMat[index, :] = listFromLine[0:2]
        index += 1
    # 使下标从零开始
    vector = numpy.tile((returnMat[0, 0]), (numberOfLines))
    returnMat[:, 0] = returnMat[:, 0] - vector
    return returnMat


def plotShow(dataMat, start, number):
    '''
    绘制图像
    :param dataMat:要被绘图的数据[:, 0]-x  [:, 1]-y
    :param start:要显示数据的其实位置
    :param number:要显示的数量
    :return: null
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[start:number, 0], dataMat[start:number, 1])
    return plt


def readDataPlatShow():
    str = input("请输入文件名：")
    datMat = readData(str)
    plt = plotShow(datMat, 0, 1000)
    plt.show()