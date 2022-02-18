import numpy as np
from scipy.stats import beta
import random
import pandas as pd
from initData import initData
from matplotlib import pyplot as plt 
from getData import getData
from sklearn.decomposition import TruncatedSVD
from recommendSimilar import recByItem
from recByUser import recByUser


def BeginRecommend(userNum):
    ones, zeros, ctr = initData()


    # 초기화 데이터 시각화 
    ones = ctr
    ones = np.sort(ones)
    dic = {}
    for i in ones:
        try:
            dic[i] += 1
        except KeyError:
            dic[i] = 1
    # print(list(dic.keys()))
    # print(list(dic.values()))


    user_ratings, ratings_data = getData(ctr)
    # print(user_ratings, ratings_data)
    
    # 비슷한 아이템 추천 (특정 게시물과 유사한 게시물) 
    recByItemList= recByItem(user_ratings)
    print(recByItemList)
    
    userNum= 237
    recNum = 10
    userHistory, recByUserList = recByUser(user_ratings,ratings_data, userNum, recNum)

    print(f'아이템기반 추천 리스트: {recByItemList}')
    print(f'사용자 히스토리 기반 추천 리스트: {recByUserList}')
    print(f'유저 히스토리: {userHistory}')

    return recByItemList, recByUserList



def init():
    initData()

if __name__ == '__main__':
    main()
    # init()