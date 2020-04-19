#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:10:33 2020

@author: valerio_mellini
"""

"""
THEORY
we are going to solve a very simple system


1) First passage

x + y + z = 6
x + y = 5
z = 1
 
2) Matrix representation 

1 1 1 | x | 6
0 1 1 | y | 3
0 0 1 | z | 1

A = [[1,1,1],
     [0,1,1],
     [0,0,1]]

x = [x,
     y,
     z]

b = [6,
     3,
     1]

3) Solution

x = b / A
x = A inversa * b

"""

import tensorflow as tf
import numpy as np


A = tf.placeholder(tf.float32, shape=(None, None), name='A')
b = tf.placeholder(tf.float32, shape=(None, None), name='b')

#automatic calculus by tensorflow
automated_calc_x = tf.linalg.solve(A, b) 

#manual calculus
det = tf.linalg.det(A)
Ainv = tf.linalg.inv(A)
identity = tf.matmul(A, Ainv)
manual_calc_x = tf.matmul(Ainv, b)

with tf.Session() as sess:
    
    init = tf.global_variables_initializer()
    sess.run(init)
    
    feed_dict = {A: np.array([[1, 1, 1], [0,1,1], [0,0,1]]),
                 b: np.array([[6], [3], [1]])}
    
    # Variable evaluation
    automated_calc_x = automated_calc_x.eval(feed_dict=feed_dict)
    det = det.eval(feed_dict=feed_dict)
    Ainv = Ainv.eval(feed_dict=feed_dict)
    identity = identity.eval(feed_dict=feed_dict)
    
    print("""
          
          automated_calc_x      \n  {0}     \n\n
          det                   \n  {1}     \n\n
          AT                    \n  {2}     \n\n
          identity              \n  {3}     \n\n
          
          """.format(automated_calc_x , det, Ainv, identity))
      
    ris = sess.run(manual_calc_x , feed_dict=feed_dict) 
    print("RIS FROM manual_calc_x \n {0} \n".format(ris))
    print("'manual_calc_x' is equal to 'automated_calc_x'? {0}".format(np.array_equal(manual_calc_x, automated_calc_x)))
          
    
    
    
