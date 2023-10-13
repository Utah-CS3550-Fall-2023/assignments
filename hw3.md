CS 3550 Assignment 2 (CSS)
==========================

**Status**: Draft (to be finalized 16 Oct) \
**Due**: Phase 1 due **20 Oct**, Phase 2--6 due **27 Oct**

About
-----

In this assignment you'll write a backend for the frontend you
developed in [Assignmets 1](hw1.md) [and 2](hw2.md). The grading
application will then become usable: all pages will be generated from
a database, and you will be able to grade students' assignments:

- Create models in Django to describe your application's data
- Query those models to extract view-relevant data
- Use templates to generate views from data
- Modify data in response to form submissions

The assignment is due Friday, 27 Sep before midnight. The course's
normal extension policy applies. Hand in your finished assignment by
pushing it to your repository on Github.

Phase 1: Setup and header
-------------------------

Create a Django application called `grades` by running:

    python3 manage.py createapp grades

As usual, you may need to use `python` instead of `python3`, or give
the full path to your Python executable, just as you did for [Homework
1](hw1.md). See the [installation guide](install.md) for more.

This command should succeed and create a directory called `grades`
with files inside it called `models.py` and `views.py`. (It will also
contain `admin.py` and `tests.py`, which we won't be using.)

Inside the `grades` directory contain a subdirectory called
`templates`. Move all of the HTML files in `static` to this new
`templates` folder. (You can also delete `test.html`, if you still
have it.)

Open `views.py` in the `grades` directory and add the following line
to the top of the file:

    from . import models
    
Add the following lines to the bottom:

    def assignments(request):
        return render(request, "assignments.html")

Make similar definitions for the other four pages (`index`,
`submissions`, `profile`, and `login_form`). For the `index` and
`submissions` view, the function should take an additional parameter,
`assignment_id`. Make sure to use the correct function name and the
correct template name. (Note that `login` is already a Django function
that we'll need later, hence that view being called `login_form`.)

Open the `urls.py` file in the `cs3550` directory and add the
following line to the top:

    from ..grades import views

Now add these entries to the `urlpatterns` list:

```python
path("", views.assignments),
path("<int:assignment_id>", views.assignment),
path("<int:assignment_id>/submissions", views.submissions),
path("profile/", views.profile),
path("profile/login", views.login_form),
```

You should now be able to run your server, visit the following URLs,
and see the results:

- http://localhost:8000/
- http://localhost:8000/1/
- http://localhost:8000/1/submissions
- http://localhost:8000/profile
- http://localhost:8000/profile/login

Once everything works, commit everything to Github, including the new
`grades` folder and the contents of the `migrations` folder inside it.
If you have one **do not** commit your `db.sqlite3` file. (If you
accidentally do, delete it and commit again. You can add it to your
`.gitignore` file to avoid this happening in the future) You should
see the Github Action turn green. If so, Phase 1 is done. If you do
not, get help.

Phase 2: Writing a model
------------------------

Open up `models.py`. Add the following line to the top:

    from django.contrib.auth.models import User, Group

This imports the authentication system's `User` and `Group` class,
which we'll be using to represent students and TAs.

Define two classes in this file called `Assignment` and `Submission`.
Both should inherit from `models.Model` and contain `models.Field`
classes.

The `Assignment` class should have these fields:
- A short string (less than 200 characters) for the assignment `title`
- A long string for the assignment `description`
- A `deadline`, which is a date and a time
- An integer `weight` (which is how much the assignment is worth
  toward the final grade)
- An integer number of maximum `points` (which is how much this
  assignment is graded out of)
  
A `Submission` class should have these fields:
- The `assignment` it is a submission for
- The `author` who submitted the assignment
- The `grader` who is grading the assignment
- A `file` containing the submission itself
- A `score`, which is a floating-point number

As you define these fields, think carefully about:
1. Which fields have to allow blanks
2. Which fields should have defaults
3. For `ForeignKey` fields, what should happen if the related object
   is deleted

When defining the `grader` field, you will need to pass the
`related_name='graded_set'` argument to `ForeignKey`. Note that Django
will automatically also add an `id` field to each model.

When you're finished, run:

    python3 manage.py makemigration
    python3 manage.py migrate

This Phase will be autograded by running a dummy data script, which
you can find [here](...). You can run it on your own machine by saving
it to the same directory as `manage.py` and then running:

    python3 makedata.py

If you need to edit your model (because you made a mistake) you must
remember to run:

    python3 manage.py makemigration
    python3 manage.py migrate

The dummy data script creates a superuser account with a username and
password of `pavpan`. You should be able to log in to the admin
interface by running your server and then going to
[http://localhost:8000/admin](http://localhost:8000/admin). Once
there, you should be able to log in and add, edit, or delete any
assignments or submissions you like.

Phase 3: Assignments view
-------------------------

For the rest of the Phases of this assignment, you will be
implementing the grades application. We won't yet be implementing
authentication, so for now we will only implement the grader side of
the application. We'll make the five views you have right now (index,
assignments, submissions, profile, and login) generated from templates
and have those templates get their data from the database.

Create a folder named `templates` inside the `grades` application.
Move all of the HTML files in `static` to this new `templates` folder.
(You can also delete `test.html`, if you still have it.)

Open `views.py` and add the following line to the top of the file:

    from . import models

This allows your view functions (a.k.a. controllers) to use the models
you defined.

Modify the `assignments` view function to query the database for all
assignments and pass them to the `assignments.html` template.

Now open up your `assignments.html` file. It should contain a table.
Delete all the content rows (not the header row) from the table; these
rows should be generated from the list of all assignments passed in by
the view. Specifically:

- The "Assignment" column should be the assignment's `title`
- Also the assignment cell should link to `/N`, where `N` is the
  assignment ID
- The "Due date" column should be the assignment's `deadline`,
  formatted appropriately
- The "Weight" column should be the assignment's `weight`

Run your server with:

    python3 manage.py runserver --noreload

You should now be able to navigate to `http://localhost:8000/` and see
the assignments page. If it looks like the screenshot, move on to the
next phase. If it happens to contain no rows, that may be because you
didn't run the dummy data script. Fix that by running:

    python3 manage.py migrate
    python3 makedata.py

If you now see data, you can move on. If you still don't, get help.

Phase 4: Assignment view
------------------------

For the `index` view, you will need to look up the assignment based on
the assignment ID and pass that to the template.

The assignment description is supposed to contain HTML. When adding it
to the template, make sure to use the `safe` filter to allow raw HTML
to be directly added to the HTML.

For the action card, you will also need to look up:

1. How many total submissions there are to this assignment
2. How many of submissions are assigned to "you"
3. How many total students there are

For item (2), you can assume "you" is the user with a name of `ta1`.
For item (3), you can use the following code to find the total number
of students:

    models.Group.objects.get(name="Students").user_set.count()

You can pass all of this data as additional template parameters.

Make sure the word "submissions" in the action card is correctly
pluralized. That is, it should say either "1 submission assigned to
you" or "2 submissions assigned to you". Also make sure all other
plurals are correctly pluralized; for example, an example worth one
point total should not say "1 points" in the subtitle, and if only 1
submission exists the action card should not say that "1/1
submissions".

Make sure the `grade` link in the action card points to
`/N/submissions`, where `N` is the assignment ID.

Test that various assignments look normal. Only the "Homework 1"
assignment has an extensive description. Test what happens if you the
visit the URL for an invalid assignment, like
http://localhost:8000/123456789/; this should show a 404 page instead
of a crash page.

Phase 5: Submissions and Profile view
-------------------------------------

Write the `profile` view. The table should contain one row per
assignment. For each assignment, the "Graded" column should count how
many submissions are assigned to `ta1` and how many of those are
graded (which means a non-null `score` for that submission). Do not
loop over submissions one by one; instead, use the `count` query
operator.

Write the `submissions` view. Like with the `assignment`
view, you will need to look up the `Assignment` in question by its ID
and then request all `Submission`s to that assignment whose `grader`
is set to `ta1`. The template should generate the table so that:

- The "Student" column has the submission's author's name
- The "Submission" link should point to the submission's `file.url`
  field. This link won't work, however, until Homework 5.
- The input field should have a name of `grade-X` where `X` is the
  submission's ID and have a value which is the submission's `score`.
  
The rows should be sorted by `author`'s `username`. The "All grades
out of" text at the top should show the assignment's `points` field
and the "Back to assignment" link should go back to the `index` page
for the same assignment.

In each template, navigation banner is the same. Create a new file
called `header.html` containing just this navigation banner. For the
tab title use the `title` template parameter. In each template,
replace the navigation banner with an `include` of `header.html`,
passing in the correct tab title. This should make your templates much
shorter.

Test that if you add assignments, assign submissions to `ta1`, or
grade submissions via the admin interface, that your application shows
the updates correctly.

Phase 6: Grading
----------------

Open up your `submissions` template. Check that all of the `input`
elements and also the `<button>` element are inside a `form` element.
Add an `action` attribute to the form whose value is the URL
`/N/grade`, where `N` is the assignment ID. Also add a `method`
attribute with value `post`.

Define a new view function called `grade` and update `urls.py` to map
that URL to this new view function.

Inside this view function, the `request.POST` field contains the each
input field. It is basically a hash table that maps the field's `name`
to its `value`.

Iterate through the input fields. In Python, when you iterate over a
hash table, you get each **key** in the hash table. Skip any keys that
don't start with `grade-`.

For each input field, extract the submission ID from the key. You can
use Python's `split` method to split a string into substrings and
`int` to convert a string to an integer. Look up the `Submission` with
that ID. Now compute the score for that submission. To do so, use
`request.POST[key]` to get the value the TA typed into the score field
and call the `float` function on it to convert it to a floating-point
number. Set the submission's score to that. Catch the `ValueError`
exception---that's thrown if the score isn't a valid floating-point
number, and in that case you want to set the score to `None`.

Remember to `save` any model object that you change. If you'd like,
you can try using the `bulk_update` method to have fewer trips to the
database.

After updating grades use the `redirect` function to redirect back to
the correct submissions page. You can import `redirect` from
`django.shortcuts`.

Make sure all of your views handle any errors. If you are passed an
invalid assignment ID, raise an `Http404` exception, which you can
import from `django.http`. If you are passed an invalid submission ID
in `grade`, raise an `Http400` exception, which you can import from
the same place.

Write a cover sheet
-------------------

Run your server and view each page on your website in your browser.
Read through the requirements of Phases 1--5 and ensure that all
requirements are met. Visit invalid URLs and submit invalid grades.
Moreover, make sure that your website HTML still passes all the
requirements of [Assignment 1](../hw1/index.md) despite any changes
you may have made.

If you find any problems, use the browser developer tools to
understand and correct the problem.

Once you are sure everything works correctly, copy-and-paste the
following text into a new empty text file called "HW3.md":

```
Homework 3 Cover Sheet
----------------------

In this assignment, I completed:

- [ ] Phase 1
- [ ] Phase 2
- [ ] Phase 3
- [ ] Phase 4
- [ ] Phase 5
- [ ] Phase 6

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

Web applications have backends just like this one, though typically
with many more model classes, views, and actions. However, the core
ideas, including models, views, and controllers, as well as concepts
like queries and templates, are the same, even in frameworks other
than Django and languages other than Python.

One thing we did not focus on in this assignment is performance. This
grading application would probably never see enough requests that
performance would be a problem, but widely-used web applications have
to focus intensely on performance to reduce costs. Performance is a
big focus in CS 4550 Web Software Development II.

Grading Rubrik
--------------

This assignment is worth 100 points. The different phases are worth
different weights:

**Phase 1** is worth 10 points. It is graded on:

- Your web server must start up without error
- Your web server must serve all the main URLs
- Your web server must continue to serve all static files, including
  the favicon, the CSS file, and the image on the assignment page.
  
If you pass all auto-tests, then you have completed this phase.

**Phase 2** is worth 20 points. It is graded on:

- You must define all of the necessary classes and fields.
- The corrent field type should be used for each field.
- All fields must have the correct lengths, nullness, and blank
  settings, and fields with defaults should have reasonable defaults.
- Foreign key fields should have reasonable `on_delete` behaviors.

**Phase 3** is worth 10 points. It is graded on:

- The assignments view must be dynamically generated.
- Assignments for the assignments view are correctly queried from the
  database.
- Each column in the table uses the correct field.
- The due date is printed correctly.
- The assignment name links to the correct URL.

**Phase 4** is worth 15 points. It is graded on:

- The assignment view is dynamically generated.
- Assignment name, due date, and points are printed correctly.
- The total submissions and total students are printed correctly.
- Assignment description is correctly rendered (we should not see HTML
  tags on the page)
- "Grade" link goes to the correct page.

**Phase 5** is worth 20 points. It is graded on:

- The profile and submissions view is dynamically generated.
- Profile view contains one row per assignment.
- Profile view contains correct counts of assigned and graded
  submissions.
- Counts only refer to submissions assigned to `ta1`.
- Profile view uses queries, not loops, to count submissions.
- Submissions view contains one row per submission.
- All columns in the submission view are correctly generated.
- Only submissions for the current assignment are shown.
- Submissions are sorted by username.
- Other dynamically-generated parts of the Submissions page are
  correctly generated.
- Navigation banner is located only in `header.html` and never
  duplicated in templates.

**Phase 6** is worth 20 points. It is graded on:

- Form element on submissions page has correct `action` and `method`.
- `grade` view defined and accessible from a URL
- Submitting grades works
- It is possible to submit an empty grade
- Invalid grades (like the word "hello") are treated as if empty
- After successful grade submission, user is redirected back to
  submissions page
- Invalid requests receive appropriate error codes.

**Cover Sheet** is worth 5 points. It is graded on:

- Cover sheet is formatted correctly.
- All questions on the cover sheet have coherent answers.

Note that if your cover sheet does not list all people you discussed
the assignment with, or misrepresents others' work as your own, that
is academic misconduct and can result in severe sanctions beyond the 5
points the cover sheet is worth. In the most severe cases, the
sanction for academic misconduct is failing this course.
