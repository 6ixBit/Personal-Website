from .app import db, app
from .models import Git

url = 'https://api.github.com/users/6ixbit/repos?direction=desc'

def insert_db(url):
    req = requests.get(url, headers={'Authorization': 'token {}'.format(app.config['GIT_KEY'])})
    result = req.json()

    repos = {}

    for x in result:
        git = Git()    # Instance to connect to database model class

        # Extract data needed
        repos['name'] = x['name']
        repos['description'] = x['description']
        repos['created_at'] = x['created_at']
        repos['size'] = x['size']
        repos['language'] = x['language']
        repos['last_updated'] = x['updated_at']
        repos['repo_url'] = x['svn_url']

        # Dict values are passed into DB model object
        git.repo_name = repos['name']
        git.description = repos['description']
        git.created_at = repos['created_at']
        git.size = repos['size']
        git.language = repos['language']
        git.repo_url = repos['repo_url']
        git.last_updated = repos['last_updated']

        # Commit to DB
        db.session.add(git)
        db.session.commit()
        db.session.close()
        print('Data points inserted')

    return repos

insert_db(url)         # Pre-populate DB upon deployment