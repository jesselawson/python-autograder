def test_num_packages_ready():
	assert(num_packages_ready == 44)
		
def test_additional_packages():
	assert(additional_packages == 10)
	
def test_total_packages():
	assert(total_packages == num_packages_ready + additional_packages)

def test_total_costs():
	assert(total_costs == ((44+10)*3))

