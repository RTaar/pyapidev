from app import schemas
from . database import client, session


def test_root(client):
    res = client.get('/')
    print(res.json().get('message'))
    assert res.json().get('message') == 'I\'M A LIVE!'
    assert res.status_code == 200


def test_create_user(client):
    res = client.post('/users/', json={
        'email': 'ttt@gmail.com',
        'password': 'password'
    })

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'ttt@gmail.com'
    assert res.status_code == 201


def test_login_user(client):
    res = client.post('/login/', data={
        'username': 'ttt@gmail.com',
        'password': 'password'
    })
    print(res.json())
    assert res.status_code == 200
