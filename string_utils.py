def split_before_uppercases(formula):
    start = 0
    end = 0
    split_formula = []
    if not formula:
      return split_formula
    else:
      for char in formula[1:]:
        if char.isupper():
          split_formula.append(formula[start:(end+1)])
          start = end + 1 
        end += 1
      split_formula.append(formula[start:(end+1)])
      return split_formula

def split_at_digit(formula):
    digit_location = 1
    for char in formula[1:]:
      if (char.isdigit()):
        break
      digit_location += 1

    if digit_location == len(formula):
      return formula, 1
    else:
      return formula[0:digit_location], int(formula[digit_location:])

def count_atoms_in_molecule(formula):
    count_atoms = {}

    for atom in split_before_uppercases(formula):
        atom_name, atom_count = split_at_digit(atom)
        
        count_atoms[atom_name] = atom_count

    return count_atoms



def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(formula))
    return molecules_atoms_count
