# -*- coding: utf-8 -*-

import chainer
import chainer.chain
import chainer.functions as F
import chainer.links as L

import numpy as np

class DQN(Chain):
    def __init__(self, n_actions)