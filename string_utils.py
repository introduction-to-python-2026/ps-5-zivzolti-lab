def split_before_each_uppercases(formula):
  res = []
  current_char = ""
  for char in formula:
    if char.isupper() and current_char:
      res.append(current_char)
      current_char = char
    else:
      current_char += char
      if current_char:
        res.append(current_char)
  return res
  
 def split_at_first_digit(formula):
  for i, char in enumerate(formula):
    if char.isdigit():
        return formula[:i], int(formula[i:])
  return formula, 1
   
 def count_atoms_in_molecule(molecular_formula):
    atoms_count_dict = {}
    for atom in split_before_each_uppercases(molecular_formula):
      atom_name, atom_count = split_at_first_digit(atom)
      atoms_count_dict[atom_name] = atoms_count_dict.get(atom_name, 0) + atom_count
    return atoms_count_dict

 def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")  
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")
   
def count_atoms_in_reaction(molecules_list):
    molecules_atoms_count = []
    for molecule in molecules_list:
      molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count



