from flask import Flask, request
from flask import render_template
from models import *

app = Flask(__name__)

@app.route('/')
def index():
	loans_count = Loan.select().count()
	# schools_count = School.select().count()
	# school = School.get(somethingsomething)
	gradelist = Loan.select(Loan.grade).distinct().order_by(Loan.grade.asc())
	return render_template('index.html', count=loans_count, gradelist = gradelist)

@app.route('/grades', methods=['POST'])
def grades():
	grade = request.form.get("grade")
	checkins = Loan.select().where(Loan.grade == grade).limit(20)
	#checkins = Checkin.select().where(Checkin.neighborhood == neighborhood)
	return render_template('table.html', checkins = checkins, grade = grade)

@app.route('/checkins/<neighborhood>.csv')
def neighboorhoodcsv(neighborhood):
	checkins = Checkin.select().where(Checkin.neighborhood == neighborhood)
	return render_template('template.csv', checkins = checkins)

# # Mark a parameter in the url by putting < > around it
# # and then it will come into the function! like magic
# # /schools/school-of-food-and-finance - slug
# # /schools/01M292-school-of-food-and-finance
# @app.route('/schools/<dbn>')
# def show(dbn):
# 	# Aggregate functions
# 	# SELECT MEDIAN(total_students) FROM schools
# 	# SELECT MAX(total_students) FROM schools
# 	# SELECT AVG(total_students) FROM schools
# 	school = School.get(School.dbn == dbn)
# 	avg = School.select().aggregate(
# 		fn.Avg(School.total_students)
# 	)

# 	# Just go grab the score by the dbn
# 	try:
# 		score = Score.get(Score.dbn == dbn)
# 	except:
# 		score = None

# 	# Get the number of schools with <= students,
# 	# then divide it by the total number of students
# 	num_smaller_schools = School.select().where(
# 		School.total_students <= school.total_students
# 	).count()
# 	student_count_percentile = 100 * num_smaller_schools / School.select().count()

# 	return render_template('show.html', school=school, avg=avg, student_count_percentile=student_count_percentile, score=score)

if __name__ == '__main__':
    app.run(debug=True)