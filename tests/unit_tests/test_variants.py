import pytest
from UnleashClient.variants import Variants


VARIANTS = \
    [
        {
            "name": "VarA",
            "weight": 34,
            "payload": {
                "type": "string",
                "value": "Test1"
            },
            "overrides": [
                {
                    "contextName": "userId",
                    "values": [
                        "ivanklee86@gmail.com"
                    ]
                }
            ]
        },
        {
            "name": "VarB",
            "weight": 33,
            "payload": {
                "type": "string",
                "value": "Test 2"
            }
        },
        {
            "name": "VarC",
            "weight": 33,
            "payload": {
                "type": "string",
                "value": "Test 3"
            }
        }
    ]


@pytest.fixture()
def variations():
    yield Variants(VARIANTS, "TestFeature")


def test_variations_override_match(variations):
    override_variant = variations._apply_overrides({'userId': 'ivanklee86@gmail.com'})
    assert override_variant['name'] == 'VarA'


def test_variations_overrid_nomatch(variations):
    assert not variations._apply_overrides({'userId': 'ivanklee87@gmail.com'})


def test_variations_seed(variations):
    # Random seed generation
    context = {}
    seed = variations._get_seed(context)
    assert float(seed) > 0

    # UserId, SessionId, and remoteAddress
    context = {
        'userId': 'ivanklee86@gmail.com',
        'sessionId': '1',
        'remoteAddress': '1.1.1.1'
    }

    assert context['userId'] == variations._get_seed(context)
    del context['userId']
    assert context['sessionId'] == variations._get_seed(context)
    del context['sessionId']
    assert context['remoteAddress'] == variations._get_seed(context)


def test_variation_selectvariation_happypath(variations):
    variant = variations.select_variant({'userId': '2'})
    assert variant
    assert 'payload' in variant
    assert variant['name'] == 'VarC'


def test_variation_selectvariation_multi(variations):
    tracker = {}
    for x in range(100):
        variant = variations.select_variant({})
        name = variant['name']
        if name in tracker:
            tracker[name] += 1
        else:
            tracker[name] = 1

    assert len(tracker) == 3
    assert sum([tracker[x] for x in tracker.keys()]) == 100


def test_variation_override(variations):
    variant = variations.select_variant({'userId': 'ivanklee86@gmail.com'})
    assert variant
    assert 'payload' in variant
    assert variant['name'] == 'VarA'