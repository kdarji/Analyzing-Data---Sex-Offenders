__author__ = 'new'


import csv
import unittest
from HW2 import Offender_list
from HW2 import main



#Testing name
class unitTesting(unittest.TestCase):

    def GenderTest(self):
        i = Offender_list()
        self.assertNotEqual(Offender_list())
        self.assertNotEqual(i[0], 'MALE')
        self.assertNotEqual(i[0], 'FEMALE')

    def AgeTest(self):
        i = Offender_list()
        self.assertNotEqual(Offender_list())
        self.assertNotEqual(i[1], [19]-[65])

    def RaceTest(self):
        i = Offender_list()
        self.assertNotEqual(Offender_list())
        self.assertNotEqual(i[0], 'BLACK', 'WHITE', 'HISPANIC', 'ASIAN', )

unittest.main()