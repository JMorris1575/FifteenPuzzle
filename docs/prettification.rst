.. _prettification:

######################################
Making the Website Look More Appealing
######################################

This is something I've done before, several times in fact. I could, I suppose, try to write a lot of CSS from scratch,
but I'm pretty sure it wouldn't be as good as simply using Bootstrap. Also, the login page on the Christmas website uses
FontAwesome and I want a review on how to use that too.

***************
Using Bootstrap
***************

Going to https://getbootstrap.com/ I see that the CDN links have not changed since I made the Christmas website and that
Bootstrap is still on version 5.3.2. I added the <link> and <script> tags from the "Include via CDN" section and so I
should now be ready to use Boostrap.

******************
Using Font Awesome
******************

Font Awesome is currently on version 6.5.1 and the approach is different than before. They want me to set up a "kit." I
entered my FrJamesMorris email on their start page and clicked "Send Kit Embed Code." They sent me a confirmation email
and asked me to choose a password. I think <pet-kzoophone> should do nicely. It seemed to accept that so I came to a
page where I could name my kit. I called it "Jim's Kit." Great name, don't you think? Otherwise I left all the defaults
in place and clicked the "Save Changes" button.

Clicking on the Set Up tab on that page brought me to the <script> tag I need to include within the <head> tag in
``base.html``. Now to see if it works.

To test it I just used my stubbed in entry page and placed a solid house icon under the heading. I seem to have gotten
both the little house under the heading that I expected, and the Bootstrap defaults. I guess I didn't know bootstrap had
defaults but all of my pages are now using a sans serif font.

I see that by changing the <i> tag, or just copy/pasting it, I can change the size and color of the icon, and use some
limited animations. The animations, I think, could be annoying. I think something more controlled,
`as offered here <https://www.youtube.com/watch?v=vqXLGX0szIQ>`_ might be better if I want to have animations.

************
Google Fonts
************

I went to https://fonts.google.com and selected Caveat for the page heading and Lato for the numbers. By clicking on
what looks like a clipboard at the upper right a sidebar opened where I could copy the links to put into the <head> tag
of *base.html*::

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Lato&display=swap" rel="stylesheet">

It also gave me some CSS rules to specify families::

    font-family: 'Caveat', cursive;
    font-family: 'Lato', sans-serif;

I put the links into the ``<head>`` tag of *base.html* but will save the CSS rules here for later reference if it turns
out I need them.

*******************
Overall Page Design
*******************

The overall look I have in mind is much like I have already done for the Christmas website: a big header area with a
background color that goes all the way across any size screen and a footer to match. The contents of the page will go,
of course, between the header and the footer and will contain the main puzzle, sometimes the aimed-for solution, a tally
of time and moves made will also sometimes be present. There should also be a space for other text, such as instructions
for the "tutorial" phase as well as messages from people or stories of ancestors given as "prizes" in the game. My ideas
for the content area will probably change when I start to develop it.

.. _header_design:

Designing and Implementing the Header
=====================================

The contents of the header will simply be the name "Fifteen Puzzle" at the left, a Welcome <user> message at the right,
along with a logout link next to the name. Later I may want to add options of types of puzzles to play at the right
and/or a logo image to use at the left.

Background and Foreground Colors
--------------------------------

It seems that, for the Christmas website, where I changed Bootstrap's primary and secondary colors to fit my website,
I created a *styles.scss* file in the *static* directory in the root folder for the Django program, most recently,
*christmas23*. Here I don't intend to change anything in bootstrap if I don't have to but will provide my own background
and foreground colors for the header (and footer) with the following::

    // SCSS Variables

    $color-background: #120f7a;
    $color-foreground: #ffdd55;
    $color-header-link: rgba(255, 221, 85, 0.8) !important;
    $color-header-link-hover: rgba(255, 221, 85, 1.0) !important;

    // Rules

    header, footer {
        background: $color-background;
        color: $color-foreground;
    }

    header a {
        color: $color-header-link;
        text-decoration: none;
    }

    header a:hover {
        color: $color-header-link-hover;
        text-decoration: none;
    }

    .header-text {
        font-family: 'Caveat', cursive;
        font-size: 4rem;
    }

I don't see anyplace where this scss file is referenced in the Christmas website's *base.html* file so I suspect that is
why there is an ``@import "../bootstrap/scss/bootstrap";`` statement at the top of the file. Here I will try to bring it
in with my own link::

    <link rel="stylesheet" type="text/css" href="{% static '/scss/styles.scss' %}">

However, before I tried that I read online that it won't work. The scss file needs first to be translated into css
which, as it turns out, can be done in VSCode with the "Live SASS Compiler" extension. I will try that...

First I had to point VSCode to my *FifteenPuzzle* folder in *D:/Documents on D/My Django Projects/* and actually create
the scss file in *fifteen24/static/scss*. The Christmas website namespaced it within a *site* subfolder but I am going
to try it without that.

I followed the directions in the `"Live SASS Compiler" video <https://www.youtube.com/watch?v=9J__JAgQbS0>`_ and here
is what I got in my *fifteen24/static/css/styles.css* file::

    header, footer {
      background: #120f7a;
      color: #ffdd55;
    }

    header a {
      color: rgba(255, 221, 85, 0.8) !important;
      text-decoration: none;
    }

    header a:hover {
      color: rgb(255, 221, 85) !important;
      text-decoration: none;
    }

    .header-text {
      font-family: "Caveat", cursive;
      font-size: 4rem;
    }/*# sourceMappingURL=styles.css.map */

With such a short css file I could have done that myself, but Live SASS Compiler also produced a *-min.css* version and
a *.map* version, though I don't know what good the latter is.

Updating the link above to something that will work::

    <link rel="stylesheet" type="text/css" href="{% static '/css/styles.css' %}">

Hmm... It's not working. I tried both with and without namespacing it under *site* but the terminal keeps giving me a
404 error (file not found) when trying to "GET /static/css/styles.css HTTP/1.1". It always gives the numbers 404 and
1801 at the end of the error message. I tried to stop and restart the server but got the same results. Time for another
chat with ChatGPT...

According to ChatGPT there should not be a forward slash "/" in front of the css in the ``{% static %}`` template tag
AND there needs to be a ``STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`` line in the *settings.py* file. When
I made both of those changes it worked! Now to figure out why...

I experimented with the forward slash "/" and discovered that it doesn't make any difference if it's there or not. That
may be why the Christmas website has been working so long even with one.

It does seem to make a difference if I namespace the css file within a *site* folder. It doesn't work when I do that,
though I had to do a ctrl-Refresh to show that it wasn't working. There must be some place in the Christmas website
where I tell it I'm using *site*.

It turns out that the STATICFILES_DIRS line in the Christmas website settings comes in both *dev.py* and *prod.py* as::

    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static', 'site'), )

I'm guessing the addition of "site" here is what makes it required in the Christmas website whereas the ``DIRS`` line
in the ``TEMPLATES`` setting is::

    'DIRS': [os.path.join(BASE_DIR, 'templates')],

which doesn't require the "site" folder.

The documentation for ``STATICFILES_DIRS`` at https://docs.djangoproject.com/en/5.0/ref/settings/#staticfiles-dirs
says::

    Default: [] (Empty list)

    This setting defines the additional locations the staticfiles app will traverse if the
    FileSystemFinder finder is enabled, e.g. if you use the collectstatic or findstatic management
    command or use the static file serving view.

    This should be set to a list of strings that contain full paths to your additional files
    directory(ies) e.g.:

    STATICFILES_DIRS = [
        "/home/special.polls.com/polls/static",
        "/home/polls.com/polls/static",
        "/opt/webfiles/common",
    ]

    Note that these paths should use Unix-style forward slashes, even on Windows
    (e.g. "C:/Users/user/mysite/extra_static_content").

So, it seems that ``STATICFILES_DIRS`` is not needed for regular static files within apps, but for extra ones, like for
the overall program.

Building the Header
-------------------

All that being done I just have to employ Bootstrap styles and the ``.header-text`` class to accomplish what I described
:ref:`above <header_design>`.

Adding the ``.header-text`` class immediately changed the font.

Unlike the ``{% block content %}`` template tag, the ``{% include "header.html" %}`` template tag is not within a
Bootstrap container. I will first add a ``<div>`` with a class of "container" to surround the existing content of
*header.html*.

.. note:: I feared that some of my Christmas apps used a second container within the one provided by *base.html* but
          that does not seem to be the case. You may want to check for it more thoroughly though.

I will need to divide the header container into a row with two columns to put the title on the left and the welcome
message and logout link on the right. I also added an ``.h4`` class to the ``<span>`` with the welcome message to make
the text larger.

Getting the button to be on the same line and looking like a link is going to be more of a challenge. I will have to add
some css code to the header page to get it to work. Fortunately, :ref:`the code <logging_out>` has been provided by
Django. Still, though, it took a lot of experimentation to finally get what I wanted. Here is the final form of the
whole *header.html* file::

    {% load static %}

    {% block head %}

        <style>
            #logout-form {
                display: inline;
            }
            #logout-form button {
                background: none;
                color: rgba(255, 221, 85, 0.8) !important;
                border: none;
                cursor: pointer;
                padding: 0;
                text-decoration: underline;
            }
            #logout-form button:hover {
                color: rgba(255, 221, 85, 1.0) !important;
            }
        </style>

    {% endblock %}

    <header>
        <div class="container">
            <div class="row">
                <h1 class="col-8 header-text">The Fifteen Puzzle</h1>
                {% if user.is_authenticated %}
                    <div class="col d-flex justify-content-end">
                        <div class="d-flex align-items-center">
                             <span class="h4">Welcome {{ user.first_name }}!&nbsp</span>
                             <form id="logout-form" method="post" action="{% url 'user:logout' %}">
                                 {% csrf_token %}
                                 <button class="h6" type="submit">(Log out)</button>
                             </form>
                        </div>
                    </div>
                {% else %}
                    <div class="col d-flex justify-content-end">
                        <div class="d-flex align-items-center">
                            <span class="h4">Welcome!&nbsp</span>
                            <a href="{% url 'user:login' %}?next={{ request.path_info }}">(Login)</a>
                        </div>
                    </div>
                {% endif %}
            </div>
        </div>
    </header>

Several things to note:

#. I need to learn more about Bootstrap's ``.d-flex``
#. I finally realized what the ``?next=`` is for. It's for the case where a non-logged in person tries to get directly
   to a page -- say from a saved link. The ``@login_required`` will catch that, send them to the login page, and when
   they log in they will get to the page they originally asked for.
#. I'm going to have to decide whether to put the css styling for the ``header a`` selector here or leave it in
   *fifteen24/static/styles.css*.

Improving the Header
--------------------

While working on the *login.html* and *logout.html* pages, and getting *logout.html* even to appear, I also made some
changes to *header.html* so it now looks like this::

    {% load static %}

    {% block head %}

    (...)

    <header>
        <div class="container">
            <div class="row">
                <h1 class="col-8 header-text">The Fifteen Puzzle</h1>
                {% if user.is_authenticated %}
                    <div class="col d-flex justify-content-end">
                        <div class="d-flex align-items-center">
                             <span class="h4">Welcome {{ user.first_name }}!&nbsp</span>
                             <form id="logout-form" method="post" action="{% url 'user:logout' %}">
                                 {% csrf_token %}
                                 <button class="h6" type="submit">(Log out)</button>
                             </form>
                        </div>
                    </div>
                {% elif next %}
                    <div class="col d-flex justify-content-end">
                        <div class="d-flex align-items-center">
                            <span class="h4">Welcome!&nbsp</span>
                            <a href="{% url 'user:login' %}?next={{ next }}">(Login)</a>
                        </div>
                    </div>
                {% else %}
                    <div class="col d-flex justify-content-end">
                        <div class="d-flex align-items-center">
                            <span class="h4">Welcome!&nbsp</span>
                            <a href="{% url 'user:login' %}">(Login)</a>
                        </div>
                    </div>

                {% endif %}
            </div>
        </div>
    </header>

This currently works to prevent people from getting to a url they entered into the address box without being logged in.
It remains to be seen if it will also work for cases where they are authenticated but enter the url for a page to which
they do not have permission.

Designing and Implementing the Footer
=====================================

After all that, the footer is going to be easy! It will simply have "Fifteen Puzzle - Originally Created in 2024" in the
center of a blue band at the bottom of the page. I don't have to load the static system, I've already adjusted the text
color in *styles.css*, all I have to do is add a few tags::

    <footer>
        <div class="container">
            <div class="d-flex justify-content-center">
                <h4>Fifteen Puzzle - Originally Created in 2024</h4>
            </div>
        </div>
    </footer>

**************
The Login Page
**************

The login page used for the Christmas website is sparse but functional. Here I might add a little bit more but I don't
think much more will be necessary. Here is my sequence of development of the existing login page:

#. Create a card to hold the login items.
#. Center the card.
#. Create a card header with blue background and yellow text.

   * When I tried to add a ``.card-header-text`` class to the *styles.css* in the main *static* directory it didn't
     work.
   * I could, however, insert the ``<style>`` code I wanted into the *login.html* page itself.
   * Eventually I solved the problem but I'm not sure how. Part of it may have been a syntax error in the css file,
     and part of it not using the right class in the tag. One thing I learned (again) is that keeping an eye on the
     GET and POST reports generated by the server can be helpful.

#. Move the card down a little from the header.
#. Center the input boxes and login button.
#. Use Bootstrap to style the input boxes.
#. Use Bootstrap to style the login button.
#. Add Font Awesome characters to the Username and Password input boxes.

   * I had trouble with this because Bootstrap has removed ``.input-group-append`` and ``.input-group-prepend`` which I
     had used in the Christmas website. It is much simpler now, just add the span containing the <i> tag as a direct
     child of the ``.input-group`` div and give it the ``.input-group-text`` class.

#. Add Font Awesome character to the Login button.
#. Add css styling for button when the mouse hovers over it.

***************
The Logout Page
***************

Making the Logout Page Visible
==============================

Before I can style it I first have to get *logout.html* even to appear. Currently, when I click the "(Log out)" link in
the header area on the entry page, it sends me to a blank page consisting only of the header and the footer. The url
path to the logout page is as follows::

    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),

and the *user/logout.html* file is present, but I see no indication that it is being used.

Also, I notice that the "(Login)" link in the header of my blank logout page links to::

    http://localhost:8000/user/login/?next=/user/logout/

and the ?next=/user/logout/ part should not be there. That is for when someone enters the url for one of the websites
pages without being logged in or without the appropriate level of permissions.

Django Documentation
--------------------

The documentation on the
`LogoutView class <https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.views.LogoutView>`_
says that it will redirect to LOGOUT_REDIRECT_URL from the *settings.py* file if it is not given a ``next_page``
parameter. I do not have that set in *settings.py*, and it has no default according to
`the settings documentation <https://docs.djangoproject.com/en/5.0/ref/settings/#logout-redirect-url>`_, so that is
probably my problem. When I added this line to *settings.py*::

    LOGOUT_REDIRECT_URL = reverse_lazy('user:logout')

nothing changed.

The Solution
------------

Then I noticed the difference between my *login.html* page and my *logout.html* page and the latter only had the
``{% extends "base.html" %}`` tag at the top and none of the others. When I made it look like this::

    {% extends "base.html" %}

    {% block title %}Fifteen Logout{% endblock %}

    {% block content %}

        <h1>This is the stubbed-in logout page.</h1>

    {% endblock %}

it started working and kept working even after I commented out the ``LOGOUT_REDIRECT_URL`` line in *settings.py* so I
deleted that line entirely.

Styling the Logout Page
=======================

There is not much to this page. I think it simply needs to have a good-bye message and a button to get to the login page
if they want. I think I'll put it all in a Bootstrap card with a title of "Thanks for Visiting!" Here are the steps:

#. Create the card
#. Create the title
#. Create a message about logging in again.
#. Create a button to return them to the login page.
#. Put a blue border on the card the same color as the title background

I created the blue border through CSS by overriding the border styling of Bootstrap's ``.card`` class:

**styles.scss**::

    .card {
        border: 2px solid $color-background;
    }

This will automatically apply to the cards throughout my website.
