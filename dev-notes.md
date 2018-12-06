# Notes

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
