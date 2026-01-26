from eth_utils import to_wei  # type: ignore
from moccasin.boa_tools import VyperContract  # type: ignore

from contracts import monkey_token  # type: ignore

INITIAL_SUPPLY = to_wei(1_000_000, "ether")


def deploy() -> VyperContract:
    monkey_contract = monkey_token.deploy(INITIAL_SUPPLY)
    print(f"Deployed MonkeyToken at {monkey_contract.address}")
    return monkey_contract


def moccasin_main() -> VyperContract:
    return deploy()
