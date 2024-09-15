.. _authentication:

##################################
Building the Authentication System
##################################

In trying to develop the authentication system following the Test-Driven Development discipline of always writing a test
before writing the code, I found I didn't have any idea how to do it. I suspect that is because I really don't know how
the authentication system works in Django. I decided to simply build the system the normal way, somewhat simultaneously
writing urls, views and html files, and tinkering around until it works on the local server.

***********
First Steps
***********

In order to do this I needed to do a ``python manage.py migrate`` to actually create the User database, then create a
superuser with ``python manage.py createsuperuser`` to have access to the admin. I decided to keep my usual
identification information: username = Jim, email = FrJamesMorris@gmail.com, password = <dylan_selfie>.

With that done I could create a few test users, including a fake sign-in for Charlie:

+----------------+-----------------------------+--------------------------+
| username       | email                       | password                 |
+================+=============================+==========================+
| Charles        | charlie@example.com         | charliespassword         |
+----------------+-----------------------------+--------------------------+
| TestUserOne    | test_user_one@example.com   | testpassword1            |
+----------------+-----------------------------+--------------------------+
| TestUserTwo    | test_user_two@example.com   | testpassword2            |
+----------------+-----------------------------+--------------------------+

***************
Initial Results
***************

When I enter a valid user in the login page it generates a *Page not found* error because it cannot find any page at
*http://localhost:8000/user/login/puzzle/entry/*. I wouldn't expect it to at this point but I have a couple of
questions:

#. Where did it get its information as to where to go after a successful login? (I commented out the
   ``LOGIN_REDIRECT_URL`` in settings.)
#. Why does it still include ``/user/login/`` as part of the url?

Here is the pertinent code:

**user/urls.py**::

    app_name = 'user'
    urlpatterns = [
        path('login/', auth_views.LoginView.as_view(template_name='user/login.html',
                                                    next_page='puzzle/entry/',
                                                    redirect_authenticated_user=False), name='login'),
    ]

**config/settings.py**::

    # LOGIN_REDIRECT_URL = reverse_lazy('entry')

I suspect it is my inclusion of next_page='puzzle/entry/' in the parameters given to the LoginView class view that
answers both of my questions. When I delete that parameter, but leave the ``LOGIN_REDIRECT_URL`` setting commented out,
it now is looking for something at *localhost:8000/accounts/profile/*. Not what I was expecting but */accounts/profile/*
is Django's default value for ``LOGIN_REDIRECT_URL``.

When I uncomment the ``LOGIN_REDIRECT_URL`` line in *settings.py*, I get a *NoReverseMatch at /user/login/* error
because, as of yet, there is no url named 'entry.' That can be easily fixed.

**********************
Completing the Process
**********************

I see three things that need to be done:

#. Gradually modify my code until a bona-fide entry page appears for an authenticated user.
#. Verify that the right things happen when the username and password entered are incorrect.
#. Build a Logout system.

At the end I will probably want to set ``redirect_authenticated_user`` back to ``True`` so that a person doesn't have to
log in every single time. I may also want to look into what those strange lines having to do with an authenticated user
NOT having access to a page they've requested actually do and when they are used.

Getting to the Entry Page
=========================

The steps to accomplish this were to:

#. Create a *urls.py* file in the *puzzle* app.
#. Create a path in config/urls.py to include the puzzle/ urls.
#. Create a path named 'entry.'
#. Create the view to which the path points.
#. Create the *entry.html* template to be rendered by the view.

Thinking of Corresponding Unit Tests
====================================

Looking at what needed to be done I wonder what unit tests I could write to test for the proper operation of those
things. Is there a way, for instance, to check to see if the authenticated user is being sent to the right path before
checking for whether the template was rendered successfully?

`This page <https://docs.djangoproject.com/en/5.0/topics/testing/tools/>`_ at Django's documentation turned out to have
a lot of useful information. Here are some of the things I noticed:

#. When I use the ``self.client.post()``, say for logging someone in, I can supply their login information in a
   dictionary: ``response = self.client.post('/user/login/', {'username': "Charles", 'password': 'charliespassword'})``.
#. I can enter a group of individuals to be used by all the login tests by using something like the following::

    class MyTests(TestCase):
        @classmethod
        def setUpTestData(cls):
            charlie = User.objects.create_user("Charles", "charliespassword")

        def test1(self):
            login(username="Charles", password="charliespassword")
            ... continue with test

#. If I am not testing the authentication process itself, but I'm testing something where a user needs to be logged in
   for it to function (perhaps if I'm using ``login_required`` in the path), I can use::

    def test1(self):
        force_login(charlie)        # with charlie defined as above

#. There are various assertions, special to Django's test cases, that can check for the proper urls, status codes, html,
   etc. The assertions `can be found here <https://docs.djangoproject.com/en/5.0/topics/testing/tools/#assertions>`_ but
   you may also need to look through the documentation for the various test case classes earlier on that page as well as
   the documentation on requests and responses.

Having read that I feel more prepared to write sensible unit tests. For that I will return to the
:ref:`tests document <second_unit_tests>`.

*********************************************************
Continuing Authentication without Test-Driven Development
*********************************************************

What remains to be done now that I have stepped away from :abbr:`TDD (Test-Driven Development)` is to create a process
to log out and go to a logout page which, itself, has a link to get back to the login page. I will keep it very basic,
for now, and work on making it look better separately.

Header and Footer
=================

Because the sensible place for the logout link is in the header I will create stubbed-in header.html document that
contains it along with a heading and the player's name. While I'm at it I may as well write a footer.html document to
give information about the program, such as when it was created, the version it is, etc.

.. _logging_out:

Logging Out
===========

I think I have discovered the change in Django that caused the problem I noticed after trying to switch to Django 5.0.
Using a regular ``<a>`` link produces a ``GET`` request and ``GET`` requests for logout were deprecated as of Django
4.1. Apparently they finalized it with Django 5.0. See the note from the
`Django 4.1 release notes <https://docs.djangoproject.com/en/5.0/releases/4.1/#features-deprecated-in-4-1>`_::

    Log out via GET¶

    Logging out via GET requests to the built-in logout view is deprecated. Use POST requests instead.

    If you want to retain the user experience of an HTML link, you can use a form that is styled to appear as a link:

    <form id="logout-form" method="post" action="{% url 'admin:logout' %}">
      {% csrf_token %}
      <button type="submit">{% translate "Log out" %}</button>
    </form>

    #logout-form {
      display: inline;
    }
    #logout-form button {
      background: none;
      border: none;
      cursor: pointer;
      padding: 0;
      text-decoration: underline;
    }

I'm going to see what it looks like as a button. (It looks okay by itself, but without messing with it it appears on the
next line. Also, it doesn't match the Logout link that appears when a valid user is logged in. Perhaps I should make it
a more prominent button on the logout page anyway. And perhaps the logout page can explain its purpose -- allowing more
than one person to use the same computer.)

Blocking Users from Sneaking into Admin Areas
=============================================

This wasn't too hard once I figured out the syntax. I temporarily made the entry page off limits by using this view::

    from django.shortcuts import render, redirect
    from django.contrib.auth.decorators import login_required
    from django.conf import settings

    @login_required
    def entry_view(request):
        if request.user.is_staff:
            return render(request, 'fifteen/entry.html')
        else:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")

Then I added this section, modified from the unused version on the Christmas website, to the login page::

    {% if next %}
        {% if user.is_authenticated %}
            <p class="text-danger">Sorry, you have to have special permission to enter this page. To proceed, you need
                to login with a different account.</p>
        {% else %}
            <p class="text-danger">Please login to see the page you seek.</p>
        {% endif %}
    {% endif %}

I returned the view to this form::

    from django.shortcuts import render, redirect
    from django.contrib.auth.decorators import login_required
    from django.conf import settings

    @login_required
    def entry_view(request):
        return render(request, 'fifteen/entry.html')

Notice that I retained the imports in case I need them later.

*******
Summary
*******

Now that I have authentication working the way I want I should be able to add tests to verify that it actually happens
I think it best that they be unit tests, though, since they do get into the nitty-gritty of the code and run faster that
way anyway. I think I already have tests for logging in, I need to add tests for logging out and for trying to sneak
into restricted pages. Since there are currently no restricted pages however, I will defer them both until later. I want
to work, now, on :ref:`prettification with Bootstrap and FontAwesome <prettification>`.