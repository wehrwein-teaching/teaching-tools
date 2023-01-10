from canvasapi import Canvas

CANVAS_TOKEN_FILE = "" # set this to a file containing your canvas API token

API_URL = "https://wwu.instructure.com/" # set to your institution's canvas url
API_KEY = open(CANVAS_TOKEN_FILE).read()
COURSE_ID = "" # set this to your course id (found in the url of the course page)

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)

print("get_assignment_groups")
for g in course.get_assignment_groups():
    print('     ', g)

print("get_group_categories")
for g in course.get_group_categories():
    print('    ', g)
