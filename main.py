# Add the import statements for functions from string_utils.py and equation_utils.py here
# Download string_utils.py from your GitHub repository
!wget https://raw.githubusercontent.com/yotam-biu/ps5/main/string_utils.py -O /content/string_utils.py

# Download equation_utils.py from your GitHub repository
!wget https://raw.githubusercontent.com/yotam-biu/ps5/main/equation_utils.py -O /content/equation_utils.py

!wget https://raw.githubusercontent.com/yotam-biu/python_utils/main/lab_setup_do_not_edit.py -O /content/lab_setup_do_not_edit.py
import lab_setup_do_not_edit

from string_utils.py import parse_chemical_reaction, count_atoms_in_reaction
from equation_utils.py import build_equations, my_solve



def balance_reaction(reaction): #"Fe2O3 + H2 -> Fe + H2O"

    # 1.parse reaction
    reactants, products = parse_chemical_reaction(reaction) # [""Fe2O3", "H2"], ["Fe", "H2O""]
    reactant_atoms = count_atoms_in_reaction(reactants) # [{"Fe":2, "O":1}, {"H":2}]
    product_atoms = count_atoms_in_reaction(products)

    # 2.build equation and solve
    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    coefficients = my_solve(equations, coefficients) + [1]

    return coefficients # [1/3, 1, 2/3, 1]

