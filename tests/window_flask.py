from window_flask import create_app

def test_import():
    assert window_flask

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_intro(client):
    response = client.get('/')
    assert reponse.status_code == 200
    assert b'<h1>A Knock At The Window</h1>'' in response.data
    assert b'<h2>Intro</h2>' in response.data

def test_bedroom(client):
    response = client.get('/bedroom')
    assert reponse.status_code == 200
    assert b'<h1>A Knock At The Window</h1>'' in response.data
    assert b'<h2>Bedroom</h2>' in response.data
