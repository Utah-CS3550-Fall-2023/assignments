import datetime

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cs3550.settings")
django.setup()

from django.core.files.base import ContentFile
from grades.models import User, Group, Assignment, Submission

def midnight(month, day):
    if month < 11 or month == 11 and day < 5:
        tz = datetime.timezone(datetime.timedelta(hours=-6), "MDT")
    else:
        tz = datetime.timezone(datetime.timedelta(hours=-7), "MST")
    return datetime.datetime(2023, month, day, 11, 59, 59, 999999, tz)

def initial_data():
    tas, _ = Group.objects.get_or_create(name='Teaching Assistants')
    students, _ = Group.objects.get_or_create(name='Students')

    prof = User.objects.create_superuser("pavpan", "pavpan@cs.utah.edu", "pavpan")
    ta1 = User.objects.create_user("ta1", "ta1@cs.utah.edu", "ta1")
    ta2 = User.objects.create_user("ta2", "ta2@cs.utah.edu", "ta2")
    tas.user_set.add(ta1, ta2)

    s1 = User.objects.create_user("s1", "s1@cs.utah.edu", "s1")
    s2 = User.objects.create_user("s2", "s2@cs.utah.edu", "s2")
    s3 = User.objects.create_user("s3", "s3@cs.utah.edu", "s3")
    students.user_set.add(s1, s2, s3)

    hw0 = Assignment.objects.create(
        title="Github username",
        description="Submit a text file with your github username",
        deadline=midnight(8, 1),
        weight=1,
        points=1
    )
    hw1 = Assignment.objects.create(
        title="Homework 1 (HTML)",
        description="""
<p>In this assignment, you will set up a web server serving HTML web
pages for the grading application:</p>

<ul>
<li>Configure and start a <em>basic web server</em> using Django</li>
<li>Create <em>basic web pages</em> using HTML for data/content</li>
</ul>
        
<p>For example, here is a page <b>you will make</b>, in a file called <code>assignments.html</code>:</p>

<img class='screenshot' src='/static/assignments.png' alt='A screenshot of the assignments page' />
""",
        deadline=midnight(9, 8),
        weight=100,
        points=100
    )
    hw2 = Assignment.objects.create(
        title="Homework 2 (CSS)",
        description="Create a consistent style and layout for the grades application",
        deadline=midnight(9, 22),
        weight=100,
        points=100
    )
    hw3 = Assignment.objects.create(
        title="Homework 3 (Backend)",
        description="Implement a Django backend for the grades application",
        deadline=midnight(10, 27),
        weight=100,
        points=100
    )
    hw4 = Assignment.objects.create(
        title="Homework 4 (Deploy)",
        description="Deploy the grades application to AWS",
        deadline=midnight(11, 10),
        weight=100,
        points=100
    )
    hw5 = Assignment.objects.create(
        title="Homework 5 (Permissions)",
        description="Implement user permissions in the grades application",
        deadline=midnight(11, 24),
        weight=100,
        points=100
    )
    hw6 = Assignment.objects.create(
        title="Homework 6 (JS)",
        description="Add front-end scripts to the grades application",
        deadline=midnight(12, 8),
        weight=100,
        points=100
    )
    
    Submission.objects.create(
        assignment=hw0,
        author=s1,
        grader=ta1,
        file=ContentFile("s1", name="s1.txt"),
        score = 1.0,
    )
    Submission.objects.create(
        assignment=hw0,
        author=s2,
        grader=ta2,
        file=ContentFile("s2", name="s2.txt"),
        score = 1.0,
    )
    Submission.objects.create(
        assignment=hw0,
        author=s3,
        grader=ta1,
        file=ContentFile("s3", name="s3.txt"),
        score = None,
    )

    Submission.objects.create(
        assignment=hw1,
        author=s1,
        grader=ta1,
        file=ContentFile("HW1 for S1", name="h1s1.txt"),
        score = 93.0,
    )
    Submission.objects.create(
        assignment=hw1,
        author=s2,
        grader=ta2,
        file=ContentFile("HW1 for S2", name="h1s2.txt"),
    )
    Submission.objects.create(
        assignment=hw2,
        author=s1,
        grader=ta1,
        file=ContentFile("HW2 for S1", name="h2s1.txt"),
    )

if __name__ == "__main__":
    initial_data()

