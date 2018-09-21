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


    # Proof-of-Work: Hard to compute, easy to verify
    def proof_of_work(self, previous_proof): 
        new_proof = 1
        check_proof = False
        while (check_proof is False): 
            #arg for operation must be non-symmetrical
            #encode needed to add 'b' in front of string, required for sha256 input
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            # Check whether the result has 4 leading zeroes -- the number of 0's is the complexity 
            if hash_operation[:4] == '0000': 
                check_proof = True
            else: 
                new_proof += 1 
        return new_proof
            
    def hash(self, block): 
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    # Cycles over the entire chain, making two checks
    # stored previous hash is hash of previous block; proof is valid
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain): 
            block = chain[block_index]
            # Test 1: Stored previous hash equals the hash of the previous block 
            if block['previous'] != self.hash(previous_block): 
                return False 
            # Test 2: The proof of each block is valid
            previous_proof = previous_block['proof']
            proof = block['proof'] 
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000': 
                return False
            # All tests passed, advance block in the chain 
            previous_block = block 
            block_index += 1
        return True
        
    
        
        

# Part 2 -- mining the blockchain 
