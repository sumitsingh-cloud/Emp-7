# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 08:49:37 2026

@author: user
"""

class Base:
    def show(self):
        print("Statement from base class")

class Derived(Base):
    def show(self):
        super().show()
        print("Satement from derived class ")


ob=Derived()
ob.show()
ob.show()