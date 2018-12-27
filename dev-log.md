# Notes

## 2018-12-27

Successful day of getting through Part 2. Part 2 seemed like a lot of administrivia-type stuff and general piping to get the project off the ground. Part 3 is looking quite encouraging and interesting.

Had a bit of a epiphany today when it really sunk in that the
Users service is a wholly separate service from the Exercises
service that is yet to be built. For my application, this will be
relevant when I create a Notes service. The Notes service will be
entirely separate from the Users service and the Notes service
will use the Users service to ensure only authorized users are
accessing the API. I'm looking forward to seeing how all this
works and fits together.

## 2018-12-21

New day. Fresh start. Starting with [Flask, SQLAlchemy and testing](https://spotofdata.com/flask-testing/).

Phew. Ok back up to a working place. The above article was exactly
what I needed to get back up and running. Now I can move on to
work stuff without thinking about how stupid I am.

Plus I feel like I understand the requisite objects required for
Flask-SQLAlchemy a bit better now.

On to Chapter 12 - Workflow at the next opportunity.

## 2018-12-20

Very frustrating day.

I thought I was just going to breeze through the chapter on Jinja
templating. How hard could it be, right? But no, of course not, instead
I run into every fucking error under the sun.

It's become clear that I don't understand Flask application contexts at
all. I have no idea what the fuck is going on under the hood. Of course,
all the tutorials use the outdated `unittest` instead of `pytest` which
means I have very little to go on in terms of examples. Both the
testdriven.io and Flask mega tutorials both use Flask's built-in support
for testing which I think originally supported just unittest, so they

just stuck with that. I don't know. It's all very confusing and now I
have to figure out what's going on with `pytest` scopes and the like.

Overall, very frustrating. Mostly because I had high hopes of busting
through two chapters, and instead I didn't even make it through one and
now everything is fucking broken and I don't know what to do to debug
it. 0 commits because I made 0 progress. GAH! Fuck!

That said. I have a couple leads. I think the following will be helpful:

* [Flask, SQLAlchemy and testing](https://spotofdata.com/flask-testing/)
* [Testing a Flask Application using pytest](https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/)

Start with the first. The second seems like he just sort of hacked it
to make it work.

## 2018-12-17

Three commands to remember for working with `docker-machine`.

1. `export GOOGLE_APPLICATION_CREDENTIALS=~/Credentials/remember-it-compute-engine.json`
2. eval $(docker-machine env auto-recall)
3. eval $(docker-machine env -u)

Ran into an issue of the docker-compose looking like it was getting
stuck on building the users services, but what was actually going on
was that I had somehow lost my `.dockerignore` file and docker was
trying to import all of the Python libraries. So, added that back and
it was fine.

To build and deploy to prod, run the following:

```bash
docker-machine env auto-recall-prod
eval $(docker-machine env auto-recall-prod)
```

Don't forget to `docker-machine kill auto-recall-prod` when done.

## 2018-12-11

In Chapter 10. Got up to the Gunicorn section.

## 2018-12-10

Got through Chapter 9. Tomorrow is deployment (Chapter 10). This is where it
gets interesting. I figure I will want to adapt the instructions for GCP
instead of AWS.

## 2018-12-07

Another issue with the tutorial I ran into today.

1. The test case `test_add_user_invalid_json_keys` does not pass
unless you add `username=username` to the filter on the query in the
`GET /users` route.

I'm now up to the *Get single user* section of the RESTful routes
chapter.

## 2018-12-06

A couple issues with the Flask-React tutorial.

1. `postgres` URL is deprecated, must use `postgresql`.
2. CLI commands have underscores changed to hyphens.

## 2018-12-05

Woo-hoo! Got it done. Officially got `pytest` integrated with the application.
All the same tests that were originally written with `unittest` are now written
and running in `pytest` with the expected results.

Spent some time brainstorming on a Notes API. This would be the core of the
Remember-It system. As usual, authentication is the first hurdle to overcome.

I'm thinking that I may try to tackle SSH-based encryption. I don't really know
how that works but it would be cool to find out.

In any case, I have a lot more to do with the Flask-React tutorial, and I can
get to work a little bit at a time on a Note API that will accept notes from
the user.

## 2018-12-04

Almost there with getting `pytest` set up to work in place of
`unittest`. Got `test_config.py` to work because there were no
dependencies or inheritance. `test_users.py` is a little more
complicated because it inherits from a `BaseTestCase` class that
contains some special function for testing.

Need to figure out the right way to set up PyTest Fixtures so
that they get called at the right time during testing. Once I do
that, I should be good to go.
