from users.apis import Register, Login, UserDetails


urls = [
    ('/user/register', Register),
    ('/user/login', Login),
    ('/', UserDetails)
]
