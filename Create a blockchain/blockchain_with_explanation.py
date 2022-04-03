# Create a Blockchain
# To be initialized:
# Flask==0.12.2: pip install==0.12.2
# Importing the libraries
#from base64 import encode
#Please note it won't run it's just for explanation
import datetime
import hashlib
import json
#from tabnanny import check
#from urllib import response
from flask import Flask, jsonify
# Part-1:Building A Blockchain


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')
        # we create a block what would we their in the blocks

    # whenever a block is created then it needs a to check wether the block is right or wrong
    def create_block(self, proof, previous_hash):
        # by the help of proof work and by the help of previous hash previous block is checked i.e., it is connected to right one or not
        block = {'index': len(self.chain)+1,  # A block variable is created and it is defined by 4 keys or
                 # we can say a dictionary is created for the block.// index is there to provide the number of the block and it is moved by +1
                 # It will give us the exact date and time when the block is created by the help
                 'timestamp': str(datetime.datetime.now()),
                 # of "datetime" library we take datetime module and from that we use now()func. to give time it is to be kept in string
                 'proof': proof,  # We will be solving a proof of work to check the block
                 'previous_hash': previous_hash}  # It will tell the adress of the previous block
        # we will append/add the chain i.e., single blocks
        self.chain.append(block)
        return block
        # we create previous block to access whenever needed

    def get_previous_block(self):
        # here it is '-1' because 'chain-1' will be the last block
        return self.chain[-1]
        # proof of work->
        # we create a problem so that miners may solve and then they may mine the block the question is mainly hard to solve but
        # #easy to veify

    def proof_of_work(self, previous_proof):
        # here 1 is taken beacuse as we know nonce is arbitrary (i.e., miners guess that only)
        new_proof = 1
        # so whenever the proof will be wrong then it will be incremented by +1 it will be mainly trial and error approach
        check_proof = False  # we will be checking here wether the proof is right or wrong
        # and it is initiallised to false because we don't know wether the proof is right or wrong so we assume it to be wrong
        # and when the proof will be right then by the help of loop we will set it to true
        while check_proof is False:
            # here we will give a problem to miners they will solve it and mine the block
            # and here by providing the libraries the output will be in 64 digits i.e., hexadigit 0-1 and a-f
            hash_operation = hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()
            # if the hash has four leading zeores then it will be right
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1  # if it is wrong then new_proof is incremented by +1
                return new_proof
    # here we will input a blocks and we will return the output in sha256

    def hash(self, block):
        # we took json.dumps not directly dumps because we need the ans in string
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    # here we will check wether the blocks are linked with their correct blocks or not
    def is_chain_valid(self, chain):#we will take 2 arguments
        previous_block= chain[0]#this is the first block of our chain so we initialise it with 0
        block_index=1#as we can see in the dictionary of blockchain that index starts with 1 so we initialised it with 1
        while block_index<len(chain):
            block=chain[block_index]#here we get the current block
            if block['previous_hash']!=self.hash(previous_block):#here we are checking the if previous hash of current block is not equal to the hash of previous block
                return False
                previous_proof=previous_block['proof']#here we are giving the proof of previous block by the index 
                proof=block['proof']#we get the proof of current block
                hash_operation = hashlib.sha256(str(proof**2-previous_proof**2).encode()).hexdigest()#it is the problem to be solved by miner
                if hash_operation[:4]!='0000':
                    return False #else
                    previous_block=block #make previous_block current block and iterate it and block index by 1
                    block_index+=1
                    return True

                    #Part 2:- MINING OUR BLOCKCHAIN
                    #Creating a web app
                    app = Flask(__name__) #we imported flask and written on top on line 9 and by writing these lines we made a web app (https://flask.palletsprojects.com/en/1.1.x/quickstart/)
                     
                    #Creating A Blockchain
                    blockchain = Blockchain() 

                    #Mining a new block
                    @app.route('/mine_block', methods=['GET'])#it is a decorator it is a address/URL where the block will be mined(full URL IS http://127.0.0.1:5000/mine_block)
                    def mine_block():
                        previous_block=blockchain.get_previous_block()#here we accessed our previous block for previous proof for the new proof 
                        previous_proof=previous_block['proof']#here we accessed previous proof from previous block
                        proof=blockchain.proof_of_work(previous_proof)#here we get the new block proof and we wrote previous_proof as argument 
                        #because it takes previous proof as argument to solve the riddle i.e., new_proof-previous_proof
                        previous_hash=blockchain.hash(previous_block)#we accessed our previous hash from our previous block
                        block = blockchain.create_block(proof,previous_hash)#as we accessed proof and previous_hash so as we created a func. to create a block i.e., create_block where 
                        #arguments were proof and previous_hash hence we created a block and it returns block check line 21
                        response = {'message':'congratulations you mined a block',
                                    'index':block['index'],
                                    'timestamp':block['timestamp'],
                                    'proof':block['proof'],
                                    'previous_hash':block['previous_hash']}
                        return jsonify(response) , 200   
                    #Getting The full blockchain
                    @app.route('/get_chain', methods=['GET'])
                    def get_chain():
                        response = {'chain': blockchain.chain,
                                    'length':len(blockchain.chain)}
                        return jsonify(response) , 200  
                    #Running the app
                    app.run(host = '0.0.0.0',port=5000)

                                 






                 

