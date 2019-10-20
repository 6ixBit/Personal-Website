# Personal-Website [![build](https://circleci.com/gh/6ixBit/Personal-Website.svg?style=shield)](https://circleci.com/gh/6ixBit/Personal-Website)
My Personal website built with Flask and hack.css (hackcss.egoist.moe)

Tech Stack:

- Flask
- CircleCI 
- Docker 
- Redis (RQ server) - To update Git repos every hour on /projects route
- Postgres - Store repo data pulled from GItHub 

# Run
1. Activate virtual env using: source venv/bin/activate on your terminal
2. set environment varibale if not running with Docker. export flask_app=run.py
2. enter flask run in your terminal
