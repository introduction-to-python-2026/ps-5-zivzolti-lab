import string_utils as su
import equation_utils as eu



def balance_reaction(reaction): #"Fe2O3 + H2 -> Fe + H2O"

    reactants, products = parse_chemical_reaction(reaction) 
    reactant_atoms = count_atoms_in_reaction(reactants) 
    product_atoms = count_atoms_in_reaction(products)

    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    coefficients = my_solve(equations, coefficients) + [1]

    return coefficients # [1/3, 1, 2/3, 1]

