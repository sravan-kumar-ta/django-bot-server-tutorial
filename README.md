# Django-bot-server

> Django based bot server that uses django-channels for  WebSockets connection.
> I forked this project from https://github.com/vaisaghvt/django-bot-server-tutorial

### Screen Casting  -> [Click here to View 📺](https://www.linkedin.com/posts/sravankumarta_chat-bot-source-code-httpslnkdingw9tduxw-activity-7027566697679130624-5f4t?utm_source=share&utm_medium=member_desktop)

## My contributions...:
* *Modify it instead of text-inputs to buttons*
* *Create models in Postgres database*
* *Store the number of calls per user*
* *Shows all calls made by the user*
* *Modify the database to add new bots from the database*


# getting started

To get this running, simply run the following 

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases


Create the databases using PostgreSQL with the credentials provided in the settings.py file and initial migrations with the following command:
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/chat/ and chat with the bot
