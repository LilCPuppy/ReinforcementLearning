# This file will be used to generate the initial value function for the
# algorithm, and dump the results (with corresponding values) in a csv file.

import board_utils as board_utils

def build_all_ternary_strings_of_length_nine():
	'''This function will be used to get all ternary strings of length 9.
	
	Returns:
		A list of strings.  Should be length 19,683.
	'''
	return build_all_ternary_strings_of_length_nine_helper([])

def build_all_ternary_strings_of_length_nine_helper(cur_list):
	'''See above.  Enjoy the recursion magic.

	Args:
		cur_list: The current list ;)
	Returns:
		The whole list of ternary strings.
	'''
	if len(cur_list) == 9:
		return [cur_list]

	first_branch = build_all_ternary_strings_of_length_nine_helper(
		cur_list+['0'])
	second_branch = build_all_ternary_strings_of_length_nine_helper(
		cur_list+['1'])
	third_branch = build_all_ternary_strings_of_length_nine_helper(
		cur_list+['2'])

	return first_branch + second_branch + third_branch




def main():
	all_ternary_strings = build_all_ternary_strings_of_length_nine()
	results = []
	for ternary_string in all_ternary_strings:
		value = board_utils.get_initial_board_value(
			board_utils.hash_code_to_board(''.join(ternary_string)))
		results.append((ternary_string, value))

	# Write to a file.
	with open('initial_value_states.txt', 'w') as f:
		for result in results:
			f.write('{}\n'.format(result))



if __name__ == '__main__':
	main()