# input a genome file and return a file genome.chrom.sizes to be associated with the custom build (or just have it as an output to be used later in the history.
# adapted from https://bioexpressblog.wordpress.com/2014/04/15/calculate-length-of-all-sequences-in-an-multi-fasta-file/
from sys import argv
# python calculating_chrom.sizes.py genome_input.fa output.chrom.sizes
genome = str(argv[1])
output = str(argv[2])
# genome = 'test-data/test.fasta'
# output = "test-data/test_chrom.sizes"

chromSizesoutput = open(output,"w")

records = []
record = False
for line in open(genome, 'r').readlines():
	if line[0] == '>':
		if record:
			records.append(record)
		record = [line.strip("\n").split(' ')[0][1:], 0]

	else:
		sequence = line.strip('\n')
		record[1] += len(sequence)
		
for seq_record in records:
	output_line = '%s\t%i\n' % (seq_record[0], seq_record[1])
	chromSizesoutput.write(output_line)

chromSizesoutput.close()
