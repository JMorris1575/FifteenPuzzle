###########################
Developing the Action Pages
###########################

As currently conceived, the player will first come to the entry page and then, from there, go on to one puzzle or
another. I haven't yet decided a number of things about these puzzles so I think it would be best for now to simply
add a button to the entry page to get to a simple puzzle page where I can work out more details.

**********************
Rudimentary Entry Page
**********************

I think the entry page should have a main card that will later hold some kind of scoreboard -- either for that
individual player or for the group or possibly both. For now, though, it will hold only a lowly button which, being
clicked, directs one to a simple puzzle page. The entry page already extends *base.html* and supplies its own title so
I only need to add the card and the button. Here are the steps:

#. Add the card.
#. Add a header to the card.
#. Create a stubbed-in version of the puzzle page.

   * Create the template extending *base.html* and supplying "Fifteen Puzzle Page" as the title.
   * Add a url path to *fifteen/urls.py* to access ``puzzleview`` at ``fifteen/puzzle/``.
   * Write ``puzzleview`` in the simplest of ways.

#. Add a button to the card for accessing the puzzle page.

**************************************
Initial Development of the Puzzle Page
**************************************

I guess I should start where I'm thinking of having the players start, with a 2 x 2 grid with the numbers 1, 2 and 3 in
it just to develop the basics of how it looks. For that I will start with a rudimentary puzzle page, containing just a
card with the puzzle, and then experiment with how this simplest of puzzles should look with thoughts ahead, perhaps, to
how it should operate.

The Rudimentary Puzzle Page
===========================

I just need a space to work so I will create a card and try to create a frame for the 2 x 2 grid for starters. Here are
the steps:

#. Add the card.
#. Put a header on the card.
#. Put a temporary message inside the card.
#. Experiment with ways of creating and displaying a frame for the 2 x 2 grid.

Thoughts on the Grid
--------------------

The tiles not only have to move they also need to have different appearances when they are numeric tiles than they do
when they are picture tiles. I would also like to have a black, or perhaps some other color, border around them with a
grey area behind them.

But before any of that gets done, I have to make them square, and I'd also like them to have rounded corners. Their size
should be proportional to the size of the screen somehow so that they don't appear too big on desktop computers nor too
small on phone screens.

Perhaps I can create a ``<div>`` with an ``id="puzzle-frame"`` positioned with Bootstrap and styled with my own css. I
will, temporarily at least, put the css within the same html page for convenience.

Creating the Puzzle Frame
-------------------------

The ``.card-body`` is already a Bootstrap ``.row`` so I will put my puzzle frame there. For starters I will make it
``.col-md-4`` in horizontal size and then try to style it with css.

This is the arrangement that worked, minus the rest of the html code:

css::

    <style>
        #puzzle-frame {
            border: 10px solid black;
            border-radius: 10px;
        }

        #puzzle-area {
            position: relative;
            overflow: hidden;
            padding-bottom: 100%;
        }

        #puzzle-area p {
            position: absolute;
        }
    </style>

html::

        <div class="card col-md-10 my-3 mx-md-auto">
            <div class="card-header text-center card-header-text">
                <h3>Practice Space for Puzzle Development.</h3>
            </div>
            <div class="card-body row justify-content-center">
                <div id="puzzle-frame" class="col-md-4 bg-secondary">
                    <div id="puzzle-area">
                        <p>Something, at least, needs to be here or
                        nothing will show up in the div. It will have zero height and
                        I won't be able to see anything.</p>
                    </div>
                </div>
            </div>
        </div>

I need to study the css rules about position, overflow, and padding to understand how this works.

CSS Position
------------

I went to the W3Schools page on `position <https://www.w3schools.com/css/css_positioning.asp>`_ and found it quite
helpful, though I'm not sure how much I've retained. Here is a summary, portions marked with asterisks if I had to look
them up first:

There are five sorts of positions:

#. **static**: the default
#. **fixed**: \*stays in one location on the viewport. The top, bottom, left and right properties are used to set its
   position on the screen. I suppose it would have its purpose but it would seem annoying to me.\*
#. **relative**: \*allows an element to be positioned relative to its normal position with the top, bottom, left and
   right properties.\*
#. **absolute**: \*is like fixed except that the element is positioned relative to its nearest positioned ancestor
   instead of the viewport. If there are no positioned ancestors, it uses the document body and moves along with the
   page scrolling\*
#. **sticky**: keeps its contents on screen even if scrolling beyond it. It can be used for headings it seems to me but
   I'm not sure how it would work with <table> headings. It needs a special webkit in case the user is using Safari. It
   doesn't work on Internet Explorer. \*It will only work if you specify at least one of top, bottom, left or right.\*

I think my tiles need to be set up with absolute positioning and then can be moved either with JavaScript or with CSS.
That is something that remains to be discovered.

CSS Overflow
------------

There are four values for the `overflow <https://www.w3schools.com/css/css_overflow.asp>`_ property:

#. **visible**: the default. Extra content is shown even if it is outside the given area.
#. **hidden**: Extra content is truncated. Not shown under any circumstance.
#. **scroll**: scroll bar(s) appear to allow seeing content that exceeds its bounds in either direction.
#. **auto**: scroll bar(s) appear only if the content exceeds its bounds. Some browsers do this anyway, even if overflow
   is set to scroll.

The overflow property only works for block elements that have a specified height.

My ``#puzzle-frame`` element, and its child ``#puzzle-area`` don't need or want scroll bars so I should set overflow to
hidden.

Adding a Working Grid
=====================

Now that I have a frame I can experiment with adding the tiles and being able to move them around.

Displaying the Tiles
--------------------

First I'll just try to display three tiles, a 1, 2 and 3, in their solved position. Here are the steps I'll try:

#. Create a ``<div>`` inside the ``#puzzle-area`` with a class of ``.tile-odd`` containing the number 1.
#. Create a style for that ``<div>`` that:

   * gives it a white or ivory background
   * gives it a gold color for the text in an ``<h1>`` tag
   * gives it a size that is half the size of its container both in width and height
   * gives it absolute positioning within its ``<div>`` in the upper left hand corner

#. Add the other tiles one by one and adjust colors until you are satisfied.

Initial Method for Moving the Tiles
-----------------------------------

This is going to take some thought and probably some study on animation techniques. Something tells me I am going to
want to use JavaScript and JQuery in order to have the control I need not only for moving the tiles but for positioning
them correctly in the first place. I am going to have to give some thought to some data structures too. For instance,
how should a tile know what size grid it is in in order to be the right size for that grid? Currently I've got it all in
css but I don't think it can stay there. Css animation doesn't seem to be meant for playing games.

The Need for Research
=====================

I decided to do some research before going any further. The research turned out to be rather lengthy and so I decided to
put it in a :ref:`separate document <research>`. When I'm finished I'll come back here to continue building the Fifteen
puzzle.

Moving Tiles
============

In this section I'm only concerned with being able to move the tiles at all. The JQuery ``animate()`` method can do this
quite nicely, but I need to be very careful about the syntax.

Modifying the Styling
---------------------

I made some changes to the styling. Instead of having two
classes ``.tile-odd`` and ``.tile-even`` I broke them into three classes: ``.tile``, ``.odd`` and ``.even``. This saved
repeating some code and will help when I finally get the text to the right size. Here is how the css code looks now::

    .tile {
        position: absolute;
        color: GoldenRod;
        width: 50%;
        height: 50%;
    }

    .odd {
        background: Ivory;
        border-top: 5px solid White;
        border-left: 5px solid White;
        border-right: 5px solid AntiqueWhite;
        border-bottom: 5px solid AntiqueWhite;
    }

    .even {
        background: Crimson;
        border-top: 5px solid Red;
        border-left: 5px solid Red;
        border-right: 5px solid DarkRed;
        border-bottom: 5px solid DarkRed;
    }

The Event Listener
------------------

The code to do the actual movement is fairly simple at this stage::

    <script>

        $(function() {
            $('.tile').click(function() {
                $(this).animate({top : '+=' + $(this).outerHeight() + 'px'});
            });
        }); // end ready

    </script>

Later I discovered that it also works with the line::

    $(this).animate({top : '+=50%'});

which would be easier to work with.

All I have is a click event listener on all of the tiles and, when clicked, they each move down -- whether or not
anything is in their way! I am able to remove all three tiles from the frame with this! Obviously not the code I want
to end up with.

Thoughts About Simulating an Actual Puzzle
==========================================

To make my puzzle more realistic, even at this early stage, I am going to have to develop a means for determining:

#. Which tiles can move in the current configuration
#. For the tiles that can move, the direction in which they can move
#. Group moves should be possible. That is, clicking any tile in line with the blank should move it and all the tiles
   between it and the blank.

One way to accomplish this, it seems, is to create the tiles as objects much as the ``component`` function in the
``game.html`` tutorial. Then, at the beginning of a game, and after each move, the tiles can check and update their
ability to move. This shouldn't be too hard to determine. Any tile in the same column as the blank can move vertically,
any tile in the same row as the blank can move horizontally.

So, if I have a ``blank`` object, with the properties ``row`` and ``column`` and realize that, happily, the new position
of the blank is always going to be on any valid position that was clicked, the whole process might look like this in
pseudo code::

    if the tile the user clicked can move
        save the row and column of the tile clicked
        save the direction that the tile(s) can move
        move the tiles in that direction
        update the position of the blank to the row and column saved above
        for every tile in the puzzle
            if it is in the same row as the blank
                if it is in a column less than the blank's column
                    set it's direction to right
                otherwise
                    set it's direction to left
            if it is the same column as the blank
                if it is in a row less than the blank's row
                    set it's direction to down
                otherwise
                    set it's direction to up
            if it is not in the same row or column as the blank
                    set it's direction to none

But before I work on that I will have to work on using JQuery/JavaScript to create and place the tiles to begin with.

So far I have been creating the tiles as ``<div>``s inside another ``<div>`` with the id of ``puzzle-area`` which, in
turn, is in a ``<div>`` with the id of ``puzzle-frame``. The tiles are moved by animating their css properties through
the ``animate()`` function in JQuery.

However, the size of the ``<div>``s is not known in advance. Although the size of the tiles can be suitably controlled
with css properties, I have not yet figured out how to adjust the size of the font to correspond to the current size of
the tiles. I want to experiment with using a ``<canvas>`` tag of a given binary size (384 x 384) which is evenly
divisible by 2, 3, and 4 so that I can easily use grids of those sizes.

What I don't know is how simple it will be to animate the tiles once they are clicked and how easy it will be to
determine whether they have been clicked or not.

Experimenting with the ``<canvas>`` Tag
=======================================

I don't want to completely destroy what I have so far, nor let it interfere with this new approach, so I will create a
second puzzle page to experiment on. Here are the steps to accomplish that:

#. Copy *puzzle.html* to *puzzle-two.html*
#. Make any adustsments necessary in *fifteen/urls.py* and *fifteen/views.py* to display *puzzle-two.html* instead of
   *puzzle.html*.
#. Edit the html in *puzzle-two.html* to include the Bootstrap card etc. but otherwise only a ``<cavas>`` tag set to
   a size of 384 x 384. Perhaps I can give it a border to frame it appropriately.

Adding a Single Tile
--------------------

I will begin by creating a single tile, the white tile in the upper left corner, and display it on the screen. Here are
the steps:

#. Create a ``<script>`` section in *puzzle-two.html* and insert the JQuery ``ready`` function.
#. Create a plain white tile in the upper left corner.
#. Add shading to the edges of the tile.

.. _chat_gpt_version:

Considering how I would add shading to the edges of the tiles that are "attached" to the tiles I asked ChatGTP this
this question: "I am building a simulation of the Fifteen puzzle in html. I want to use a <canvas> as my puzzle frame
and have numbered tiles that move around when they are clicked. How can I create the squares within the canvas and have
the text for the numbers stay with the tiles when they are moved?"

Here is the response::

    To create a Fifteen puzzle using HTML canvas, you can follow these steps:

    1. Set up your HTML file with a canvas element.
    2. Use JavaScript to draw the puzzle grid and numbers on the canvas.
    3. Implement logic to handle tile movement when clicked.

    Here's a simple example to get you started:

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fifteen Puzzle</title>
    <style>
        canvas {
            border: 1px solid black;
        }
    </style>
    </head>
    <body>
    <canvas id="canvas" width="400" height="400"></canvas>

    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        const tileSize = 100; // size of each tile
        const puzzleSize = 4; // size of the puzzle (4x4 for Fifteen puzzle)

        // Initialize the puzzle
        let puzzle = [];
        for (let i = 0; i < puzzleSize; i++) {
            puzzle[i] = [];
            for (let j = 0; j < puzzleSize; j++) {
                puzzle[i][j] = i * puzzleSize + j + 1;
            }
        }
        puzzle[puzzleSize - 1][puzzleSize - 1] = 0; // empty space

        // Function to draw the puzzle
        function drawPuzzle() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.font = '30px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            for (let i = 0; i < puzzleSize; i++) {
                for (let j = 0; j < puzzleSize; j++) {
                    const tile = puzzle[i][j];
                    if (tile !== 0) {
                        const x = j * tileSize + tileSize / 2;
                        const y = i * tileSize + tileSize / 2;
                        ctx.fillStyle = '#cccccc';
                        ctx.fillRect(j * tileSize, i * tileSize, tileSize, tileSize);
                        ctx.fillStyle = '#000000';
                        ctx.fillText(tile, x, y);
                    }
                }
            }
        }

        // Function to get mouse position relative to the canvas
        function getMousePos(canvas, event) {
            const rect = canvas.getBoundingClientRect();
            return {
                x: event.clientX - rect.left,
                y: event.clientY - rect.top
            };
        }

        // Function to handle tile click event
        function handleClick(event) {
            const mousePos = getMousePos(canvas, event);
            const tileX = Math.floor(mousePos.x / tileSize);
            const tileY = Math.floor(mousePos.y / tileSize);
            // Implement logic to move the clicked tile if valid
            // For simplicity, you can swap the clicked tile with the empty space if adjacent
            // Remember to update the puzzle array and redraw the puzzle
            // You may need to check if the move is valid and handle edge cases
            // such as clicking on the borders of the puzzle
            drawPuzzle(); // Redraw the puzzle after the move
        }

        // Add click event listener to the canvas
        canvas.addEventListener('click', handleClick);

        // Initial draw
        drawPuzzle();
    </script>
    </body>
    </html>
    ```

    This code provides a basic setup for the Fifteen puzzle using HTML canvas. You need to implement logic inside the
    `handleClick` function to move the tiles when clicked. You can swap the clicked tile with the empty space if they
    are adjacent. After each move, you need to update the `puzzle` array and redraw the puzzle using the `drawPuzzle`
    function.

I copy it here for whatever useful ideas it can give me but I didn't really want its version of the whole program!
From my later questions, however, I gather that I can't just use JQuery's ``.animate`` function directly since "HTML
canvas doesn't natively support animations like DOM elements."

I wonder if there are JavaScript or JQuery libraries out there that could help...

It turns out there are a `number of them <https://themeselection.com/javascript-game-library/>`_ but I wonder what the
learning curve might be. I could use Godot too, it might go easier now that I have a better understanding of Ajax. Or
I might just continue developing my own means of animation as I've seen in the
:ref:`W3Schools tutorials <w3schools_tutorials>`. I think that's what I'll do for now at least.

The Tile Class
--------------

The JavaScript ``class`` needs a ``constructor()`` method which defines the parameters of the object being constructed.
My tile objects will have to have an x and y position, a size, a background color, a color, a number, and a direction of
motion that defaults to ``null``. Here is the code that (eventually) worked::

    $(function() {
        const canvas = $("#puzzle-frame")[0];
        const ctx = canvas.getContext('2d');

        class Tile{
            constructor(x, y, size, bg, color, number, dir) {
                if (dir === undefined) { dir = null; }
                this.x = x;
                this.y = y;
                this.size = size;
                this.bg = bg;
                this.color = color;
                this.number = number;
                this.dir = dir;
            }
            draw() {
                ctx.fillStyle = this.bg;
                ctx.fillRect(this.x, this.y, this.size, this.size);
                ctx.font = this.size * 0.8 + 'px arial';
                ctx.textBaseline = 'middle';
                ctx.textAlign = 'center';
                ctx.fillStyle = this.color;
                ctx.fillText(this.number.toString(), this.x + this.size / 2, this.y + this.size / 2,);
            }
        }

        size = canvas.height / 2;
        tile = new Tile(0, 0, size, "AntiqueWhite", "GoldenRod", 1);
        tile.draw()

    }); // end ready

****************************
Generalizing the Puzzle Page
****************************

In the end the kind of puzzle displayed will be determined by the server-side Django program. Here I will stick to
number puzzles but develop a means of displaying the various kinds of puzzles: 2 x 2, 3 x 3, 4 x 4 and see how they
look.

The Puzzle Array
================

This will involve moving the tiles into an array. It could be a linear array, or it could be a two-dimensional array set
up to match the dimensions of the puzzle. To start, anyway, I will keep to square arrangements of the tiles but which
would be best, a one or two-dimensional array?

I think I will start by trying a one-dimensional array. I can keep the row and column data as properties of the Tile
class and have a separate Blank class to keep track of it's row and column. This might facilitate both the drawing and
the checking of the tile positions against the server-supplied patterns for the correct solutions.

Here is some pseudocode for the initialization of the base position of various sorts of puzzles:

.. code-block:: text

    (given the number of rows and columns desired and the size of the current puzzle area)
    calculate the size of the tiles that will be needed
    puzzle_array = []       // puzzle_array is a global variable
    tile_num = 1
    for each row
        for each column in that row
            if this is not the last column in the last row
                calculate the x and y position of a tile in that row and column
                push a new tile with x, y, tile_num, size, row and column into the puzzle_array
                increment tile_num

And here is the final code that works:

.. code-block:: javascript

    function createPuzzle(tiles_on_a_side, puzzle_height) {
        size = puzzle_height / tiles_on_a_side;
        puzzle_array = [];
        var tile_num = 1;
        for (row=0; row<tiles_on_a_side; row++) {
            for (col=0; col<tiles_on_a_side; col++) {
                if ( ! ( row == tiles_on_a_side - 1 && col == tiles_on_a_side - 1 ) ) {
                    var x = size * col;
                    var y = size * row;
                    puzzle_array.push(new Tile(x, y, size, tile_num, row, col));
                    tile_num++;
                }
            }
        }
    }

    function drawPuzzle() {
        for (i=0; i<puzzle_array.length; i++) {
            puzzle_array[i].draw()
        }
    }

    createPuzzle(4, canvas.height);
    drawPuzzle();

Identifying Mouse Clicks
========================

Each tile must recognize when it has been clicked so that it, and any others between it and the blank, can be moved. I
notice that the :ref:`ChatGPT version <chat_gpt_version>` above uses two functions: one to pick up a mouse click, the
other to get the x and y position of the mouse relative to the canvas. I wonder if both are really necessary. In my
version I will attemp to use jQuery to set up the listener and see if I can get the x and y values from that. Here are
the steps:

#. Set up a listener and use an alert to see if it only responds to mouse clicks over the canvas.
#. Modify the alert to report on the x and y values.
#. Use those values to determine which tile is clicked.
#. Call the click event on that tile which, at first, only reports on the number of the tile clicked.

Here is the current code for this::

    $('#puzzle-frame').click( function(event) {
        const rect = canvas.getBoundingClientRect();
        mouseX = event.clientX - rect.left - 10; // mouse position adjusted for border width
        mouseY = event.clientY - rect.top - 10;
        size = puzzle_array[0].size;
        if (mouseX >= 0 && mouseX < canvas.width && mouseY >= 0 && mouseY < canvas.height) {
            tileX = Math.floor(mouseX / size);
            tileY = Math.floor(mouseY / size);
            index = tileY * canvas.width / size + tileX
            if (index < puzzle_array.length) {
                alert('You clicked tile number ' + puzzle_array[index].number);
            } else {
                alert('You clicked the blank.');
            }
        }


Marking Moveability
===================

I will need to create a Blank() object for this, which only needs ``row`` and ``col`` properties to mark the row and
column of its current position. Then a scan through the ``puzzle_array``, to check whether a tile is in the same row
or column as the blank and whether to the left, right, above, or below, should not be too difficult.

Here is the code that worked. It starts with a new function I added to the Tile() class::

    class Tile() {
        ( ... )
        set_motion() {
            if (this.row == blank.row) {
                if (this.col < blank.col) {
                    this.dir = 'right';
                } else {
                    this.dir = 'left';
                }
            } else {
                if (this.col == blank.col) {
                    if (this.row < blank.row) {
                        this.dir = 'down';
                    } else {
                        this.dir = 'up';
                    }
                } else {
                    this.dir = null;
                }
            }
        } // end of set_motion
    } // end of Tile definition

    class Blank {
        constructor(row, col) {
            this.row = row;
            this.col = col;
        }
    } // end of Blank definition

    function createPuzzle(tiles_on_a_side, puzzle_height) {
        size = puzzle_height / tiles_on_a_side;
        puzzle_array = [];
        var tile_num = 1;
        for (row=0; row<tiles_on_a_side; row++) {
            for (col=0; col<tiles_on_a_side; col++) {
                if ( ! ( row == tiles_on_a_side - 1 && col == tiles_on_a_side - 1 ) ) {
                    var x = size * col;
                    var y = size * row;
                    puzzle_array.push(new Tile(x, y, size, tile_num, row, col));
                    tile_num++;
                }
            }
        }
        blank = new Blank(tiles_on_a_side - 1, tiles_on_a_side - 1);
        for (var i=0; i<puzzle_array.length; i++) {         // this part can be made into a function to be called, also,
            puzzle_array[i].set_motion();                   // after moving the tiles.
        }
    }

Moving the Tiles
================

Everything is in place, I think, to begin to actually move the tiles when they are clicked. Here is the pseudocode I
developed above:

.. code-block:: text

    if the tile the user clicked can move
        save the row and column of the tile clicked
        save the direction that the tile(s) can move
        move the tiles in that direction
        update the position of the blank to the row and column saved above
        for every tile in the puzzle
            if it is in the same row as the blank
                if it is in a column less than the blank's column
                    set it's direction to right
                otherwise
                    set it's direction to left
            if it is the same column as the blank
                if it is in a row less than the blank's row
                    set it's direction to down
                otherwise
                    set it's direction to up
            if it is not in the same row or column as the blank
                    set it's direction to none

I notice that the last part of the pseudocode is already accomplished by the set_motion() method in the Tile class and
the new function I can make out of the lines commented above in the previous block of code. That mostly leaves the
section I nonchalantly mentioned as "move the tiles in that direction."

Taking baby steps I will:

#. Detect whether the tile clicked can move or not and display that with an alert.
#. Save the row and column of the clicked tile and display that.
#. Create a "moving" array containing any tiles that are going to move. Display that array. (Learn how to use log?)
#. "Move" the tiles simply by changing their row and column values. Display the new values.
#. Create and call the function to set the movement values.
#. Draw the puzzle to show the changes.

Checking Solutions
==================

I eventually got all that to work after having some problems with typos and a mysterious looping effect. Multitudes of
items kept getting added to the ``moving_tiles`` array -- possibly related to something called "variable hoisting" in
JavaScript which I haven't investigated yet. Next I want it to be able to tell if the puzzle is in the "solved"
condition.

Because there are many different ways to solve the puzzle, horizontal, vertical, forwards, backwards, spiral, etc., and
because I want the Django program to control what the current solution is, I think I will need a ``solution`` array to
hold the numbers of the tiles in the correct pattern and devise some way to test whether the puzzle has reached that
pattern. Here is the plan:

#. Create the ``solution`` array and initialize it with the vertical solution.
#. After each move call a stubbed in function to check whether the puzzle is solved.
#. Work on the ``solved`` function until it works.

Refactoring: Creating a Puzzle Class
====================================

It occurs to me that this program would be easier to write, and perhaps even more efficient, if I created a Puzzle class
to hold the tiles, moving the tiles, reporting on positions of tiles for checking solutions, etc. Some of my currently
kind of klunky functions should probably be part of the Puzzle class instead of general functions.

One advantage will be to hide the details of the implementation from the rest of the program, thus making the rest of
the program easier to write. If I should later decide to change these details, say in making the ``puzzle_array`` into a
two-dimensional array, I should be able to do so without messing up the rest of the program.

Planning the Puzzle Class
-------------------------

Initial Thoughts
^^^^^^^^^^^^^^^^

Off the top of my head I can think of the following things the ``Puzzle`` class needs to do:

#. Contain a representation of the puzzle
#. Contain properties pertaining to the puzzle such as the number of horizontal and vertical tiles
#. Create puzzles either of numbers or of pictures
#. Draw the current state of the puzzle
#. Move clicked tiles -- which may include a means of determining whether a tile can move and in which direction
#. Checking for a win

I'm not sure how to handle the ``.click`` listener. Should it be entirely outside the classes? (I doubt if that is
possible without dealing with the implementation details.) Should it be within the ``Tile`` class?, the ``Puzzle``
class?, some combination of both? I don't know. Perhaps looking over the ``game.html`` file from the W3Schools tutorial
will help.

I notice, by looking at *game.html*, that its ``myGameArea``, which more or less corresponds to my Puzzle Class, is an
object rather than a class. This object has functions as well as properties. This might be a approach to take as well.
On the other hand, that might just be an earlier example from before JavaScript even had classes. W3Schools reports that
`JavaScript classes came in 2015 <https://www.w3schools.com/js/js_classes.asp>`_ as a template for creating objects. I
notice that the game tutorial did not use classes at all. That strengthens my belief that the game example comes from
that earlier period. What they called ``myGameArea`` was an object variable and they also used a ``component`` function
to create game objects. The ``component`` function had other functions within it, as did the ``myGameArea`` variable,
both seeming to serve the purpose of class methods. I will stick with creating a ``Puzzle`` class.

More Developed Ideas
^^^^^^^^^^^^^^^^^^^^

I need to be more systematic about the properties and methods of the ``Puzzle`` class. Here I will try to generate a
list of all the properties and methods I will need not only by looking at the list above, but going through my current
code to see the existing variables, constants and functions that could better be properties and methods of the
``Puzzle`` class.

+-----------------------------------------------------+
| The Puzzle Class                                    |
+=====================================================+
| | **Properties:**                                   |
| |     canvas                                        |
| |     puzzle_tiles?                                 |
| |     start_position                                |
| |     solution                                      |
| |     h_tile_count                                  |
| |     v_tile_count                                  |
| |     tile_size                                     |
+-----------------------------------------------------+
| | **Methods:**                                      |
| |     draw()                                        |
| |     move_tiles()                                  |
+-----------------------------------------------------+

Implementing the Puzzle Class
-----------------------------

I think I should do this incrementally but I'm not sure how to do so. I have copied my existing, and working, JavaScript
from *puzzle-two.html* to *puzzle.html* and have started writing the ``Puzzle`` class but am not certain how I can do
it as a step-by-step process keeping it working along the way.

What I will try to do is first create a constructor that simply reproduces what the ``createPuzzle`` function already
does. Then, step by step, try to add more and more functionality to the ``Puzzle`` class.

The Puzzle Class Constructor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I will start by simply duplicating the functionality of the ``createPuzzle`` function, see if it works, then add other
features to it one by one such as:

#. Letting it calculate the size of the canvas instead of having it as a parameter.
#. Giving it a ``start_map`` object for the original placement of the tiles
#. Giving it a ``solution_map`` object for the correct placement of the tiles
#. ... other things I will think of later

Second Attempt at Implementing the Puzzle Class
-----------------------------------------------

My first attempt to do a step-by-step process, above, was to try to keep the program working while adding one thing at
a time to the ``Puzzle`` class. That wasn't working out. Changes I wanted to make within the ``Puzzle`` class kept
interfering in strange ways with existing code outside that class and I was spending too much time trying to get things
to work that were going to be changed anyway.

I decided to try a different approach:

#. Comment out the pertinent code outside the ``Puzzle`` class
#. Build the ``Puzzle`` class step-by-step, checking it every step of the way -- not as a fully functioning program, but
   more or less according to the following pattern:

   A. That the class is constructed properly according to the given start pattern
   #. That it can display the puzzle
   #. That it can identify which tile is clicked
   #. That it can move that tile, or those tiles, in the proper direction.

Puzzle Class Constructor
^^^^^^^^^^^^^^^^^^^^^^^^

This is a chance, if I should decide to take it, to try to implement the data structure for the puzzle differently. I've
been using a single dimensional array, both here and in my original *FifteenTest* project, but here, anyway, it has been
complicating my life by requiring that the tiles keep track of their row and column for instance, and making it
necessary to have a special function to work from the current row and column of a tile backwards to it's index in the
``puzzle_array``. I wonder if I might create a one-dimensional array that contains the actual tiles, including the
blank, and a two-dimensional array that simply pushes the indices to the tiles around. I will try that here.

I can keep the name ``puzzle_array`` for the one-dimensional array and, if it always has the blank in position zero, the
number for each tile will correspond to its index, thus reducing the parameters of the ``Tile`` constructor to x, y,
dir, and type.

That raises the question, however, as to how the correct solution can be discerned. Perhaps I can use ``grid`` as the
name of the main puzzle grid and ``solution_grid`` as the name of the solution grid. If each only contains the tile
numbers, which correspond to each tile's index in the ``puzzle_array`` checking for a win could be as easy as
`` if (grid == solution_grid) { ... }``

Here is the ``Puzzle`` class constructor in pseudo code:

.. code-block:: text

    puzzle_map: side_tiles: n, // the number of tiles on each side,
                start_positions [ <list of numbers representing the initial positions of the tiles> ],
                solution [ <list of numbers representing the correct positions of the tiles> ]

    constructor(puzzle_map, canvas)
        create ``tile_array`` tiles for every number in the puzzle (side_tiles * side_tiles -1), starting with a blank
        set pointer to 0
        for each row in side_tiles
            for each column in side_tiles
                place the value start_positions[pointer] at that position in grid
                set the x and y values of the corresponding tile in ``tile_array``
                place the solution[pointer] value at that position in solution_grid

Now the question is whether the tile size is something for the ``Tile`` class to keep track of or if it needs to come
from the ``Puzzle`` class. Currently the ``Puzzle`` class calculates it to use in creating the tiles but does not save
it as an instance variable. It makes sense that it would calculate it, since it depends on the size of the canvas and
the ``side_tiles`` count of the current puzzle. It is also using it to calculate the positions of each of the tiles but
that seems more like something the ``Tile`` class can do for itself with just the row and column information. I will
implement that.

The Puzzle.draw() Function
^^^^^^^^^^^^^^^^^^^^^^^^^^

This was very easy to write, though I had to make a bit of a change to the ``Tile.draw_tile()`` function to allow for
the blank being included in the ``puzzle_array``. Here is the code for ``Puzzle.draw()``::

    draw() {
        for (let i=0; i<this.puzzle_array.length; i++) {
            this.puzzle_array[i].draw_tile();
        } // end of iteration through tiles in puzzle_array
    } // end of draw()

Identifying Clicked Tiles
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``.click()`` method will need to be part of the main program. The question as to which tile is getting clicked, and
what to do about it, should be answered by the ``Puzzle`` class.

There is some filtering that needs to be done to convert the raw mouse position values to the coordinates of the
``#puzzle-frame`` and that the click actually occurred within the ``#puzzle-frame``. Once that is done, the resulting
values can be sent to a method in the ``Puzzle`` class to identify and process clicks.

All I want to do for now is make sure the puzzle can report, say, the value and position of the tile clicked. Here are
the steps:

#. Write a ``.click()`` responder to report on the raw values of the position of the mouse pointer.
#. Convert the raw position to ``#puzzle-frame`` coordinates.
#. Check to see the click was within the ``#puzzle-frame``.
#. Send the filtered position to the ``Puzzle.process_click(x, y)`` method.
#. Convert the x and y values to col and row respectively.
#. Use console.log to display the corresponding tile index from the grid.
#. Use console.log to display the corresponding tile from ``puzzle_array``.

I rethought my decision concerning the ``size`` variable. I needed it in the ``Puzzle`` class to identify which tile was
clicked and realized that having ``size`` information for each tile was rather silly since they all had the same size.
It does make sense that the puzzle would keep track of the size of its tiles and can send that to the ``Tile`` class
when necessary.

Moving Clicked Tiles
^^^^^^^^^^^^^^^^^^^^

I will try to work out, here, an algorithm for moving the clicked tile and any others in its row and column if they are
lined up with the blank. Previously I used a scan of all the pieces and saved in each tile its possible direction of
motion or ``null`` if it could not move. I'm not sure that will be necessary. I should be able to do that while
processing the clicked tile.

The row and column containing the blank should be easy to find since it is in ``grid`` as the zero index. Finding out if
the clicked tile is in the same row or column and in which direction should also not be too difficult. Then I will have
to select the tiles for motion and actually move them. Here is my first attempt to express that as a step by step
process:

#. Scan the grid for the row and column of the blank.
#. Determine whether the clicked tile is lined up with the blank.
#. Determine the direction of motion up, down, left or right and set the motion parameters accordingly (delta x or delta
   y) for it will apply to all of the tiles.
#. For each tile that should move, apply the motion parameters (+1 or -1 to the row or column in grid.) Then move the
   blank to the former position of the clicked tile.
#. Recalculate the positions of the moved tiles and apply to ``puzzle_array``.
#. Redraw the puzzle.

While writing the steps above the questions that nagged at me were:

#. How to actually move the tile indices in the ``grid``. This will involve some swapping I suppose.
#. How to recalculate the positions of the moved tiles. I could scan through the whole grid, or apply the changes at the
   same time that I move the indices in the ``grid``. But that makes me wonder, again, whether I really need the
   ``puzzle_array``.
#. Should I move the several aspects: locating the blank, moving the indices, repositioning the tiles, etc., to their
   own functions, called only once, or make one big ``process_click`` method?

Here is a failed attempt to write the pseudocode:

.. code-block:: text

    locate blank_row and blank_col
    if clicked tile's row matches blank_row
        set delta_col and delta_y to 0
        if clicked_row < blank_row
            set delta_row to +1 and delta_x to +size
        else
            set delta_row to -1 and delta_x to -size
        for all the tiles from the clicked tile to the blank tile
        ... ???

I decided, instead, to take another step-by-step process:

#. Write code to locate and report on the row and column of the blank.
#. Have a clicked tile report true or false as to whether it is lined up with the blank.
#. Calculate direction of motion: either forward or backward along either rows or columns.
#. Create the means of moving single columns:

   A. Create the means of moving a single tile down.
   #. Create the means of moving a single tile up.
   #. Create the means of moving multiple tiles up or down.

#. Create the means of moving single rows.
#. Create the means of moving single columns.
#. Devise a way to check to see if the puzzle is solved.

Interlude
=========

I now have a working version of the numeric puzzle but I noticed some things that need to be addressed:

#. Something should happen to prevent further action when the user has solved the puzzle. (I decided to save this for
   later. Partially because I may want to be able to easily shift a puzzle from unsolved and solved states for testing
   purposes and partially because what happens when the puzzle is solved will also involve the Django program.)
#. I should look at optimizing and clarifying the code. I'm not sure I need two calls to ``this.move()`` in the
   ``process_click()`` method for instance. I can probably do with just one. (I was able to do with just one.)
#. It seems that the ``Puzzle.draw()`` method should be able to set the x and y positions of the tiles according to
   their grid positions which makes me wonder, once again, whether I even need the ``puzzle_array`` or even if I need
   the ``Tile`` class. (I decided to keep the current data structure for now, changing it would complicate the
   ``Puzzle.draw()`` method and it all may affect adding picture puzzles to the program later.)
#. Considerable amounts of code can be removed from the program since they are not being used:

   A. Lines that have been commented out.
   #. Methods in the ``Tile`` class that are no longer being used.

After doing that clean-up I would like to add sound:

#. Clicks for moving tiles or groups of tiles.
#. A winning sound or a random choice of winning sounds for when a user solves a puzzle.

After that it will be time to figure out how to make picture puzzles.

Preliminary Thoughts on Making Picture Puzzles
==============================================

I first thought of installing the Python Pillow module but that would mean I would have to do all the image processing
in Django on the server and somehow send the results to the JavaScript on the client machines. Then I wondered about
doing the image processing in JavaScript and it looks fairly easy to do.
`One source <https://stackoverflow.com/questions/8912917/cutting-an-image-into-pieces-through-javascript>`_ says it can
be easily done just using another canvas, JavaScript generated in this case. Chapter 7 of *JavaScript & jQuery* may also
be useful, especially when it comes to putting the picture pieces into html tags.

It might be useful to try to outline exactly what I want to happen when a picture puzzle is called for. Here is my first
attempt:

#. Receive the filename of the image. (In my current testing and development mode this can just be setting a variable.)
#. Load the image and use the loaded image to create the number of pieces indicated by ``side_tiles * side_tiles``.
#. Create the blank and tiles 1 through ``side_tiles * side_tiles - 1`` with a 'pic' type.
#. Somehow point each tile to it's corresponding picture piece.
#. At some point you will have to draw the tile with its picture piece. Hopefully you will be able to add shading to it.

The last couple of steps are so vague that I know I'm not ready to do any coding yet. I have to get a clearer idea of
how the tiles are going to be drawn when they are of the "pic" type.

After "sleeping on it" overnight and looking over some documentation of JavaScript's ``.drawImage()``
`method <https://www.w3schools.com/jsref/canvas_drawimage.asp>`_, I have clearer ideas of what needs to be done. Most
of the work will be done in the ``Tile.constructor()`` method and the ``Tile.draw_tile()`` method. The constructor will
do the work of dividing the picture up into smaller pieces, saved as "DOMStrings" in the Tile itself. The drawing
method will have to use those "DOMStrings" to draw the actual images. This may require an <img> tag to be created in
the html code but I'm not sure about that yet. Maybe it's time for a chat with ChatGPT::

    I have a JavaScript Array of DOMStrings for several images. I want to display those images in various places on an
    existing <canvas>. How do I do this?

    You can achieve this by first loading the images from the array of DOMStrings and then drawing them onto the canvas
    at desired positions. Here's a step-by-step guide on how to do this:

    1. Load the images from the array of DOMStrings.
    2. Once the images are loaded, draw them onto the canvas at desired positions using the `drawImage()` method of the
       canvas context.

    Here's a sample code demonstrating this:

    ```javascript
    // Assume imagesArray is your array of DOMStrings for images
    // canvas is your existing canvas element
    const canvas = document.getElementById('myCanvas');
    const ctx = canvas.getContext('2d');

    // Load images from the array of DOMStrings
    const images = [];
    let loadedImagesCount = 0;
    for (let i = 0; i < imagesArray.length; i++) {
        const img = new Image();
        img.onload = () => {
            loadedImagesCount++;
            if (loadedImagesCount === imagesArray.length) {
                // Once all images are loaded, draw them onto the canvas
                drawImages();
            }
        };
        img.src = imagesArray[i];
        images.push(img);
    }

    function drawImages() {
        // Clear the canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Define positions for drawing images
        const positions = [
            { x: 100, y: 100 },
            { x: 200, y: 200 },
            { x: 300, y: 300 }
            // Add more positions as needed
        ];

        // Draw images at specified positions
        for (let i = 0; i < images.length; i++) {
            const position = positions[i];
            ctx.drawImage(images[i], position.x, position.y);
        }
    }
    ```

    In this code:

    - We first load all images from the array of DOMStrings using the `new Image()` constructor and set their `src`
      attributes to the corresponding DOMStrings.
    - When each image is loaded (`onload` event), we keep track of the number of loaded images (`loadedImagesCount`).
      Once all images are loaded, we call the `drawImages()` function to draw them onto the canvas.
    - Inside `drawImages()`, we clear the canvas and define positions for drawing images. Then, we use the
      `drawImage()` method to draw each image onto the canvas at the specified positions.

From this I see that it is necessary to convert the DOMStrings into JavaScript Images and that these Images can be drawn
directly by ``ctx.drawImage()``. Perhaps I should create the Images in the ``Tile.constructor()`` and save them in the
Tile instead of the corresponding DOMString. I will try that first. Here is the plan:

#. Create a suitable image for the puzzle 300px x 300px. Save it to *fifteen/static/fifteen/images*.
#. Receive the filename of the image. (In my current testing and development mode this can just be setting a variable.)
#. Add code to ``Puzzle.constructor`` to create puzzle pieces as JavaScript Images and save them to the Tile class.
   (Also edit the code so that ``Tile.image = null`` for numeric puzzles.

   A. Change the Tile constructor to include the ``image`` property.
   #. Change the code for numeric puzzles so that the ``image`` property is set to null.
   #. Add to the code for pic puzzles so that:

      i. A new square canvas is created with ``this.size`` sides.
      #. A new ``context`` is created to create the puzzle pieces.
      #. A new Image is created for each puzzle piece.
      #. The Image is stored in the Tile along with the other parameters.

#. Edit the code in ``Tile.draw_tile()`` to draw the images in their proper places on the grid.

I had considerable trouble with:

#. Getting the right puzzle pieces to appear in the right places. I was creating them in the loop that created the grid
   but it needs to be in the loop that creates the puzzle_array and the corresponding row and column needs to be
   calculated from the value of i, being careful to skip the blank.
#. Dealing with the asynchronus nature of JavaScript code. I was often trying to use the image before it completely
   loaded. ChatGPT helped me learn where the ``Image.onload`` needed to go.
#. When I added the "shading" to the tiles ChatGPT also helped me figure out how to set the strokeStyle to an rgba
   setting. I learned that numerical expressions being concatenated to strings need to be within parentheses so that
   they will be read as expressions. I had also neglected to declare the index, i, of the second loop as a variable. I'm
   not sure why that would give me the results I was getting -- the lower right shading being applied on the upper left
   of all but the first tile, but declaring i as a var solved the problem.

Solving a Picture Puzzle
========================

When a picture puzzle is solved I would like the entire image to fade into the puzzle space without the tile lines.
I would also like some audio to play, both a "win" sound, which I imagine as an etherial harp-like sound as the
image is fading in, and some kind of story about or message from the person or people pictured.

I think I'll try to do it by adding an ``<img>`` tag to the html and have it be hidden. Then, when the puzzle is solved,
do whatever it takes to fade that image in.

First I will have to position it over the space of the image in the puzzle. I should be able to do that with CSS, though
it might be useful to have it appear at the beginning and then fade to the scrambled puzzle tiles. *As it turned out, I
used css to size the image and JavaScript to position it.*

Fading the image out at the beginning and fading it back in when the puzzle is solved turned out to be easy, along with
playing a sound::

    if (JSON.stringify(this.grid) == JSON.stringify(this.solution_grid)) {
        puzzle_reveal.play();
        $('#solution-picture').fadeIn(3000);
    }

***********************
Interacting with Django
***********************

Now that the basic puzzle is working I want to get it to interact with the server through Django. This will involve:

#. Creating and selecting puzzles in Django.
#. Sending the puzzles from Django and receiving them on the client machine with jQuery/Ajax.
#. Designing and developing the game aspects:

   A. Having the solution visible
   #. Creating a timer
   #. Sending game results back to the server.

#. Developing the models that will be needed for the game.

Sending and Receiving Numeric Puzzles
=====================================

I think the best place to start, or at least the place I am most interested in right now, is sending a puzzle from
the server through Django and receiving it on the client machine through Ajax. Currently the puzzles are hard coded in
the JavaScript. I need to review Boggle to see how puzzle information can be initiated when coming from the server.

Here are some steps to follow:

#. Study Boggle to see how it used Ajax to get information from the server.
#. Send a self-created puzzle to the puzzle page.
#. Generate random number puzzles and send them to the puzzle page.
#. Send a randomized picture puzzle to the puzzle page.

How Games are Initialized in Christmas Boggle
---------------------------------------------

When the *game_play.html* page is opened, *christmas_boggle.js* is started and it initializes the game with a
``$.post()`` command. It posts back to the ``request_url`` a JavaScript Object with the the page's
``csrfmiddlewaretoken`` and a ``command`` of "init_page".

Boggle's ``GameView`` uses that to determine the player's next game and return a ``JsonResponse`` containing a
``game_info`` dictionary with all the pertinent game information.

Back on the client, the ``setNextGame()`` function is called with the game information and sets a number of variables
pertaining to the implementation of the game in JavaScript. Once that is done the function ``setInterface()`` is called
to manage the control portion of the page, making sure the right things are visible.

The game then waits for some interaction from the user to start a game.

Thoughts on How to Initialize Fifteen Puzzles
---------------------------------------------

I think I would like to use ``$.get()`` rather than ``$.post()`` since I am clearly GETTING information from the server
rather than posting it. Also, since there are a lot of utility programs in *boggle.views.py* I would like to separate
them out into one or more other files. They could be named *tools.py* and/or *game.py*.

I would also like to test the implementation carefully along the way, not with official unit tests or functional tests
as I was trying for a while, but simply using ``alert`` and ``print`` to verify that things are going according to plan.

Also, this is as good a time as any to pull the javascript out of the html file and read it in separately.

Implementing Initialization
---------------------------

Establishing Communication
^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is my plan:

#. Copy/paste the JavaScript portion of *puzzle.html* into *fifteen/static/fifteen/scripts* as *fifteen.js*. Verify that
   it is still running using the browser.

   A. For some reason I don't remember, it can't find the audio files. They seem to have to be defined at the end of
      the html file.
   #. The same is true for the image file I am temporarily using. (One of my baby pictures.)
   #. Once fixing this I noticed that the image did not show up on the puzzle pieces until the second try. I am going to
      have to try to figure out why and then fix that too.

#. Create an initialization section in *fifteen.js* containing only an ``alert`` to ensure that it is being used.
#. Modify ``puzzle_view()`` to print ``request.GET``.
#. Put a ``$.get()`` call in the initialization section with some fake entry to be displayed by the view.

   A. I could not display the fake entry with the expected ``request.GET['command']`` I could only retrieve it with
      ``request.GET.get('command')``. This could be a major problem if it means I have to change a lot of my old
      Christmas website code! Hopefully there is something else going on that I don't yet see.
   #. Ah! I see the problem! When ``puzzle_view()`` is originally called from the entry page or, in my case, the refresh
      button, request.GET is empty. If I try to find a 'command' key in an empty QueryDict it will generate a KeyError.
      using ``.get('command')`` bypasses this because, I think, it returns ``None`` when the key doesn't exist. I am
      using it in an ``if`` statement and ``None`` certainly does not equal the strings I testing it against.

Sending a Numeric Puzzle
^^^^^^^^^^^^^^^^^^^^^^^^

First I have to create the numeric puzzle in Django and then send it to JavaScript to be read and used. Here is my plan:

#. Change the command to "get_puzzle" in *fifteen.js*.
#. When the command "get_puzzle" is found in ``puzzle_view()``, print a response.
#. Change ``puzzle_view()`` so that an actual puzzle is sent instead. Use an ``alert`` in JavaScript to display, through
   ``JSON.stringify`` what was sent.
#. Use that data to initialize the puzzle.

   A. I had to put the creation and drawing of the puzzle in the ``$.get()`` callback function.
   #. I will have to make a lot of changes to the way image puzzles are handled. Currently I've just put the image out
      of the way by adding ``d-none`` to its Bootstrap class.

Making a Sad Mistake
--------------------

At this year's priest retreat I added the ability for Django to actually create random puzzles and then to be able to
create random puzzles of various sizes. I also created *tools.py* as a place for these helper functions to live and, in
the process figured out why, when using ``$.get()`` instead of ``$.post`` I need to use ``request.GET.get()`` instead of
``request.GET[]`` on the Django side. I documented all of it in this file.

Then, when preparing to return back home, I overwrote the old version of this file into this one, deleting all of that
documentation!!! Because I never enabled version control it is just gone, never to be seen again. The part I regret
most is losing the reason that ``request.GET.get()`` needs to be used. I hope it will come back to me.

Sending and Receiving Pictorial Puzzles
=======================================

Now the challenge is how to send pictorial puzzles from Django to be received by *fifteen.js*. I decided to "consult"
with ChatGPT to get some ideas. Here are the results:

.. code-block:: text

    User
    How do I go about loading an image into JavaScript/jQuery through an Ajax call?

    ChatGPT

    You can load an image into JavaScript/jQuery through an Ajax call by using the $.ajax() function or
    the shorthand methods like $.get() or $.post(). Here's a basic example of how to do it:

    javascript

    $.ajax({
        url: 'path/to/image.jpg',
        method: 'GET',
        responseType: 'blob', // Set the response type to blob
        success: function(data) {
            var imageUrl = URL.createObjectURL(data); // Create object URL from blob data
            // Now you can use imageUrl to display the image
            $('#image-container').html('<img src="' + imageUrl + '" alt="Loaded Image">');
        },
        error: function(xhr, status, error) {
            console.error('Error loading image:', error);
        }
    });

    In this example:

        url specifies the path to the image.
        method is set to 'GET' since you are fetching the image.
        responseType is set to 'blob' to indicate that the response will be in binary format.
        In the success callback, data will contain the image data in blob format. You can create a URL
        for the blob using URL.createObjectURL(data) and then use this URL to set the src attribute of
        an <img> element.
        In case of an error, the error callback will handle it.

    Ensure that the path specified in the url parameter is correct and accessible from the location
    where your JavaScript code is running. Additionally, make sure you handle CORS (Cross-Origin
    Resource Sharing) if the image is hosted on a different domain.

    User
    How would I do it using $.get() and if the image file is on the server and will be determined by
    a function on the server?

    ChatGPT

    If you're using $.get() and the image file path is determined dynamically on the server side,
    you can make an AJAX request to a server endpoint that returns the image path. Here's how you
    can do it:

    Assuming you have a server-side function that returns the image path based on some parameters,
    you would make an AJAX call to that function and then load the image accordingly.

    JavaScript/jQuery code:

    javascript

    // Make an AJAX call to the server-side function
    $.get('/get_image_path', { /* any parameters required */ }, function(response) {
        // Assuming response contains the image path
        var imagePath = response.imagePath;

        // Create an image element and set its src attribute to the retrieved path
        var $img = $('<img>').attr('src', imagePath).attr('alt', 'Loaded Image');

        // Append the image element to a container
        $('#image-container').html($img);
    })
    .fail(function(xhr, status, error) {
        console.error('Error fetching image path:', error);
    });

    In this code:

        The $.get() function sends an AJAX GET request to the /get_image_path endpoint on your server.
        You can pass any necessary parameters to the server-side function as the second argument of
        $.get().
        The function(response) is the success callback, where response contains the data returned
        by the server. You would extract the image path from this data.
        Then, you create a new <img> element using jQuery, set its src attribute to the retrieved
        image path, and set an alternative text using alt.
        Finally, you append the image element to a container in your HTML (identified by
        #image-container).

    Make sure that the server-side function /get_image_path returns the image path correctly. Adjust
    the endpoint URL and parameters according to your server-side implementation.

    User
    Can you suggest a Django view function for `/get_image_path`?

    ChatGPT

    Certainly! Below is a simple Django view function that could be used for the /get_image_path
    endpoint:

    python

    from django.http import JsonResponse

    def get_image_path(request):
        # Logic to determine the image path based on request parameters or any other criteria
        # For demonstration purposes, let's assume a static image path is returned
        image_path = '/path/to/your/image.jpg'

        # Construct a JSON response containing the image path
        response_data = {'imagePath': image_path}

        # Return the JSON response
        return JsonResponse(response_data)

    In this Django view function:

        JsonResponse is used to construct a JSON response containing the image path.
        You would replace the logic inside get_image_path to dynamically determine the image
        path based on your requirements. This could involve querying a database, processing
        request parameters, etc. For simplicity, I've just used a static path as an example.
        Ensure that the URL pattern for this view function is correctly configured in your
        Django urls.py file.

    Here's how you might configure the URL pattern in your urls.py:

    python

    from django.urls import path
    from .views import get_image_path

    urlpatterns = [
        path('get_image_path', get_image_path, name='get_image_path'),
        # Other URL patterns for your Django application...
    ]

    This setup will map the /get_image_path endpoint to the get_image_path view function.
    Adjust the URL pattern according to your project's URL structure.

This suggests something to me. Instead of complicating the ``puzzle_view()`` function with numerous commands I could
call utility functions within that file to accomplish each task. The tradeoff would be, it seems, having to create a
number of new url patterns to process each of the different AJAX calls.

Blocking Out the Details
------------------------

I think it will be helpful to outline exactly what needs to be done on the server side and on the client side to send
and receive a pictorial puzzle. Here is my first attempt to do this for a testing implementation:

#. On the Server Side:

   #. When the view is first entered the type of puzzle and its image are determined by the server system.
   #. Subsequent ajax calls can change the size of the puzzle from 2 x 2 up to 5 x 5.

#. On the Client Side:

   #. The success callback function should 

*********************
Questions and Answers
*********************

During the development above I noted certain questions or topics for future study. Here is a record of what I learned.



.. note:: Something to Investigate: the difference between setting canvas width and height in the <canvas> tag and in
          css. Which does JavaScript use? <canvas> is a DOM element so information about it should be available for
          manipulation.

.. note:: Learn about variable hoisting and try to determine whether that is a likely cause for the browser getting
          hung up in certain circumstances while trying to move tiles.

console.log Not Always Printing
===============================

I noticed that the ``console.log`` function wasn't always printing things if they were simply repeated. I discovered
that, at least on Firefox, it does log them but doesn't print them directly to the console. Instead it collects them
together and gives a count of how many of the same strings are being logged.

Mozilla has some `documentation <https://developer.mozilla.org/en-US/docs/Web/API/console/log_static>`_ on
``console.log`` that doesn't discuss this but does give some useful information. I think some of it should go into my
"Infrequent Commands" project.
