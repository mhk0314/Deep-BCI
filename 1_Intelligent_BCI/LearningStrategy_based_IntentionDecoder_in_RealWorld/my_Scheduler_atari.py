
import gym
import time
from psychopy import visual, core, event, monitors
from psychopy.hardware import keyboard
import time
import numpy as np
from scipy import io
import os
import math
import numpy as np
import itertools
import random

def block_permut(num_of_gameType = 3, num_eachGame = 2):

    DAY_SESSION = []

    len_sess = num_eachGame * num_of_gameType

    ### initialize : 112233 ###
    for game_type in range(num_of_gameType) :
        for i in range(num_eachGame) :
            DAY_SESSION.append(game_type+1)

    ### permutation :
    # in random order with the one constraint of never playing the same game twice in a row  ###

    cand_list = []
    random.seed(2021)
    for t in range(100):  # make session candidates # 100
        res = random.sample(DAY_SESSION, len(DAY_SESSION))
        if res not in cand_list:
            flag = 0
            for i in range(len(res)):
                try:
                    if res[i] == res[i + 1]:
                        flag = 1
                except:
                    # print("last")
                    ''
                if flag == 1:
                    break
            if flag == 0 :
                cand_list.append(res)

    return cand_list

