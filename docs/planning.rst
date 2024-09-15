###########################
Planning the Fifteen Puzzle
###########################

January 10, 2024

I originally wrote about this idea in one of my Christmas 2023 documents but I want to do the detailed development here
and then copy the whole app over to Christmas 2024 when the time comes. Meanwhile, I hope to learn a number of things
in the process of development. Here is a (probably) parital list:

#. Using Test-Driven Development (TDD) on my own.
#. Finding out what's new in the Django 5.0 version of authentication and why I couldn't get it to work when
   deploying Christmas 2023.
#. Gain more experience with the Caddy server.
#. Learn how to cut up images in python to make them into fifteen smaller images.
#. Learn how to do css, javascript, or some other means of animating the pieces.

*****************************
Broad Overview of the Program
*****************************

In this section I want to consider and decide upon the overall working of the program. The next section will deal with
a little more specific approach, one that can, I hope, be translated into a set of functional tests. At this level, the
questions that need to be answered are:

#. What does the player see when first entering the game? Should the game be played on that page, as in Christmas
   Word Game, or is it more of a gateway to the game-playing page as in Christmas Jumble and Christmas Boggle.
#. Should there be different versions of the game, such as a Fifteen Puzzle Race, an unscramble family members option,
   or an unscramble ancestors option. Maybe I can think of others too, as in that Fifteen Puzzle with letters I still
   have.
#. What choice, if any, should the player have as to which game is played? If they have a choice, how do they make it?

That should do for a starter, though I know that pondering these questions will probably lead to others.

Overall Look and Feel
=====================

The basic question is should there be one main page with ancillary detail pages, as in Word Game, or two (or more) pages
with ancillary detail pages to serve as kind of a buffer before starting a game. An advantage of the first is that a
player gets right to it without a lot of extra clicking. A disadvantage is that I would have to come up with some
neutral puzzle (a correctly solved Fifteen Puzzle?) to display before the game is actually started.

An advantage of having a buffer page, so to speak, is that it can display the scores and, if there are other parameters
players can set, they can set them here before entering the puzzle page. This page makes a good place to keep the
directions and this also opens the possibility of having different html pages for the different types of games.

Just from writing the above I can tell that I prefer the second, multi=page, approach.

Game Versions
=============

I would like to have different versions of the game. Here are some ideas.

#. Solitaire version: Players solve the number version of the Fifteen Puzzle from various, spontaneously generated,
   starting positions. There will be no record kept of their games but they can choose to store their current game and
   come back to it later. Maybe they can save more than one game by giving each a name. Perhaps they will also have the
   opportunity to solve other kinds of number games: such as reversing the order, the spiral, evens and odds, etc.
#. Fifteen Puzzle Race: Players compete to finish Fifteen puzzles in the shortest time. Each player sees the same
   starting position for the numbers in each game. They should be able to save their game and come back to it later.
   Maybe that can be made automatic regardless of how they leave the page. (But perhaps not. There may be some necessary
   restrictions on this.
#. Family Picture Puzzles: Facial shots of family members can be used as Fifteen Puzzles. Once each is solved there
   should be some kind of reward. The players see, or perhaps hear, a Christmas greeting from that family member, or
   their answer to a Christmas question of some sort.
#. Ancestor Puzzles: Like the family pictures version except with pictures of ancestors. The prize can be a story from
   Janet about that ancestor.
#. One of a Kind word puzzle: based on the promotional puzzle I still have.

Choices
=======

I see several options here:

#. A random type of puzzle is picked for each day.
#. They can choose between Puzzle Races and a random puzzle.
#. They can choose between solitaire, races or a random family/ancestor puzzle or the word puzzle.
#. They can choose any of the five (or however many I end up with) types.

I think I want to give the players complete choice over what kind of puzzle they want to play, but I don't want the game
to have so many choices that it becomes too vast a playground to get interested in.

Which brought another consideration into my mind.

Making it a Fun Game
====================

At some point I am going to have to consider what will make the game most fun to play and make the players want to keep
coming back. This game can take some time to solve. Chess champion, Bobby Fischer was timed to solve it in 25 seconds,
considered an incredibly fast speed. (See https://www.youtube.com/watch?v=QxvnEwvgfeI starting around 11:30.) I'm not
sure what the average time might be, or how long it would take someone who is not familiar with it at all. It could be
quite frustrating and people would avoid it. I'll have to think about this. Perhaps I can make a 3 x 3 version for the
faces. Perhaps I could have categories of people according to their self-described experience, or assign them to
different levels of puzzle difficulty based on how they solve certain puzzles.

But the psychology of the game in this context is what is important. There have to be reasons to want to come back and
play some more. What reasons?

My Own Thoughts
---------------

I thought of doing an internet search on "What makes puzzle games fun" or some such thing. I will probably still do that
but even in phrasing the question an answer popped into my mind: Levels! People like to start simple and get some early
success, but they also like to be challenged later on. Here is a rough draft of the levels I've thought of so far:

Lv | Description

#. A 2 x 2 grid with numbers 1, 2 and 3.
#. A 3 x 3 grid with numbers 1 through 8.
#. Some 3 x 3 grids with babies and the very young saying "Merry Christmas." (The babies will say it in their own
   language.)
#. A 4 x 4 grid with numbers 1 through 15 -- the original Fifteen puzzle.
#. Some 4 x 4 grids with older kids saying what they like about Christmas. (All parts with kids need parental
   permission.)
#. Some 4 x 4 grid with ancestors telling their stories. (Janet's help needed here.)
#. The Race. A set of pre-established 4 x 4 grids so that family members can strive to solve it in the least amount of
   time. Perhaps they can replay particular puzzles to improve their score -- or beat another family member.
#. The Race Continued. A set of pre-established 4 x 4 grids and a number of different variations on how they must be
   solved: backwards, vertical, spiral, red and white, etc.
#. Timed play. A set of pre-established 4 x 4 grids, with various required solutions, that must be solved within a given
   time. (This might require knowing, or at least estimating, the minimum time needed to solve a particular puzzle.

Internet Search
---------------

I searched on "How do I make puzzle games fun?" and looked, at least partially, at these two sites:

#. https://machinations.io/articles/how-to-design-a-puzzle-game
#. https://auroriax.com/puzzle-explorable/

The second one had some actual games as examples and I was getting drawn in, but I think I'm at least on the right
track with the levels ideas I expressed above.

.. _detailed_overview:

***********************************
More Detailed Overview, Section One
***********************************

This section will help me develop an overview of the basic working of the program that can be translated into some of
what Harry Percival calls Functional Tests. This first section will focus on the basic functionality of the game. Once
this is in place there will probably be a need to use :abbr:`TDD (Test-Driven Development)` to make sure more than one
player can play, that the proper things are being saved to the database, that levels are proceeding properly, that
scoreboards are displayed with the proper scores, etc.

I will use the narrative style of description from the player's point of view.

Authentication
==============

Charlie goes to *fifteen.jatmorris.org* (during development *localhost:8000*) and see's a login page.

He enters his username and password into the input boxes and then presses Enter.

He comes to the fifteen app's entry page with "Christmas Fifteen" on the title tab.

The Entry Page
==============

He sees a message that welcomes him to the game for the first time and informs him that he will start at Level 1 when he
presses the "Play" button.

He clicks the "Play" button and comes to the game page for Level 1.

Level One
=========

Charlie sees a very simple puzzle made with a 2 x 2 grid and containing the numbers 1, 2 and 3 but in the wrong places.

He also sees a "map" off to the side that tells him where each number is supposed to go.

There are instructions telling him to click or tap on a number next to the blank space to get that number to move into
the blank.

Charlie clicks or taps on the "1" tile and it moves up.
He clicks on the "2" tile and it moves to the right.
He clicks on the "3" tile and it moves down.
He clicks on "1" again and it moves to the left.
When he clicks on the "2" again it moves up.

Since all the numbers are now in their proper place, Charlie is rewarded with some sort of champion sound.

A box appears telling him how long it took him to solve the puzzle.

The box also includes buttons where he can choose to play the level again to improve his time or go to the next level.

He clicks the "Play Again" button and the page resets to its initial appearance except that the "Next Level" button is
still visible.

He changes his mind and clicks the "Next Level" button and he enters the page for Level Two.

***************************************
Ready to Start Initial Functional Tests
***************************************

I think I have quite enough to keep my busy for a while with just this much of the program. I really do need to test my
approach to authentication in Django 5.0 and the actual playing of the game will be interesting to figure out how to
implement and how to test. This seems like a good place to start writing some tests. I decided to put that into
:ref:`a separate document <developing_tests>`.

Thought Collection
==================

Leaving Puzzles
---------------

#. Players should be able to leave a puzzle and come back to it later.
#. Any timers involved should remember the current time if a player leaves a game.
#. The current state of the puzzle should also be remembered.
#. This means, however clunky it is, I will have to catch other means of leaving the page besides the prescribed ones.
   If they do choose to leave this puzzle will be crossed off his or her list, if it is a tournament puzzle, and cannot
   be re-entered. This could get complicated!