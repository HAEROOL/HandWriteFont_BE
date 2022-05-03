API endpoints
=============

Basic
-----

- /dj-rest-auth/login/ (POST)

    - username(optional)
    - email
    - password

    Returns Token key
    ```
    {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXN~",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl9~",
        "user": {
            "pk": "admin@admin.com",
            "email": "admin@admin.com"
        }
}
    ```

- /dj-rest-auth/logout/ (GET)
    ```
    {
        "detail": "로그아웃되었습니다."
    }
    ```
- /dj-rest-auth/password/change/ (POST)

    - new_password1
    - new_password2
    ```
    {
    "detail": "새로운 패스워드가 저장되었습니다."
    }
    ```

    .. note:: ``OLD_PASSWORD_FIELD_ENABLED = True`` to use old_password.
    .. note:: ``LOGOUT_ON_PASSWORD_CHANGE = False`` to keep the user logged in after password change

Login 되어 있을 때 본인을 반환함
- /dj-rest-auth/user/ (GET, PUT, PATCH)

    - email

    Returns pk, email


- /dj-rest-auth/token/verify/ (POST)

    - token

    Returns an empty JSON object.

    .. note:: ``REST_USE_JWT = True`` to use token/verify/ route.
    .. note:: Takes a token and indicates if it is valid.  This view provides no information about a token's fitness for a particular use. Will return a ``HTTP 200 OK`` in case of a valid token and ``HTTP 401 Unauthorized`` with ``{"detail": "Token is invalid or expired", "code": "token_not_valid"}`` in case of a invalid or expired token.


- /dj-rest-auth/token/refresh/ (POST) (`see also <https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage>`_)

    - refresh

    Returns access

    .. note:: ``REST_USE_JWT = True`` to use token/refresh/ route.
    .. note:: Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid. ``HTTP 401 Unauthorized`` with ``{"detail": "Token is invalid or expired", "code": "token_not_valid"}`` in case of a invalid or expired token.

Registration
------------

- /dj-rest-auth/registration/ (POST)

    - username
    - email
    - password1
    - password2
    - profile_image
    - NickName
