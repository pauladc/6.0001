def part_c(initial_deposit):
	#########################################################################
	down_payment_cost = 800000 * 0.2
	current_savings = 0
	high = 1
	low = 0
	steps = 0
	r = (high + low)/2
	while (abs(current_savings - down_payment_cost) > 100):
	    if (initial_deposit >= (down_payment_cost - 100)):
	        r = 0.0
	        break
	    if (steps >= 36):
	        r = None
	        break
	    current_savings = initial_deposit * (1 + r/12)**36
	    if(current_savings > down_payment_cost):
	        high = r
	    if(current_savings < down_payment_cost):
	        low = r
	    r = (high + low)/2
	    steps += 1
	
	
	
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	print('Best savings rate: ' + str(r))
	print('Steps in bisection search: ' + str(steps))
	return r, steps