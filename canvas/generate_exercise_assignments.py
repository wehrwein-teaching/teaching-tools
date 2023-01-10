# beware - this is both extra messy and very special-purpose


from canvasapi import Canvas
from datetime import datetime, timedelta

import sys

CANVAS_TOKEN_FILE = "" # set this to a file containing your canvas API token

API_URL = "https://wwu.instructure.com/" # set to your institution's canvas url
API_KEY = open(CANVAS_TOKEN_FILE).read()
COURSE_ID = "" # set this to your course id (found in the url of the course page)

# find these using canvas_recon:
ASSIGNMENT_GRP_ID = ""
GROUPSET_ID = ""


def make_assignments(course, lecture_number, month, day):

    # set up deadlines w/ offsets
    onehour = timedelta(hours=1)
    fivemins = timedelta(minutes=5)
    due_at_noon = datetime(2023, month, day, 12, 0)
    lock_at_noon = due_at_noon + fivemins

    # create new assignment
    EI_args = {
        'name': f'E{lecture_number}I',
        'submission_types': ['online_upload'],
        'allowed_extensions': ['pdf'],
        'notify_of_update': False,
        'points_possible': 5,
        'due_at': due_at_noon,
        'lock_at': lock_at_noon,
        'description': '<p>Upload your solutions to the <strong>Exercises</strong> by the start of class in PDF format. Clearly legible scans of handwritten answers are fine.</p>',
        'assignment_group_id': ASSIGNMENT_GRP_ID,
        'published': True,
        'allowed_attempts': -1
    }

    EI = course.create_assignment(EI_args)

    # add overrides to set different deadlines for 10am sections
    #for section_id in sections_10am:
    #    ei.create_override(**{
    #        'assignment_override[course_section_id]': section_id,
    #        'assignment_override[due_at]': due_at_10am,
    #        'assignment_override[lock_at]': lock_at_10am
    #    })

    ET_args = {
        'name': f'E{lecture_number}T',
        'submission_types': ['on_paper'],
        'notify_of_update': False,
        'group_category_id': GROUPSET_ID,
        'points_possible': 5,
        'due_at': due_at_noon + onehour,
        'description': '<p>This is the correctness portion of the in-class exercise grade, scored on a per-team basis.</p>',
        'assignment_group_id': ASSIGNMENT_GRP_ID,
        'published': True,
        'allowed_attempts': -1
    }

    ET = course.create_assignment(ET_args)

# get course object
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)

if len(sys.argv) == 4:
    lecture_number = sys.argv[1]
    month = int(sys.argv[2])
    day = int(sys.argv[3])


    make_assignments(course, lecture_number, month, day)
else:
    print("danger - do you really want to do this?")
    sys.exit(0)
    dates = [
        (3, 1, 18),
        (4, 1, 20),
        (5, 1, 23),
        (6, 1, 25),
        (7, 1, 27),
        (8, 1, 30),
        (9, 2, 1),
        (10, 2, 6),
        (11, 2, 8),
        (12, 2, 13),
        (13, 2, 15),
        (14, 2, 17),
        (15, 2, 22),
        (16, 2, 27),
        (17, 3, 1),
        (18, 3, 3),
        (19, 3, 5)
    ]
    for num, mo, da in dates:
        print(f"{num}, {mo}/{da}")
        make_assignments(course, num, mo, da)



