# pragma version 0.4.3
"""
@license MIT
@title Monkey Token
@author fooyay
@notice An example ERC20 token implemented in Vyper.
"""



from snekmate.auth import ownable

initializes: ownable

@deploy
def __init__():
    ownable.__init__()
    
