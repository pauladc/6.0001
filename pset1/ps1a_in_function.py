def part_a(annual_salary, portion_saved, total_cost):
	#########################################################################
	portion_down_payment = 0.2
	current_savings = 0
	r = 0.04
	months = 0
	down_payment_cost = total_cost * portion_down_payment
	
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while(current_savings < down_payment_cost):
	    months += 1
	    monthly_saved = annual_salary * portion_saved / 12
	    monthly_return_investement = current_savings * r / 12
	    current_savings += monthly_saved +  monthly_return_investement
	print('Number of months: ' + str(months))
	return months