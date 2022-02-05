def part_b(annual_salary, portion_saved, total_cost, semi_annual_raise):
	#########################################################################
	percent_down_payment = 0.2
	total_saved = 0
	r = 0.04
	months = 0
	down_payment_cost = total_cost * percent_down_payment
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while(total_saved < down_payment_cost):
	    months += 1
	    monthly_saved = annual_salary * portion_saved / 12
	    monthly_return_investement = total_saved * r / 12
	    total_saved += monthly_saved +  monthly_return_investement
	    if (months % 6 == 0):
	        annual_salary += annual_salary* semi_annual_raise
	print('Number of months: ' + str(months))
	return months