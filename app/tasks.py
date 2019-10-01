from redis import Redis
from rq import Queue
from . import db, app
from .models import Git
import requests
from rq_scheduler import Scheduler
from redis import Redis
from rq import Queue
from datetime import datetime

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

def update_db(url):

    req = requests.get(url, headers={'Authorization': 'token {}'.format(app.config['GIT_KEY'])})  # Make request to GitHub API
    result = req.json()             # Serve response as JSON

    repos = {}                      # Hold temporary results pulled from Gituhb
    listy = []                      # List holds info for each repo, represented as dict(s) in a List

    for x in result:
        # Extract data needed
        repos['name'] = x['name']
        repos['description'] = x['description']
        repos['created_at'] = x['created_at']
        repos['size'] = x['size']
        repos['language'] = x['language']
        repos['last_updated'] = x['updated_at']
        repos['repo_url'] = x['svn_url']
        listy.append(repos)

    git = Git.query.all()                                           # Query entire database to be compared with new Git results

    count=0

    for x in git:                                                   # Once each repo has been pulled
        if x.repo_name == listy[count]['name']:                             # if db val == git api val
            if x.description !=  listy[count]['description']:       # if git val has changed then update db
                x.description = listy[count]['description']
                db.session.commit()
                print(x.repo_name + ' description updated')
            elif x.created_at != listy[count]['created_at']:
                x.created_at = listy[count]['created_at']
                db.session.commit()
                print(x.repo_name + ' created_at updated')
            elif  x.size != listy[count]['size']:
                x.size = listy[count]['size']
                db.session.commit()
                print(x.repo_name + ' size updated')
            elif x.language != listy[count]['language']:
                x.language = listy[count]['language']
                db.session.commit()
                print(x.repo_name + ' language updated')
            elif x.last_updated != listy[count]['last_updated']:
                x.last_updated = listy[count]['last_updated']
                db.session.commit()
                print(x.repo_name + ' last_updated updated')
            elif x.repo_url != listy[count]['repo_url']:
                x.repo_url = listy[count]['repo_url']
                db.session.commit()
                print(x.repo_name + ' repo_url updated')
            else:
                print('No updates made!')

        count += 1
    db.session.close()
    

q = Queue(connection=Redis())              # Setup Queue
scheduler = Scheduler(connection=Redis())

#initial_insert_job = scheduler.schedule(
  # scheduled_time=datetime.utcnow(),
   # func=insert_db,
   # args=[url],
   # repeat=0
#)

job = scheduler.schedule(                                     # Make DB calls every 30 minutes
    scheduled_time=datetime.utcnow(),
    args=[url],
    func=update_db,
    interval=1800)   
print('Job enqueued', job)

# list_of_job_instances = scheduler.get_jobs() View running jobs