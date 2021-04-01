from . import client

_client = client


def test_get_model(client):
    res = client.get("/models/alexnet")
    assert res.status_code == 200
    assert res.json() == {'model_name': 'alexnet', 'message': 'Deep Learning FTW!'}
