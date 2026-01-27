from script.deploy import deploy, INITIAL_SUPPLY


import boa




RANDOM_USER = boa.env.generate_address("random_user")
def test_deploy_token():
    monkey_token = deploy()

    assert monkey_token.totalSupply() == INITIAL_SUPPLY


def test_token_emits_events():
    monkey_token = deploy()
    with boa.env.prank(monkey_token.owner()):
        monkey_token.transfer(RANDOM_USER, INITIAL_SUPPLY)
        logs = monkey_token.get_logs()
        first_log = logs[0]
        assert len(logs) == 1
        assert type(first_log).__name__ == "Transfer"
        assert first_log.address == monkey_token.address
        assert first_log.sender == monkey_token.owner()
        assert first_log.receiver == RANDOM_USER
        assert first_log.value == INITIAL_SUPPLY
        assert monkey_token.balanceOf(RANDOM_USER) == INITIAL_SUPPLY
