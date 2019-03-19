import sqlite3

DB_FILE = 'payroll_dc_small.db'
conn = sqlite3.connect(DB_FILE)


def main():
	print('a6 - standard report 1')
	strsql = """select
					substr(EDLVLT, 4) ed_level,
					max(salary) max_salary,
					min(salary) min_salary,
					round(avg(salary), 2) avg_salary,
					count(salary) employee_count
				from factdata_mar2016, edlvl
				where factdata_mar2016.EDLVL =edlvl.EDLVL
				group by ed_level
				order by avg_salary desc
				limit 15;
		"""
	cursor = conn.execute(strsql)
	# the formating string for each row of the report
	report_string_format = '{0:<40}\t{1:<12}{2:<12}{3:<12}{4:<12}'
	# printing the header of the report. 
	print(
		report_string_format.format(
			'Education Level', 'Max Salary', 'Min Salary', 'Avg Salary', 'Employee Count'
			)
		)

	for row in cursor:  
		ed_level, max_salary, min_salary, avg_salary, employee_count = row
		print(
			report_string_format.format(
				ed_level, max_salary, min_salary, avg_salary, employee_count
				)
			)

	cursor.close()		# close cursor
	conn.close()		# close connection to the db

if __name__ == "__main__":
	main()
