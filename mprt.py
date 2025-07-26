# Ryan Gallagher
# Problem 16 - MPRT

# To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

# You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into: http://www.uniprot.org/uniprot/uniprot_id

# Alternatively, you can obtain a protein sequence in FASTA format by following: http://www.uniprot.org/uniprot/uniprot_id.fasta

samples = ["A2Z669", "B5ZC00", "P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]
with open("./datasets/rosalind_mprt.txt") as k:
    test_samples_raw = k.readlines()
    test_samples = []
    for line in test_samples_raw:
        f_line = line.replace('\n', '')
        test_samples.append(f_line)

def make_ID_dict(access_ID_list):
    # Stuff after underscore doesn't exist in name for database
    sep = '_'
    sep_dict = {}
    for ID_entry in access_ID_list:
        no_sep = ID_entry.split(sep, 1)[0]
        sep_dict[no_sep] = ID_entry 
    return sep_dict


def find_ID_protein_string(access_ID_list):
    
    # Stuff after underscore doesn't exist in name for database
    sep = '_'
    sep_list = []
    for ID_entry in access_ID_list:
        no_sep = ID_entry.split(sep, 1)[0]
        sep_list.append(no_sep)

    with open("./resources/uniprot_sprot.fasta") as f:
        fa = f.read().replace('\n', '').split('>')
        return list(filter(lambda ID: any(sample in ID for sample in sep_list), fa))


def get_ID_list_string(list_entry):
    SV = list_entry.split('SV=', 1)[1]
    return SV

def main():
    filtered_ID_list = sorted(find_ID_protein_string(test_samples))
    sep_dict = make_ID_dict(test_samples)
    for ID in filtered_ID_list:
        SV = list(get_ID_list_string(ID))
        loc_string = ""
        for i in range(0, len(SV)): # this will be the N-glycosylation motif
            if SV[i] == 'N' and (i+3 <= len(SV)):
                if SV[i+1] != 'P':
                    if SV[i+2] == 'S' or SV[i+2] == 'T':
                        if SV[i+3] != 'P':
                            loc_string += f"{i} "
        if len(loc_string) > 1:
            print(sep_dict[ID[3:9:1]]) # Big assumption that they're all 6 char IDs
            print(loc_string)

    return

if __name__ == "__main__":
    main()
