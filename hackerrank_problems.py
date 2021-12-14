#!/bin/python3

import math
import os
import random
import re
import sys

class HackerrankProblems():
    def __init__(self):
        pass        
        
    """
        Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
        INPUT string s: a time in 12 hour format
        RETURN string s: a time in 24 hour format
    """
    def timeConversion(self):
        return ('%02d%s') % ((int(self.time12[0:2]) % 12 + (12 if self.time12[-2:] == "PM" else 0)), self.time12[2:8])

    """
        You are in charge of the cake for a child's birthday. 
        You have decided the cake will have one candle for each year of their total age. 
        They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
        INPUT int candles[n]: the candle height
        RETURN int: the number of candles that are tallest
    """
    def birthdayCakeCandles(self):
        return self.candles.count(max(self.candles))

    """
        Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
        Then return the respective minimum and maximum values as a single line of two space-separated long integers.
        INPUT arr: an array of 5 integers
        RETURN two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.
    """
    def miniMaxSum(self):
        return [sum(self.minmaxsumarr)-max(self.minmaxsumarr),sum(self.minmaxsumarr)-min(self.minmaxsumarr)]

    """
        This is a staircase of size n :

        #
        ##
        ###
        ####

        Its base and height are both equal to n. The last line is not preceded by any spaces.

        Prints a staircase of size n.
        INPUT n: dimension of staircase
        PRINT STAIRCASE
    """
    def staircase(self):
        result = []
        for i in range(1,self.n+1):
            result.append(' '*(self.n-i)+'#'*(i))
        return '\n'.join(result)

    """
        Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
        INPUT arr: array to study
        PRINT  the following 3 lines, each to 6 decimals:
            1. proportion of positive values
            2. proportion of negative values
            3. proportion of zeros
    """
    def plusMinus(self):
        pos = list(filter(lambda num: num>0, self.arr))
        neg = list(filter(lambda num: num<0, self.arr))
        neu = list(filter(lambda num: num==0, self.arr))
        result = []
        result.append(format((len(pos)/len(self.arr)), '.6f'))
        result.append(format((len(neg)/len(self.arr)), '.6f'))
        result.append(format((len(neu)/len(self.arr)), '.6f'))
        return result

    """
        Given a square matrix, calculate the absolute difference between the sums of its diagonals.
        For example, the square matrix arr is shown below:
            1 2 3
            4 5 6
            9 8 9  
        The left-to-right diagonal = 1 + 5 + 9 = 15
        The right to left diagonal = 3 + 5 + 9 = 17
        Their absolute difference is abs(15 - 17) = 2.

        INPUT arr: square matrix to study
        RETURN the absolute difference between the sums of the matrix's two diagonals as a single integer.
    """
    def diagonalDifference(self):
        n = len(self.matrix)
        d1 = sum([self.matrix[x][x] for x in range(len(self.matrix))])
        d2 = sum([self.matrix[x][n - 1 - x] for x in range(len(self.matrix))])
        return (abs(d1 - d2))

    """
        INPUT int ar[n]: an array of integers .
        RETURN long: the sum of all array elements
    """
    def aVeryBigSum(self):
        res = 0
        for a in self.ar:
            res += a
        return res

    """
        Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: 
        problem clarity, originality, and difficulty.
        
        The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), 
        and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

        The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].
            If a[i] > b[i], then Alice is awarded 1 point.
            If a[i] < b[i], then Bob is awarded 1 point.
            If a[i] = b[i], then neither person receives a point.

        Comparison points is the total points a person earned.
        Given a and b, determine their respective comparison points.

        INPUT int a[3]: Alice's challenge rating
        INPUT int b[3]: Bob's challenge rating
        RETURN int[2]: Alice's score is in the first position, and Bob's score is in the second.
    """
    def compareTriplets(self):
        alice = 0;
        bob = 0;
        i = 0;
        while i < 3:
            if self.alice_triplets[i] < self.bob_triplets[i]:
                bob += 1
            elif self.bob_triplets[i] < self.alice_triplets[i]:
                alice += 1
            i +=1
        return [alice,bob]

    
    """
        INPUT
        RETURN
    """
    def simpleArraySum(self):
        sum = 0
        for i in self.ar:
            sum += i;
        return sum
       

    def createRandomParams(self) :
        self.time12 = '0'+str(random.randint(0,9))+':'+str(random.randint(0,5))+str(random.randint(0,9))+':'+str(random.randint(0,5))+str(random.randint(0,9))+'PM'
        self.candles = [random.randint(1,10) for i in range(4)]
        self.minmaxsumarr = [random.randint(-100,100) for i in range(random.randint(1,100))]
        self.n = random.randint(5,15)
        self.arr = [random.randint(-10,10) for i in range(random.randint(1,10))]
        self.ar = [random.randint(-10,10) for i in range(3)]
        self.alice_triplets = [random.randint(1,10) for i in range(3)]
        self.bob_triplets = [random.randint(1,10) for i in range(3)]
        self.matrix_dim = random.randint(1,10)
        self.matrix = [ 
            [random.randint(-100,100) for i in range(3)],
            [random.randint(-100,100) for i in range(3)], 
            [random.randint(-100,100) for i in range(3)]
        ]

    def printTest(self,method,input,output) :
        print('\n'+str(method).upper()+'\n\tinput:\t'+input+'\n\toutput:\t'+str(output))

    def launchTests(self) :
        output = self.timeConversion()
        self.printTest('timeConversion',str(self.time12),output)

        output = self.birthdayCakeCandles()
        self.printTest('birthdayCakeCandles','['+', '.join([str(x) for x in self.candles])+']',str(output))

        output = self.miniMaxSum()
        output = '['+', '.join([str(x) for x in output])+']'
        self.printTest('miniMaxSum','['+', '.join([str(x) for x in self.minmaxsumarr])+']',str(output))

        output = self.staircase()
        self.printTest('staircase of '+str(self.n)+' dimensions',str(self.n),'\n'+str(output))

        output = self.plusMinus()
        output = '['+', '.join([str(x) for x in output])+']'
        self.printTest('PLUSMINUS','['+', '.join([str(x) for x in self.arr])+']',str(output))

        output = self.diagonalDifference()
        self.printTest('diagonalDifference','['+', '.join([str('['+', '.join([str(y) for y in x])+']') for x in self.matrix])+']',str(output))
        
        output = self.aVeryBigSum()
        self.printTest('aVeryBigSum','['+', '.join([str(x) for x in self.ar])+']',str(output))
        
        output = self.compareTriplets()
        input = 'alice ['+', '.join([str(x) for x in self.alice_triplets])+'] & bob ['+', '.join([str(x) for x in self.bob_triplets])+']'
        output = '['+', '.join([str(x) for x in output])+']'
        self.printTest('compareTriplets',input,output)

        output = self.simpleArraySum()
        self.printTest('simpleArraySum','['+', '.join([str(x) for x in self.ar])+']',str(output))