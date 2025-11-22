


def split_before_uppercases(formula):
  start = 0
  end = 0
  split_formula = []
  for char in formula [1:]:
    end += 1
    if char.isupper():
      substring = formula[start:end]
      split_formula.append(substring)
      start =end
    
  substring = formula[start:]
  if substring is not None and substring != "":
    split_formula.append(substring)
  
  return (split_formula) 

def split_at_digit(formula):
  digit_location = 1
  for char in formula[1:]:
    if char.isdigit() == True:
      break
    digit_location += 1

  if digit_location == len(formula):
    prefix = formula 
    numeric = 1
  else:
    prefix = formula[:digit_location]
    numeric = int(formula[digit_location:])

  return (prefix, numeric)

def split_before_each_uppercases(formula):
  start = 0
  end = 0
  split_formula = []
  for char in formula [1:]:
    end += 1
    if char.isupper():
      substring = formula[start:end]
      split_formula.append(substring)
      start =end
    
  substring = formula[start:]
  if substring is not None and substring != "":
    split_formula.append(substring)
  
  return (split_formula)  


def split_at_first_digit(formula):
  digit_location = 1
  for char in formula[1:]:
    if char.isdigit() == True:
      break
    digit_location += 1

  if digit_location == len(formula):
    prefix = formula 
    numeric = 1
  else:
    prefix = formula[:digit_location]
    numeric = int(formula[digit_location:])

  return (prefix, numeric)


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    # Step 1: Initialize an empty dictionary to store atom counts
    names_counts_dict = {}
    for atom in split_before_each_uppercases(molecular_formula):
        atom_name, atom_count = split_at_first_digit(atom)
        
        # Step 2: Update the dictionary with the atom name and count
        names_counts_dict[atom_name] = atom_count
    # Step 3: Return the completed dictionary
    return names_counts_dict


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
