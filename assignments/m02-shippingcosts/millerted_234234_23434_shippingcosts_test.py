def test_num_packages_ready():
	assert(get_num_packages_ready() == 44)
		
def test_additional_packages():
	assert(get_additional_packages() == 10)
	
def test_total_packages():
	assert(get_total_packages() == get_num_packages() + get_additional_packages())

def test_total_costs():
	assert(get_total_costs() == ((44+10)*3))

