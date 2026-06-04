#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 3
#
# Before submitting the file to gradescope make sure of the following:
# 1. The name of the file is coding3.py
# 2. Nothing below the line `if __name__="__main__":` is changed
# 3. Make sure there are no indentation errors and that the code compiles on your end
#
# YOUR NAME: Tinklyn (Jinyuan) Xiang
# YOUR UNI: jx2553

def is_onto (domain, co_domain, mapping):
    """Determines if the function is onto.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in the co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]
    """
    mapped_values = set(mapping.values())
    meets_definition = all(val in mapped_values for val in co_domain)
    return meets_definition

def is_one_to_one (domain, co_domain, mapping):
    """Determines if the function is one-to-one.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in teh co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]

    """
    mapped_values = list(mapping.values())
    meets_definition = len(mapped_values) == len(set(mapped_values))
    return meets_definition

def is_bijective ( domain , co_domain , mapping ) :
    """Determines if the function is bijective.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in teh co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]

    """
    meets_definition = is_onto(domain, co_domain, mapping) and is_one_to_one(domain, co_domain, mapping)
    return meets_definition

def is_reflexive (adj_mat) :
    """Determines if the relation is reflexive.

    Args:
        adj_mat [list[list[int]]]: an adjacency matrix of the relation, where list[i][j] is 1 if i~j
    Returns:
        meets_definition [bool]

    """
    meets_definition = all(adj_mat[i][i] == 1 for i in range(len(adj_mat)))
    return meets_definition

def is_symmetric (adj_mat) :
    """Determines if the relation is transitive.

    Args:
        adj_mat [list[list[int]]]: an adjacency matrix of the relation, where list[i][j] is 1 if i~j
    Returns:
        meets_definition [bool]

    """
    n = len(adj_mat)
    meets_definition = all(adj_mat[i][j] == adj_mat[j][i] for i in range(n) for j in range(n))
    return meets_definition

def is_transitive (adj_mat) :
    """Determines if the relation is transitive.

    Args:
        adj_mat [list[list[int]]]: an adjacency matrix of the relation, where list[i][j] is 1 if i~j
    Returns:
        meets_definition [bool]

    """
    n = len(adj_mat)
    for i in range(n):
        for j in range(n):
            if adj_mat[i][j] == 1:
                for k in range(n):
                    if adj_mat[j][k] == 1 and adj_mat[i][k] != 1:
                        return False
    meets_definition = True
    return meets_definition

def is_antisymmetric (adj_mat) :
    """Determines if the relation is antisymmetric.

    Args:
        adj_mat [list[list[int]]]: an adjacency matrix of the relation, where list[i][j] is 1 if i~j
    Returns:
        meets_definition [bool]

    """
    n = len(adj_mat)
    meets_definition = all(
        not (adj_mat[i][j] == 1 and adj_mat[j][i] == 1)
        for i in range(n) for j in range(n) if i != j
    )
    return meets_definition

def is_irreflexive (adj_mat) :
    """Determines if the relation is irreflexive.

    Args:
        adj_mat [list[list[int]]]: an adjacency matrix of the relation, where list[i][j] is 1 if i~j
    Returns:
        meets_definition [bool]

    """
    meets_definition = all(adj_mat[i][i] == 0 for i in range(len(adj_mat)))
    return meets_definition

######################################################################
### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
######################################################################
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 3: Functions!")
    print("#######################################")
    print()
    print("---------------------------------------")
    print("PART A: Function Properties")
    print("---------------------------------------")

    example_1 = [[1 ,2 ,3 ,4],[1,2,3,4,5,6,7],{1:2, 2:3, 3:1,4:3}] #not anything
    example_2 = [[1 ,2 ,3 ,4],[1,2,3,4,5,6,7],{1:2, 2:3, 3:1,4:5}] #one to one (nothing else)
    example_3 = [[1 ,2 ,3 ,4],[1,2,3],{1:2, 2:3, 3:1,4:3}] #onto (nothing else)
    example_4 = [[1 ,2 ,3 ,4],[1,2,3,4],{1:2, 2:3, 3:1,4:4}] #bijective
    
    print("---------------------------------------")
    print("\'is_onto\' Tests")
    print("---------------------------------------")
    is_onto_tests = [example_1, example_2, example_3, example_4]
    is_onto_answers = [False, False, True, True]
  
    for count, test in enumerate(is_onto_tests):
        if (is_onto(is_onto_tests[count][0],is_onto_tests[count][1],
                    is_onto_tests[count][2]) == is_onto_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_onto_answers[count]}')
        print(f'Your Answer: {is_onto(is_onto_tests[count][0],is_onto_tests[count][1],is_onto_tests[count][2])}')
        
    print("---------------------------------------")
    print("\'is_one_to_one\' Tests")
    print("---------------------------------------")
    is_one_to_one_tests = [example_1, example_2, example_3, example_4]
    is_one_to_one_answers = [False, True, False, True]
  
    for count, test in enumerate(is_one_to_one_tests):
        if (is_one_to_one(is_one_to_one_tests[count][0],is_one_to_one_tests[count][1],
                    is_one_to_one_tests[count][2]) == is_one_to_one_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_one_to_one_answers[count]}')
        print(f'Your Answer: {is_one_to_one(is_one_to_one_tests[count][0],is_one_to_one_tests[count][1],is_one_to_one_tests[count][2])}')
    
    print("---------------------------------------")
    print("\'is_bijective\' Tests")
    print("---------------------------------------")
    is_bijective_tests = [example_1, example_2, example_3, example_4]
    is_bijective_answers = [False, False, False, True]
  
    for count, test in enumerate(is_onto_tests):
        if (is_bijective(is_bijective_tests[count][0],is_bijective_tests[count][1],
                    is_bijective_tests[count][2]) == is_bijective_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_bijective_answers[count]}')
        print(f'Your Answer: {is_bijective(is_bijective_tests[count][0],is_bijective_tests[count][1],is_bijective_tests[count][2])}')
        
    print()
    print("---------------------------------------")
    print("PART B: Relation Properties")
    print("---------------------------------------")

    example_1 = [[1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1]]
    
    example_2 = [[0, 1, 1, 0, 1],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 1],
                [0, 1, 1, 1, 1],
                [1, 1, 1, 1, 0]]
    
    example_3 = [[0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],]

    example_4 = [[0, 0, 0, 0, 1],
                [0, 1, 1, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 1, 0, 1, 1],
                [1, 1, 1, 0, 1],]
    
    print("---------------------------------------")
    print("\'is_reflexive\' Tests")
    print("---------------------------------------")

    relation_tests = [example_1, example_2, example_3, example_4]
    is_reflexive_answers = [True, False, False, False]
  
    for count, test in enumerate(relation_tests):
        your_answer = is_reflexive(test)
        if (your_answer == is_reflexive_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_reflexive_answers[count]}')
        print(f'Your Answer: {your_answer}')
        
        
    print("---------------------------------------")
    print("\'is_symmetric\' Tests")
    print("---------------------------------------")
    is_symmetric_answers = [True, True, False, False]
  
    for count, test in enumerate(relation_tests):
        your_answer = is_symmetric(test)
        if (your_answer == is_symmetric_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_symmetric_answers[count]}')
        print(f'Your Answer: {your_answer}')
        
        
    print("---------------------------------------")
    print("\'is_transitive\' Tests")
    print("---------------------------------------")
    is_transitive_answers = [True, False, True, False]
  
    for count, test in enumerate(relation_tests):
        your_answer = is_transitive(test)
        if (your_answer == is_transitive_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_transitive_answers[count]}')
        print(f'Your Answer: {your_answer}')
