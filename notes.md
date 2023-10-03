Various Notes
=============

This document lists helpful checklists and notes. You won't ever be
quizzed on it, but it might be helpful to know and practice it because
it gives you a systematic way to get various things done.

Flex-box
--------

I recommend doing all flex-box layouts in the following order. Before
beginning, I find it helpful to draw a diagram where I can draw in
containers and mark their sizes and where the whitespace should go.

**Step 1: Rows and columns.** Figure out which elements are flex
containers, and whether they are rows or columns. In the process, you
might need to add new elements (usually `<div>`, but in rare cases
there might be some semantically-appropriate other element) to be new
flex containers. Assign `display: flex` and the appropriate
`flex-direction` to each container.

Now, go through the containers *starting from the root container*. For
each one, do the following steps.

**Step 2: main direction lengths.** Next, figure out how long, in the
main direction each item should be. This means width for items in row
containers and height for items column containers.

First, assign the appropriate `width`/`height` property to handle the
"default" or "preferred" size. (The formal name is "basis".) Then ask
yourself whether its size is flexible and should change with the size
of the container. If yes, also assign an appropriate `flex-grow` and
`flex-shrink` value.

**Step 3: main direction whitespace.** Now figure out how big the
whitespace between items in the main direction should be.

First, assign the appropriate `gap` between items. This is the
"default" or "preferred" gap. Then ask yourself whether the gaps
should be flexible and change size with the container. If yes, also
assign an appropriate `justify-content` value.

**Step 4: other direction.** Now figure out how big each item should
be in the other direction (so, height inside row containers and width
inside column containers).

If it should stretch across the whole container, do nothing.
Otherwise, first set `align-items` to determine where the whitespace
goes and then `height`/`width` to set the size if not fit to content.
