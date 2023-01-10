from canvasapi import Canvas
from datetime import datetime, timedelta

import sys

CANVAS_TOKEN_FILE = "" # set this to a file containing your canvas API token

API_URL = "https://wwu.instructure.com/" # set to your institution's canvas url
API_KEY = open(CANVAS_TOKEN_FILE).read()
COURSE_ID = "" # set this to your course id (found in the url of the course page)
ASSIGNMENT_GRP_ID = "" # find this using canvas_recon

# get course object
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)

oneweek = timedelta(weeks=1)
unlock = datetime(2023, 1, 10, 7, 0)
due = datetime(2023, 1, 13, 22, 0)

# point values for each lab, with a dummy at index 0 so the numbers line up
points = ["_", 10, 15, 20, 30, 30, 30, 30, 30]

for lab in range(1,9):
    formats = ["py"] 

    # hackily specify submission format special cases
    if lab in [5, 8]:
        formats.append("png")

    # create new assignment
    lab_args = {
        'name': f'Lab {lab}',
        'submission_types': ['online_upload'],
        'allowed_extensions': formats,
        'notify_of_update': False,
        'points_possible': points[lab],
        'due_at': due,
        'unlock_at': unlock,
        'lock_at': None,
        'description': f'<p>Writeup: <a href="https://facultyweb.cs.wwu.edu/~wehrwes/courses/csci141_23w/lab{lab}/">https://facultyweb.cs.wwu.edu/~wehrwes/courses/csci141_23w/lab{lab}/</a></p>',
        'assignment_group_id': ASSIGNMENT_GRP_ID,
        'published': True,
        'allowed_attempts': -1
    }

    due += oneweek
    unlock += oneweek

    assgn = course.create_assignment(lab_args)



