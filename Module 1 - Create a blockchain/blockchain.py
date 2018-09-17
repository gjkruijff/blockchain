#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a blockchain

Created on Mon Sep 17 06:36:42 2018

@author: gjkruijff
"""

# Import the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify       # Flask will be the web application 

# Part 1 -- building a blockchain 

class Blockchain: 
    
    def __init__(self): 
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        # block implemented as dictionary; why not as class?
        # why is there no hash for the block? how about the nonce? 
        block = {'index': len(self.chain) + 1, 
                 'timestamp': str(datetime.datetime.now()),
                  'proof' : proof,
                  'previous_hash' : previous_hash 
                  }     
        self.chain.append(block)
        return block

    # get the last block, not quite as general as "previous"
    def get_previous_block(self) : 
        return self.chain[-1] # return the last block in the chain 




# Part 2 -- mining the blockchain 
