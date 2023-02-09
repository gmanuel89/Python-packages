#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-02-09
#####

## Import libraries
from rdkit import Chem
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem import rdFingerprintGenerator

## Calculate the fingerprint based upon the compound structure
def calculate_fingerprint_for_compound_structure(chemical_structure_string: str, chemical_structure_format='SMILES', fingerprint_calculation_method=None, output_format='bit') -> str:
    # initialise output
    compound_fingerprint = ''
    # Return nothing if the chemical structure is non-existing
    if chemical_structure_string is None or chemical_structure_string == '':
        return compound_fingerprint
    # Read the chemical structure from the string
    try:
        # SMILES
        if chemical_structure_format.lower() == 'smiles':
            #canon_chemical_structure = Chem.CanonSmiles(chemical_structure_string)
            compound_chemical_structure = Chem.MolFromSmiles(chemical_structure_string)
            #compound_chemical_structure = Chem.MolFromSmarts(chemical_structure_string)
        # Other chemical formats
        else:
            compound_chemical_structure = None
    except:
        compound_chemical_structure = None
    # Calculate the fingerprint (if there is a structure)
    if compound_chemical_structure is not None:
        if fingerprint_calculation_method is None or fingerprint_calculation_method.lower() == 'default':
            try:
                rdkit_gen = rdFingerprintGenerator.GetRDKitFPGenerator(maxPath = 5, fpSize = 1024)
                fingerprint = rdkit_gen.GetFingerprint(compound_chemical_structure)
                compound_fingerprint = fingerprint.ToBitString()
            except:
                pass
        else:
            try:
                if output_format == 'bit':
                    compound_fingerprint = FingerprintMols.FingerprintMol(compound_chemical_structure).ToBitString()
                elif output_format == 'base64':
                    compound_fingerprint = FingerprintMols.FingerprintMol(compound_chemical_structure).ToBase64()
                else:
                    pass
            except:
                pass
    # return
    return compound_fingerprint