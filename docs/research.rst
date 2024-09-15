.. _research:

#####################
Time Out for Research
#####################

One possibility that looks good right now is to
use the ``<canvas>`` element since its design seems to make it very suitable for games. I plan to go through the
`W3Schools tutorial on the canvas element <https://www.w3schools.com/graphics/canvas_intro.asp>`_ and see what I can
learn.

***************
Overall Process
***************

To use the ``<canvas>`` element it must know its size. I'm not sure if it can get that size from Bootstrap or if it
has to be hard-coded in pixels but I suspect it can get its size from Bootstrap since I think my Concentration game on
the Christmas website does that. The canvas element must also have a way it can be located by JQuery or JavaScript,
usually an id.

Then, to draw something, one needs to:

#. Locate the Canvas Element with JQuery or JavaScript
#. Create a Drawing Object -- which it calls a "context" which doesn't really say what it is. What it is is an object
   "with properties and methods for drawing," so I think it can be better thought of as a drawing tool. It can be 2d or
   3d and is instanced with a JavaScript line like ``const ctx = canvas.getContext("2d");``
#. Use the drawing methods to actually draw on the canvas.

.. _w3schools_tutorials:

*********************
Canvas Clock Tutorial
*********************

After discussing all of the basic drawing functions W3Schools gives a
`Canvas Clock <https://www.w3schools.com/graphics/canvas_clock.asp>`_ tutorial. I think I will create a temporary page
in my fifteen puzzle app to complete this tutorial. Perhaps it can also serve as a means to making sure an otherwise
authenticated user can access pages that only staff are supposed to be able to see. But that is for later. Now my focus
is on the tutorial.

Setting Up
==========

First I have to create the page where the clock will be made. Here are the steps I will follow:

#. Create a *clock.html* file and copy/paste much of *puzzle.html* into it.
#. Create a button on *puzzle.html* to link to access the url *fifteen/clock*.
#. Create the url path and view to facilitate the connection.
#. Test to make sure it's working.

Completing the Tutorial
=======================

Lesson One
----------

This seems pretty clear to me: set the background to (almost) black and draw a white circle in it.

Lesson Two
----------

I like the way this tutorial is looking. It shows how to work with circles, gradients, paths, and more. I will have to
review the earlier material on each drawing command to be able to do it myself however. There are some strange things,
such as the ``stroke()`` command that seems to know what it's supposed to draw, but I'm not sure how. Could I draw just
a partial rim?

Lesson Three
------------

In some ways this looks very promising, showing me how to center text I think, but in other ways it is very confusing.
Again, probably because I don't know what all the commands really do, there are some very strange things going on
involving the ``rotate``  (which, to my astronomy oriented mind, should maybe be called "revolve"?) and ``translate``
commands and how the ``translate`` command works exactly.


Lesson Four
-----------

Now we're drawing the hands and I understand most of it but there is still some weirdness connected to rotating and
drawing lines of negative lengths. I imagine the latter has to do with where the zero angle starts -- I think it must be
the 6 o'clock position. Re-rotating to the negative value of the previous rotation may be to reset the position to its
starting angle -- straight down.

Lesson Five
-----------

This I completely understood, though I still didn't get the syntax right first time. All that is required to get the
clock to work is to set up an interval to call ``drawClock`` at one-second intervals.

Since it uses the computer date/time to set the clock it should make a good way to test my Garmin watch. Currently the
computer time is about four seconds ahead of the Garmin watch which, is around fifteen seconds behind my alarm clock. I
can check to see how this changes with time.

*****************
HTML Game Example
*****************

W3Schools also has a game example that should be useful to go through. I will teach me how to animate things at the very
least.

Setting Up
==========

I will add this to the fifteen app just as I did the clock tutorial:

#. Create a *game.html* file and copy/paste much of *puzzle.html* into it.
#. Create a button on *puzzle.html* to link to access the url *fifteen/game*.
#. Create the url path and view to facilitate the connection.
#. Test to make sure it's working.
#. Proceed with the tutorial starting at https://www.w3schools.com/graphics/game_intro.asp .

Completing the Game Tutorial
============================

Part One
--------

This tutorial is set up quite a bit differently than the Clock Tutorial. It seems less well organized but that is
helping me build some strength with JavaScript. Also, it is not anticipating that I would try to add this to a
pre-existing website.

It is structured to start when the page loads. In their version they put the command: ``onload="startGame()"`` as the
first parameter of the ``<body>`` tag. In my version the ``<body>`` tag is squirrelled away inside *base.html* and thus
inaccessible. Instead I put the line ``startGame()`` to run when the script loaded. I found I had to put it at the end,
though, AFTER the function startGame() had been defined.

The next challenge was to get the JavaScript to create the canvas element itself. I couldn't do it their way since they
imagined the ``<canvas>`` tag was going to be the first thing within the ``<body>`` tag but, with my putting inside a
Bootstrap card and using the Bootstrap row and column structure, the element to put it in wasn't that easy to find.
What finally worked for me was to create a ``<div>`` to hold the canvas and give it an id of "canvas-container", get
that ``<div>`` in the JavaScript with ``getElementById()`` and then use ``.appendChild()`` to add the canvas variable
to it. This is better understood in the code itself:

game.html::

    {% block head %}

    <style>
        canvas {
            border: 1px solid #d3d3d3;
            background-color: #f1f1f1;
        }
    </style>

    {% endblock %}

    {% block content %}

        <div class="card col-md-10 my-3 mx-md-auto">
            <div class="card-header text-center card-header-text">
                <h3>W3Schools Game Tutorial</h3>
            </div>
            <div class="card-body row justify-content-center">
                <div id="canvas-container" class="col-md-6">
                </div>
            </div>
        </div>

        <script>

            function startGame() {
                myGameArea.start();
            }

            var myGameArea = {
                canvas : document.createElement("canvas"),
                start : function() {
                    this.canvas.width = 480;
                    this.canvas.height = 270;
                    this.context = this.canvas.getContext("2d");
                    canvas_container = document.getElementById("canvas-container");
                    canvas_container.appendChild(this.canvas);
                }
            }

            startGame();

        </script>

    {% endblock %}

Notice also that the canvas is given a background color and a border by means of css styling.

Part Two
--------

I'm beginning to see things about JavaScript I hadn't noticed before, especially how JavaScript's object literals are
not only like Python dictionaries, which is how I've been thinking of them, but are more like defining Python classes.
They can have both property values and methods. The ``myGameArea`` object in the code above demonstrates this but I
didn't really notice until I got to this part where they added another function to it: the ``clear()`` function::

    ...
    clear : function() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
    ...

Meanwhile they also show a ``component`` function that is treated like an object. New "components" in the game area are
created with something like::

    redGamePiece = new component(75, 75, "red", 10, 10);

The redGamePiece is an instance of what, in Python, I would call the component class, even though ``component`` is
defined as a function. Also, notice that the ``redGamePiece`` is being defined as a global variable even though it is
defined within the ``startGame()`` function. It is global because it does not have the ``var`` declaration in front of
it. This way other functions, such as the ``updateGameArea`` function can access it. Finally, since the ``component``
"function" has an ``update`` function defined within it, which simply draws the current instance in its current size and
color at its current location in a call in ``updateGameArea`` written like this: ``redGamePiece.update();``.

So far motion is accomplished by having ``updateGameArea`` called every 20 milliseconds and ``updateGameArea`` is
tasked with the responsibility of calculating the new positions of all of the objects.

I'm not sure how this will help me move my tiles around the fifteen puzzle grid but this is only the second part of
eleven.

Part Three
----------

This section was all about controlling the motion of the red block in various ways. I got most of it but I can see that
I need to study JavaScript arrays more. It seems one can add an item at position 37 for instance, when there are no
items in positions 0 through 36!

I was able to figure out how to get the mouse postion with respect to the canvas which is undoubtedly going to be
important. It's in myGameArea's ``start()`` function and can only be used AFTER the canvas has been placed in its
Bootstrap container. Here is the code for the whole ``myGameArea`` object::

    var myGameArea = {
        canvas : document.createElement("canvas"),
        start : function() {
            this.canvas.width = 480;
            this.canvas.height = 270;
            this.context = this.canvas.getContext("2d");
            canvas_container = document.getElementById("canvas-container");
            canvas_container.appendChild(this.canvas);
            rect = this.canvas.getBoundingClientRect();
            this.interval = setInterval(updateGameArea, 20);
            window.addEventListener('mousedown', function(e) {
                myGameArea.x = e.pageX - rect.left;
                myGameArea.y = e.pageY - rect.top;
            });
            window.addEventListener('mouseup', function(e) {
                myGameArea.x = false;
                myGameArea.y = false;
            });
            window.addEventListener('touchstart', function(e) {
                myGameArea.x = e.pageX - rect.left;
                myGameArea.y = e.pageY - rect.top;
            });
            window.addEventListener('touchend', function(e) {
                myGameArea.x = false;
                myGameArea.y = false;
            });
        },
        clear : function() {
            this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
        }
    }

Part Four
---------

Now we have a much better game. No scoring yet, but it is challenging at least. I am seeing some JavaScript "recipes"
for lack of a better term. For instance, how to generate random integers within a certain range.

I don't really understand why they calculate the height of the lower part of the obstacle as depending on x, which is
the canvas width: ``x - height - gap``. The value ``height`` represents the height of the upper part of the obstacle,
and ``gap`` is the random size of the gap between 50 and 200. It seems to me it should depend on the canvas height, not
its width. When I changed that the game still worked but there still seemed to be several zero-height bars on the
bottom. It's not of enough interest to me, though, to figure out why. Their version, in the "Try It Yourself" section,
uses x however so I will too.

Part Five
---------

This section had to do with displaying a score. The biggest thing I learned was that the ``component`` function can be
multi-tasked into creating different things, in this case, both rectangle and text objects.

Evaluation
==========

Although this tutorial has been useful for learning things about JavaScript, and I may want to continue it later for
that reason, it is not really going to shed very much light on what I want to do. As it turns out, JQuery has an
``animate()`` method that is probably going to be more useful.

***********************
JQuery's Animate Method
***********************

This looks like the way to go. Once an element is selected one simply calls the ``animate()`` function on it and gives
it whatever css properties one wants to change. For instance, the following code moves an element with the id of 'tile'
250 pixels to the left::

    $('#tile').animate({left: '250px'});

To get relative motion one can use += or -= to change the motion by that much. The elements to be moved must their
css position property set to relative, fixed or absolute.