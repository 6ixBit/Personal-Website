from .app import insert_db

url = 'https://api.github.com/users/6ixbit/repos?direction=desc'

insert_db(url)