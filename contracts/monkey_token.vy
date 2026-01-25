# pragma version 0.4.3
"""
@license MIT
@title Monkey Token
@author fooyay
@notice An example ERC20 token implemented in Vyper.
"""

from ethereum.ercs import IERC20
implements: IERC20

from snekmate.auth import ownable
from snekmate.tokens import erc20

initializes: ownable
initializes: erc20[ownable := ownable]

exports: erc20.__interface__

NAME: constant(String[25]) = "Monkey Token"
SYMBOL: constant(String[5]) = "MONK"
DECIMALS: constant(uint8) = 18
# NAME_EIP712: constant(String[50]) = "Monkey Token"
VERSION_EIP712: constant(String[20]) = "1"

@deploy
def __init__(initial_supply: uint256):
    ownable.__init__()
    # Note: Vyper 0.4.3 does not support named argument in __init__ calls
    erc20.__init__(
        NAME,               # name: String[25]
        SYMBOL,             # symbol: String[5]
        DECIMALS,           # decimals: uint8
        NAME,               # name_eip712_: String[50]
        VERSION_EIP712      # version_eip712_: String[20]
    )
    erc20._mint(msg.sender, initial_supply)
