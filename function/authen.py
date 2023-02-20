
def session_login():
    id_token = flask.request.json['idToken']
    expires_in = datetime.timedelta(days=5)
    try:
        session_cookie = auth.create_session_cookie(id_token, expires_in=expires_in)
        response = flask.jsonify({'status': 'success'})
        expires = datetime.datetime.now() + expires_in
        response.set_cookie(
            'session', session_cookie, expires=expires, httponly=True, secure=True)
        return response
    except exceptions.FirebaseError:
        return flask.abort(401, 'Failed to create a session cookie')

def profit():
    prof = ()
    prof = prof + ('OUE1','OUE2','OUE3')
    return prof

def patch():
    prof = ()
    prof = prof + ('CHERRY1','CHERRY2','CHERRY3')
    return prof
