CS 3550 Assignment 6 (JavaScript)
=================================

**Status**: Final \
**Due**: Phase 1 due **1 Dec**, Phase 2--5 due **8 Dec**

About
-----

In this assignment you'll use frontend scripting with JavaScript to
add a variety of convenient user interactions to the grades
application. Specifically, you will:

- Make tables sortable and filterable
- Use `fetch` to submit forms asynchronously
- Build a front-end UI for estimating future grades

The assignment is due Friday, 8 Dec before midnight. The course's
normal extension policy applies. Please note that the final is on 11
December. I therefore **strongly encourage** finishing the assigment
early.

Phase 1: Adding JavaScript
--------------------------

Create a file named `main.js` in your static directory. Add the
following contents to it:

    export function say_hi() {
        console.log("Hello");
    }

This defines a function named `say_hi` which writes to the browser
debugging console when it's run.

Note the `export` keyword. That's because this is a "JavaScript
module". We'll be using JavaScript modules in this class for our
JavaScript code. Modules (often called "ES6 modules" after the version
of JavaScript where they were introduced) are a relatively new feature
and you'll see a lot of older JavaScript tutorials not use them.

Now edit your `header.html` template (which should be included from
all other templates) and add the following lines to it:

    <script type=module>
      import { say_hi } from "/static/main.js";
      say_hi()
    </script>

A few features of this code deserve explanation. We use `type=module`
to indicate that we are using modules. That is what allows us to use
the `import` statement. All of our scripts will be modules.

Run your server and visit a page. (Since you edited `header.html`, any
page should do.) Open the browser developer console. You should see
the text "Hello" appear. If it does, commit all of your changes and
confirm that more of the autotester is now passing. If it does not,
get help.

Next, we will download the jQuery library that we will be using. In
the root of your repository, execute the following command:

    git submodule add https://github.com/jquery/jquery static/jquery
    
> [!CAUTION]
> An earlier version of these instructions instead asked you to
> download the `3.x-stable` branch of jQuery, which doesn't work as it
> does not support modules. If you did so, execute the following
> command from the same folder:
>
>     git -C static/jquery checkout main
>
> This should switch your jQuery download to the latest `main` branch.
> You will be asked to (and should) commit the `.gitmodules` file.

This will download the latest version of jQuery, to a folder named
`jquery` inside your static folder. It should take about a minute to
run. If you see any lines beginning with `fatal` or `error`, something
has gone wrong. Get help immediately. If you do not, commit and push
your changes to Github; the changes should be to a new file called
`.gitmodules` and to the `static/jquery` directory. You should now see
more of the autotester passing. If it does not, get help.

Add the following line to the top of `main.js`:

    import { $ } from "/static/jquery/src/jquery.js";
    
This imports the `$` function from the jQuery library. In jQuery the
`$` function is used to wrap HTML nodes with jQuery features.

In `header.html` delete the existing `<script>` block and replace it
with the following:

    <script type="module" src="/static/main.js"></script>

The `src` attribute is more or less shorthand for `import`ing the
named file.

Then replace the `say_hi` definition with this:

    export function say_hi(elt) {
        console.log("Say hi to", elt);
    }

and add this to the end of the file:

    say_hi($("h1"));
    
You should now see it print the words "Say hi to" followed by a
JavaScript object definition. This object definition is how
jQuery-wrapped elements print. You can usually expand the `0` field to
see the underlying element being wrapped. If it does not, get help.

Commit all changes and push to Github. You should now pass the
autotester. If you do, you are done with Phase 1.

Phase 2: Sorting and filtering
------------------------------

The `assignments` and `profile` views both contain a table. The
right-most column of the table is a column of numbers. We want to add
the ability to click on that column to sort by it; clicking once
should sort it in ascending order (later rows are bigger), and
clicking again should sort it in descending order (later rows are
smaller).

Define a function called `make_table_sortable`. It should take one
argument (a `<table>` element wrapped with jQuery) and modify it to
make it sortable. The rest of this phase explains how to do so.

First, the `make_table_sortable` function should select the last
header cell in the table header. You will need to add a `click`
handler to this header cell. Use the [jQuery `on` method][jq-click] to
do so. You are expected to read the documentation to learn how to use
this method on your own, though of course you should feel free to ask
for help or with questions on Discord or in office hours.

The table can be in one of three states: unsorted, sorted ascending,
or sorted descending. We'll save the table's current state by making
this last table header cell have the class `sort-asc`, `sort-desc`, or
neither.

When the table cell is clicked (that is, inside the click handler),
use jQuery's [class attribute methods][jq-class] to determine what
state the table is in. If it's unsorted or sorted descending, make it
instead sorted ascending. If it's sorted ascending, make it sorted
descending.

Test your code by running the server, clicking on the table header,
and confirming that the classes are changed correctly. Make sure you
don't end up in a situation where both the `sort-asc` and `sort-desc`
classes are set.

[jq-click]: https://api.jquery.com/click/
[jq-class]: https://api.jquery.com/category/manipulation/class-attribute/

Next, in the click handler, you will want to sort the table rows. It's
important *not* to also sort the table header row or the table footer
row (on the profile page for students). So you should make sure (using
the browser developer tools) that only data rows are inside the
`<tbody>` element. The table header should be inside `<thead>` and the
table footer should be inside `<tfoot>`.

Once you've confirmed that, select all rows inside `<tbody>` using the
[`find` function][jq-find]. The `find` function (like all jQuery
selectors) returns a jQuery object, but you will want a regular array
that you can sort. You can use the [`toArray` function][jq-toarray] to
convert a jQuery object into a list of HTML elements. (Note: the
elements in this list are not wrapped with jQuery. If you want to call
jQuery methods on them, you will need to re-wrap them.) Then call the
[JavaScript `sort` method][js-sort] on this array; you will need to
pass a comparison function and are expected to read the documentation
to understand how to do so. Once you have a sorted array you wrap it
back into a jQuery object and then use the [`appendTo` method][jq-at]
to append those rows back to the `<tbody>` element. This method moves
elements from their old position to the end of some new element.

[jq-find]: https://api.jquery.com/find/
[jq-toarray]: https://api.jquery.com/toArray/
[js-sort]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
[jq-at]: https://api.jquery.com/appendTo/

Sort the table rows by the numeric value of the text contents of the
last `<td>` inside each `<tr>`, and make sure to sort ascending or
descending correctly. Make sure that you:

- Use the last `<td>` in each row, not any of the other `<td>`
  elements or any non-`<td>` elements.
- Get the text contents of the `<td>`, which should be a string like
  "100"
- Convert the text contents into a number. For example, it's
  important that "100" is considered to be bigger than "2", even
  though the string "2" is lexicographically later than the string
  "100".
- If the string has a percentage sign (it should, on a student's
  profile) or a fraction sign (it should, on a TA's profile), you
  convert it to a number by taking everything up to the non-whitespace
  character. If the string has no text, where it goes does not matter.
  The [JavaScript `Math.parseFloat` function][js-mpf] will do this
  correctly by default.
- Sorting descending is not the same thing as sorting ascending, then
  reversing. Instead, you need to reverse the sign of the comparison
  function. (The difference happens when two rows have the same score.)
  
[js-mpf]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat

Once you have written `make_table_sortable`, add a `script` tag to the
assignments and profile pages to make the main table sortable. Make
sure to give the script `type=module`.


Phase 3: Improving table sorting
--------------------------------

This initial sorting code works but has some flaws. Among them:

- There's no way to restore the original sort order
- There's no way to sort by another column, like the assignment due
  date
- There's no indication to the user what the current state is

Let's fix them. First, let's make it possible to restore the original
sort order. To do so, modify your template to add an attributed called
`data-index` to each `<tr>` element. This index should count up from 1
for each row of the table. You can use the [Django `forloop.counter`
variable][dj-for-counter] to output a different number for each
iteration of a `{% for %}` block in a template.

[dj-for-counter]: https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#for

Next, modify the sort code so that clicking on a table header that is
sorted descending changes it to an unsorted state. In the unsorted
state, the table rows should be sorted based on this `data-index`
attribute. In jQuery, you can use [the `.data("index")`
method][jq-data] to read the `data-index` attribute of an element.
Test that it is now possible to restore the original sort order. That
is, run the server, visit a page, and click on the table header three
times. After the first click, it should sort ascending; after the
second click, it should sort descending; and after the third click, it
should restore the original order.

[jq-data]: https://api.jquery.com/data/

Second, on the `assignments` page, let's add the ability to sort by
the assignment due date. Modify the `assignments` template to add a
`data-value` attribute to each `<td>` containing the due date. The
value of the attribute should be the timestamp for the due date; you
use [the `|date:"U"` Django filter][dj-date] to print a date as a
timestamp. Timestamps are just numbers and can be compared for
equality. Add the `sortable` class to all sortable `<th>` elements,
which should be the final column on the profile page and then the
final two columns on the assignments page.

[dj-date]: https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#date

Modify the `make_table_sortable` function to make the due date table
header cell sortable, if it's a table with a due date column. Clicking
on that table header should:

- Cycle the class on that table header from no class to `sort-asc` to
  `sort-desc`, just like the last column
- Clear the classes on all other columns (so only one column is sorted
  at a time)
- Sort the relevant column in the relevant way.

A few hints that might make this easier. First, you can add a
`data-value` attribute to the last column too. If you do this, you can
use the same sorting code for all columns. Second, your code can
assign a click event handler to all `sortable` table headers instad of
special-casing the due-date and score columns. Finally, when a table
header column is clicked, you can figure out what number column it is
using [the `index` method][jq-index]. You can then use [the `get`
method][jq-get] to get the table cell with the same index in a table
row.

[jq-index]: https://api.jquery.com/index/#index
[jq-get]: https://api.jquery.com/get/#get-index

Test that you can now sort the due date field. Test that sorting works
both ascending and descending. Also test that it's possible to sort
first by one column and then by another. Test that if you go back to
an unsorted state, the original sort order is restored.

Third, to give the user an indication of whether the text is sorted or
not, add the following code to your CSS:

    th.sortable { cursor: pointer; }
    th.sort-asc::after { content: " \25b2;" }
    th.sort-desc::after { content: " \25bc;" }
    
The first line of CSS shows the "hand" cursor when hovering over
sortable table headers, while the next two lines apply to all `<th>`
elements that have the `sort-asc` or `sort-desc` classes, and add an
up or down arrow to the table header contents. Test that there is now
an arrow on table cells and that the arrow changes direction as you
sort.

Phase 4: Asynchronous file upload
---------------------------------

When a student is logged in and on the assignment page for an
assignment that isn't due yet, they should see a submission form.
Right now, submitting that form requires loading a new page, which can
be distracting. Let's instead make that form submit synchronously.

Define a `make_form_async` function in `main.js`. This function should
take in a jQuery-wrapped `<form>` element and make it submit itself
asynchronously. In the `assignment` view, add a `<script>` tag to
invoke the `make_form_async` function on the submission form element.
Keep in mind that some assignment pages don't have submission forms,
like the TA view or when an assignment is past due.

Inside `make_form_async`, add [`submit` hander][jq-submit]. This
handler should call [the `preventDefault` method][jq-pd] to prevent
the form from being submitted normally. It should then set [the
`disabled` attribute][mdn-disabled] on the file input and button in
the form, so that the file cannot be changed and the form cannot be
submitted again.

[jq-pd]: https://api.jquery.com/event.preventDefault/
[jq-submit]: https://api.jquery.com/submit/#on-%22submit%22-eventData-handler
[mdn-disabled]: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/disabled

Inside the handler, construct a [`FormData` object][js-formdata] for
the form. Then use [the `ajax` method][jq-ajax] to submit a `POST`
request to your `submit` view containing that formdata. Specifically,
in the `settings` argument of `ajax`, pass:

- The URL of the `submit` view as `url`
- The `FormData` object as `data`
- `POST` as the type

[js-formdata]: https://developer.mozilla.org/en-US/docs/Web/API/FormData/FormData
[jq-ajax]: https://api.jquery.com/jQuery.ajax/

You also need to pass these fields in the `settings` argument,
otherwise it won't work:

- `false` as `processData`
- The form's `enctype` field as its `contentType`
- The form's `enctype` field as its `mimeType`

Finally, pass `success` and `error` functions. The `error` function
can just log an error message with `console.log`. The `success`
function should replace the `<form>` element with some text like
"Upload succeeded". You don't need to worry too much about what
exactly this looks like; it is OK if it looks like of ugly. It is only
important that there is some visual indication that the upload
succeeded.

(Of course, a proper implementation would, for example, update the
page to link to the uploaded document, so that it would look identical
to refreshing the page. However, in this assignment we're not testing
that.)

Phase 5: Hypothesizing grades
-----------------------------

When a student visits their profile page, they see their grades on all
graded assignments, but `Not Due` or `Ungraded` for ungraded
assignments. Moreover, these ungraded assignments don't participate in
the computation of their current grade. But sometimes students want to
estimate what their grade would be if they got an expected grade on an
assignment, or figure out what grade they need on the final to achieve
a specific final grade.

To make this possible, we want to add a hypothesized grade interaction
to students' profile pages. Specifically, we want to add a
"Hypothesize" button to the bottom of student profile pages. When
clicked, it should replace all `Not Due` or `Ungraded` grades with a
number input field. As percentages are typed into those input fields,
the final grade should be recalculated as if the student got that
grade on that assignment. Implement this interaction.

Start by adding a `make_grade_hypothesized` function to `main.js`.
Just like `make_table_sortable` or `make_form_async`, it should take a
jQuery-wrapped `<table>` element as an argument and add the
"Hypothesize" button and all its behavior.

First, thing the `make_grade_hypothesized` function should create a
`<button>` element and add it to the document before the `<table>`.
You can use [the `$` function][jq-core-html] to create new elements
and [the `before` method][jq-before] to add them to the document.

[jq-before]: https://api.jquery.com/before/
[jq-core-html]: https://api.jquery.com/jQuery/#jQuery2

Second, add a click handler to that button. Clicking that button
should add a `hypothesized` class to the `<table>` and change the
button text to "Actual grades". Or, if the `hypothesized` class is
already present, remove it and change the button text back to
"Hypothesize". This pattern of storing the document state in classes
is very common.

Third, when changing to the `hypothesized` state, replace the contents
of all "Not Due" or "Ungraded" `<td>` elements with a new number
input. The `<input>` element should not have a `value` attribute
initially. Store the original text contents using the `data` method.
When changing back to the non-`hypothesized` state, remove all the
number inputs and restore the original text.

Fourth, write a JavaScript function that computes the current grade.
You will want to add `data-weight` attribute to each `<td>` so that
your code knows the weight of each assignment. Then use the same rules
as [Assignment 5](hw5.md) to compute the grade. Make sure to treat
"Missing" assignments as 0 points. In non-`hypothesized` state, all
"Not Due" or "Ungraded" assignments should be ignored, but in a
`hypothesized` state, use the current value of each input element,
interpreted as a percentage, to compute the current grade. If the
input element has no value, ignore that assignment (as if it were
ungraded). When the current grade is computed, replace the "final
grade" cell in the footer with the final grade, formatted as a
percentage.

Fifth, call this grade-computation function every time you switch
between states and also any time [the `change` event][jq-change]
is fired on one of the new input elements. It should now be possible
to hypothesize a grade for a particular assignment, click somewhere
else on the page (so the input element is no longer focused) and see
the final grade update.

[jq-change]: https://api.jquery.com/change/

Test your work. You should be able to:

- Clicking "Hypothesize" should make input boxes appear.
- The input boxes should appear for all "Ungraded" or "Not Due"
  assignments, but graded or "Missing" assignments should be
  unchanged.
- Clicking "Hypothesize" should not change the final grade; your
  JavaScript grade computation should agree with the one done by
  Django.
- Clicking "Actual grades" should make input boxes disappear. The
  original text, "Ungraded" or "Not Due", should reappear.
- Typing into an input box and then clicking elsewhere should cause
  the final grade to update.
  
Double-check that you compute final grades correctly. In particular,
make sure you intepret what the user types in as a percentage, not as
a point value or as a fraction of the weight.

Write a cover sheet
-------------------

Run your server and view each page on your website in your browser.
Read through the requirements of Phases 1--5 and ensure that all
requirements are met. Test logging in as students, TAs, and the
professor and using various portions of the site.

Once you are sure everything works correctly, copy-and-paste the
following text into a new empty text file called "HW6.md":

```
Homework 6 Cover Sheet
----------------------

In this assignment, I completed:

- [ ] Phase 1
- [ ] Phase 2
- [ ] Phase 3
- [ ] Phase 4
- [ ] Phase 5

I discussed this assignment with:

- ...
- ...
- ...

[ ] I solemly swear that I wrote every line of code submitted as part
of this assignment (except that auto-generated by Django).

The most interesting thing I learned in this assignment was ...

The hardest thing in this assignment was ...
```

In the first list, replace `[ ]` with `[x]` for each phase of the
assignment you completed.

In the second list, replace the `...`s with the name of your partner
as well as any other person (student, friend, family, online stranger)
that you discussed this assignment with.

In the oath below that, check the box. Recall that, while you may
discuss the assignment in broad strokes, you must write every line of
code submitted by you, as stated in the oath below this list. This
includes the use of AI tools such as ChatGPT.

In the last two paragraphs, replace the `...` with the most
interesting and the most difficult aspect of this assignment. Don't
just make them a single sentence; the instructors use your answers to
make these assignments more interesting and easier.

Once you are done, commit everything and push it to Github. **Make
sure to include the text "Please grade" in your final commit message**
to help TAs identify the right commit to grade.

How you will use this
---------------------

This is a fairly rudimentary set of front-end interactions, with a lot
of sharp edges, like minimal error checking on the form upload and not
enough indication to the user what table columns are sortable.
Nonetheless, you've probably seen these interactions many times, and
they are important for making websites easier to use.

Basic interactions like table sorting are often provided by libraries;
for example the [Sortable library][sortable] provides a sortable
table. But interactions like the hypothesized grades are custom to our
specific application, so it's important to be able to write them
yourself.

[sortable]: https://github.hubspot.com/sortable/docs/welcome/

Grading Rubrik
--------------

This assignment is worth 100 points. The different phases are worth
different weights:

**Phase 1** is worth 5 points. It is graded on:

- You link to a `main.js` file
- The `main.js` file is loaded and runs without error
- You use the `type=module` parameter
- You import the `jquery` library.

**Phase 2** is worth 20 points. It is graded on:

- You can click on the final table header to sort the table by that
  column.
- Table rows are sorted correctly
- You can toggle between sorting ascending and descending.
- Sorting percentages or fractions works correctly.
- Table headers and footer stay put when sorting.

**Phase 3** is worth 30 points. It is graded on:

- The original sort order can be restored
- The assignment due date is sortable
- Arrows indicate the sort direction

**Phase 4** is worth 20 points. It is graded on:

- Submitting a file disables the file input and form
- Submitting a file causes the browser to make a `POST` request to the
  `submit` endpoint
- The `POST` request is correctly formatted, with the right `enctype`
- When submission is successful, the form is removed and replaced with
  some success message.
- When submission fails, the browser console should show some error
  message.

**Phase 5** is worth 20 points. It is graded on:

- Clicking the "hypothesize" button shows input boxes
- Clicking it again restores the original text and correct final score
- Typing into input boxes (and clicking elsewhere) updates the final
  score
- Empty input boxes are ignored during final score computation
- The final score is correctly computed

**Cover Sheet** is worth 5 points. It is graded on:

- Cover sheet is formatted correctly.
- All questions on the cover sheet have coherent answers.

Note that if your cover sheet does not list all people you discussed
the assignment with, or misrepresents others' work as your own, that
is academic misconduct and can result in severe sanctions beyond the 5
points the cover sheet is worth. In the most severe cases, the
sanction for academic misconduct is failing this course.
