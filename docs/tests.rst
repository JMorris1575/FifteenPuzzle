.. _developing_tests:

################
Developing Tests
################

Looking at the :ref:`detailed overview <detailed_overview>` in the planning document, Here are three areas for testing
so far derived from that document:

#. The authentication process
#. Initial appearance and functionality of the Entry Page
#. Game play functionality, including tests for solving the puzzle

*******************************
Authentication Testing Part One
*******************************

Since I don't know how to do authentication in Django 5.0, and learning it is one of the reasons I started this project,
it is providential that this topic naturally comes up first.

First Thoughts
==============

But I also don't know how to test for proper authentication. Here are some guesses as to what needs to be done with only
a tiny bit of peeking at the functional tests from the book:

#. Check to see if the login page appears when entering the base url of the site (*localhost:8000* for development.)
#. Have the test user enter their username and password and check to see if the main site opens.
#. Check to see that the main site does not open for an incorrect username.
#. Check to see that the main site does not open for an incorrect password.

Ideas from the Book
===================

There is no authentication in the book but he does show how to test at least arriving at the website. That is probably
where I should start. Here is my first planned test::

    def test_authentication(self):

        # Charlie has decided to try out the Fifteen Puzzle program and goes to its homepage
        self.browser.get(self.live_server_url)

        # He comes to a login page
        self.assertIn('Login', self.browser.title)

There is considerably more that needs to be done to set up even that test but I will save that for later.

Preparation for My First Test
=============================

Based on what the author did gradually over several chapters of the text, here is what I need to do:

#. Install Django 5.0. (It insalled version 5.0.1)
#. Install Selenium. (It installed version 4.16.0)
#. Start a django project in my FifteenPuzzle directory following the same conventions I do for the Christmas website.
   (Don't create the fifteen app until later however. It was just easier to show the whole file structure here.)::

    FifteenPuzzle
        └───fifteen24
            ├───config
            │   └───settings
            │       ├───settings
            │       │   └───base.py  dev.py  prod.py  secrets.json
            │       └───asgi.py  settings  urls.py  views.py  wsgi.py
            ├───fifteen
            │   ├───migrations
            │   │   └───__pycache__
            │   ├───static
            │   │   └───fifteen
            │   └───templates
            │       └───fifteen
            ├───functional_tests
            │   ├───init.py
            │   └───tests.py
            └───manage.py

#. Create a *functional_tests* directory in the same folder as *manage.py* as shown above.
#. Create the *tests.py* testing program within the *functional_tests* directory
#. Prepare for the tests by adding the following to *tests.py*::

    from django.contrib.staticfiles.testing import StaticLiveServerTestCase
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import WebDriverException


    class InitialVisitTest(StaticLiveServerTestCase):

        def setUp(self):
            self.browser = webdriver.Firefox()
            staging_server = os.environ.get('STAGING_SERVER')
            if staging_server:
                self.live_server_url = 'http://' + staging_server

        def tearDown(self):
            self.browser.quit()

        def test_authentication(self):

            # Charlie has decided to try out the Fifteen Puzzle program and goes to its homepage
            self.browser.get(self.live_server_url)

            # He comes to a login page
            self.assertIn('Login', self.browser.title)


#. Run the test to prove that it fails.
#. Devise unit tests to help incrementally develop the program until the current form of the functional tests pass.

I have run my first functional test and it has failed in the intended way. Hooray! Now it is time to move on to unit
tests which, in my understanding, is more oriented to testing the code. However, before I can even write any unit tests,
I have to understand how authentication works in Django.

Authentication in Django 5.0
============================

An overview of Django's authentication system can be found `here <https://docs.djangoproject.com/en/5.0/topics/auth/>`_,
which has links to more detailed discussions. I've looked through part of that but also realize that I need to
understand how the system has been working in my Christmas websites.

What I've Been Doing for Authentication
---------------------------------------

I notice that I have a user app in my Christmas websites. I don't know if I added it specifically or if it comes by
default when ``python manage.py migrate`` is run the first time. I may have created it to be able to style my own login
and logout pages, or to provide a simple way to adjust for there being two "Brians" in the family. It may just have been
suggested by the book I originally used to learn Django. In any case, it does not seem to override much of the built-in
properties of the Django User model.

Here is the sequence of events that takes place when a user enters the website for the first time:

#. The first path in *config/urls.py* redirects the user to 'user/login'.
#. The first path in *user/urls.py* engages *auth_views.LoginView* and sends it the address of the login template I
   created and a flag to ``redirect_authenticated_user=True``.
#. *auth_views.LoginView* displays my *user/login.html* page and processes the form.
#. Upon successful login the user is redirected to the ``LOGIN_REDIRECT_URL`` set in *config/base.py*, the common part
   of the original settings file.

Unit Tests for Redirection
--------------------------

With that I suspect my first unit tests should:

#. Assert that the user is redirected to the login url.
#. Assert that it has actually arrived at the proper template.

***********************
Authentication Part Two
***********************

The Next Functional Tests
=========================

Once these tests passed, the functional tests also passed so it's time to go on to the next step::

    # Charlie sees entry boxes for his username and password, each with placeholder text reminding him
    # what to enter.

    # The first time he enters them he, understandably, makes a small mistake in copying the password and is returned
    # to the login page which displays a nice message encouraging him to try again.

    # Once he enters his username and password, Charlie arrives at the game's entry page.

Planning the Login Functional Tests
-----------------------------------

In order to write this test I will need to know:

#. What it needs to simulate. (Entering the username and password and clicking the "Login" button - or pressing the
   "Enter" key.
#. How to simulate those things. (Picking out the input boxes with By, and entering strings with Keys.)
#. What the result should be from correctly entering a username and password. (The game's entry page opens.)
#. How to test for that result. (Give it a unique title and test for its presence.)
#. What the result should be from incorrectly entering a username and password. A return to the login page with an
   appropriate error message displayed.
#. How to test for that result. (Checking for the title of the login page as done previously and checking for the
   presence of the error message.)

Implementing the First Login Functional Test
--------------------------------------------

I wrote the following test in the ``InitialVisitTests``::

    # He notices two entry boxes, one with "username" and the other with "password" as their placeholder texts
    username_inputbox = self.browser.find_element(By.ID, "username_input")
    password_inputbox = self.browser.find_element(By.ID, "password_input")
    self.assertEqual(username_inputbox.get_attribute("placeholder"), "Enter your username.")
    self.assertEqual(password_inputbox.get_attribute("placeholder"), "Enter your password.")

Running the test results, of course, in a failure::

    selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="username_input"]

Now I turn to unit tests to pass this next step.

Planning the Unit Tests
-----------------------

I will write a series of unit tests to guide the development of login.html:

#. Does it properly extend the base.html file?
#. Does it allow for Bootstrap styling?
#. Can users be entered into the database?
#. Can users be retrieved from the database upon entering their username and password.
#. Does it refuse to retrieve a user when the username and password are incorrect in any way?

Using the base.html File
^^^^^^^^^^^^^^^^^^^^^^^^

Checking whether it extended the base.html file turned out to be different than I thought. I thought I'd just test for
text that would only be in the base.html file, such as "<!doctype html>" but the test always failed even though I could
see that text in the browser's display of the source code for the login page. I found a
`solution <https://stackoverflow.com/questions/39825769/django-testing-if-the-template-is-inheriting-the-correct-template>`_
here, one which seems more proper than checking for text anyway.

Delaying Test for Bootstrap
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Chapter 8 of Harry Percival's book explains a method for ensuring that Bootstrap is loaded and functioning. He does it
in his functional tests, however. I didn't understand at first but it finally occurred to me that, his method, checking
to see if an input box gets horizontally centered on the page, requires that the page is actually being served. That
means that selenium needs to be active and that means it has to be done in the functional tests.

Beyond testing for the presence of Bootstrap, however, there is no need to test every little aspect beyond what you
already do: load the page and see if you like the way it looks! I will delay that kind of testing until later as well.

Implementing the Second Login Functional Test
---------------------------------------------

The next test to implement is whether Charlie gets to the entry page when he enters his username and password. Here is
my proposed functional test::

    # Uncle Jim sent him his login information so he enters his username and password, clicks login and
    # arrives at the games entry page
    charlie = User.objects.create_user("Charlie", "charliepassword")
    username_inputbox.send_keys(charlie.username)
    password_inputbox.send_keys(charlie.password)
    login_button = self.browser.find_element(By.ID, "login_button")
    login_button.click()
    self.assertIn('Fifteen Puzzle', self.browser.title)

Time Out from Test-Driven Development
-------------------------------------

Since the main point of the above functional test is to get Charlie to the entry page, I should create an entry page and
make sure an authenticated user can get to it. This may also be the point to ensure that a user who enters a username
and password that do not match what's in the database should be returned to the login page displaying an error message.

Unfortunately, I have no clue on how to write unit tests that are really any different from the functional test I
already have. Plus, I don't really know how authentication works in Django. I decided just to get it working live and,
perhaps, figure out how I could have written unit tests for it later. I will keep my notes for that in
:ref:`authentication`.

.. _second_unit_tests:

The Second Set of Unit Tests
----------------------------

Now that I have authentication working already I can see, by looking at the local server's output, what happens for
both successful and unsuccessful logins and try to devise tests for them. Here are the results of some of my
experiments:

+----------------------------------------------+---------------------------------------------------+
| Action                                       | Result                                            |
+==============================================+===================================================+
| Log in as Charles, password correct          | A post to /user/login/ redirects (status_code 302)|
|                                              | to /fifteen/entry/ (status_code 200)              |
+----------------------------------------------+---------------------------------------------------+
| Log in as Charles, password incorrect        | Posts back to /user/login with {{ form.errors }}  |
|                                              | set to a default value indicating an incorrect    |
|                                              | username and/or password.                         |
+----------------------------------------------+---------------------------------------------------+
| Log in as Dharles, password correct          | Same as above.                                    |
+----------------------------------------------+---------------------------------------------------+
| Log in as George, using Charlie's password   | Same as above.                                    |
+----------------------------------------------+---------------------------------------------------+
| Log in as George, using any password         | Same as above.                                    |
+----------------------------------------------+---------------------------------------------------+

From this it seems that I really only have to test for someone logging in correctly and ANY kind of mismatch between
the username and the password. All incorrect logins result in the same behavior, I just have to make sure it really
happens.

Testing for Correct Login
^^^^^^^^^^^^^^^^^^^^^^^^^

I added the ``setUpTestData`` class method to create "Charles" as a user and then, while trying to use ``login`` to log
him in, I realized it wouldn't work for that purpose but suggested another test -- just to see if he could log in or
not. Here is the unit test I ended up with::

    class LoginTest(TestCase):

        @classmethod
        def setUpTestData(cls):
            charlie = User.objects.create_user("Charles", password="charliespassword") # note: password is a kwarg

        ...

        test_login_from_credentials(self):
            self.assertTrue(self.client.login(username='Charles', password='charliespassword')
            self.assertFalse(self.client.login(username='Charles', password='nothing')

Testing for Correct Redirection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What should happen upon successful login is that the site should redirect to */fifteen/entry/* so if I check for a
redirect, a url of */fifteen/entry/* and the correct template being displayed, that should be sufficient.

Here is the test that finally worked::

    def test_correct_user_login_post_redirects(self):
        response = self.client.post('/user/login/', {'username': "Charles", 'password': "charliespassword"},
                                    follow=True)
        self.assertRedirects(response, '/fifteen/entry/')
        self.assertTemplateUsed(response, 'fifteen/entry.html')

I had to use ``follow=True`` in the post request in order to properly test for the template used.

Testing for Proper Response to Incorrect Login
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this case, the site should return to */user/login/* with ``{{ form.errors }}`` being set. Thus the ``response.url``
should be ``/user/login/`` and the response should contain the form errors somehow. I will have to experiment with
printing various things in the response to find out how to test for that.

After a lot of print statements showing me various aspects of the response object
(`See documentation here <https://docs.djangoproject.com/en/5.0/topics/testing/tools/#testing-responses>`_) here is the
code that worked::

    def test_bad_login_returns_to_login_with_errors(self):
        response = self.client.post('/user/login/', {'username': 'Charles', 'password': 'wrong'})
        self.assertEqual(response.request['PATH_INFO'], '/user/login/')
        self.assertContains(response, 'Please enter a correct username and password.')

Commenting out the code that made login work I ran the tests and, though it wasn't quite the same as actual Test-Driven
Development, I could see that my tests were actually testing for something.

Thought Collection
==================

At some point I am going to have to deal with logging out of the program as well as logging in. This is part of
authentication so it should be just after completing the login portion.

*******************************************
Evaluation of Using Test-Driven Development
*******************************************

I can say I'm not overly enamoured with the process of Test-Driven Development. I can't say it's a waste of time, I
think it did force me to go through the login process, at least the part I've done so far, with a greater understanding
than I have from copy/pasting code, but it is a costly process and, in the kind of work I do, the benefits may not be
worth it.

This is not to say that testing itself is not worth it. I would like to apply tests as much as possible to various parts
of my programs in order to prevent little changes from breaking the whole thing, and to assure myself that it really is
working the way I want it to. The empty word entries in the BoggleWords database is an example. Could I have noticed
that earlier with cleverly designed tests?

But then, could I have produced those cleverly designed tests at this point in my understanding of testing? Probably
not. I think it may be more wise to learn testing on functions AFTER I write them rather than before.

Probably my biggest reasons for deciding to leave Test-Driven Development behind for now is that the program I'm getting
from it is developing so slowly that I am likely to lose interest AND so rudimentary that making it aesthetically
pleasing and worth using after I do get it working would be such a daunting task that I wouldn't do it.

So, the bottom line is that I have decided to leave Test-Driven Development behind for now. I will try to write and
apply tests to various parts of the program as I write them, but I am going to follow an approach that is closer to my
conventional approach.
