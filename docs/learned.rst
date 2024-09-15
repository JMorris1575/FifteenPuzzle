###################
Things I've Learned
###################

I thought it would be good to keep track of the things I've learned in this project for future reference. Off the top
of my head I can think of several categories, but I will try to keep up the list below as I think of new ones.

#. :ref:`Html <html>`
#. Bootstrap
#. CSS
#. Django
#. Python

.. _html:

****
Html
****

The <i> and <span> Elements
===========================

The ``<i>`` tag (or the ``<span>`` tag), is used by Font Awesome to insert its icons as font characters. I wondered
what, exactly, they do. Here is what I learned:

The <i> Tag
-----------

The <i> tag is used to make text stand apart somehow, as in *italics* which is what the "i" stands for. It is an inline
element.

The <span> Tag
--------------

The ``<span>`` tag is used like the ``<div>`` tag except that ``<span>`` is an inline element where ``<div>`` is a block
element. It simply provides a way to mark up a portion of text or other inline elements.

Buttons Inside Forms
====================

Apparently one can use any kind of "button" as a submit button within a form. I believe they can be made from ``<a>``
tags, from ``<input>`` tags, or ``<button>`` tags. At this point I'm not sure how each of these would be handled by
a Django view.
