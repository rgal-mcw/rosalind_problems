def open_fasta(file):
    with open(file) as f:
        fa = f.read().splitlines()
        fa_reads = []
        read = ""
        for line in fa:
            if line.startswith(">"):
                fa_reads.append(read)
                read = ""
            else:
                read += line
        fa_reads.append(read)
        fasta = fa_reads[1:]
    return fasta
