#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-02-09
#####

## Import libraries
from rdkit import Chem

## Determine if the chemical structure string is a valid (and parsable) string
def determine_if_chemical_structure_is_valid(chemical_structure_string: str, chemical_structure_format='SMILES') -> bool:
    # Initialise output variable
    molecular_structure_is_valid = False
    # Try to parse it
    try:
        # SMILES
        if chemical_structure_format.lower() == 'smiles':
            compound_chemical_structure = Chem.MolFromSmiles(chemical_structure_string)
            if compound_chemical_structure is not None:
                molecular_structure_is_valid = True
        # Other chemical format
        else:
            pass
    except:
        pass
    # return
    return molecular_structure_is_valid
