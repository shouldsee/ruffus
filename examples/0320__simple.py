import ruffus as rf

def run_bwa(input_file, output_file):
    print "Align DNA sequences in %s to a genome -> %s " % (input_file, output_file)
    # make dummy output file
    open(output_file, "w").close()    
    
def sort_bam(input_file, output_file):
    print "Sort DNA sequences in %s -> %s " % (input_file, output_file)
    # make dummy output file
    open(output_file, "w").close()    
    
pipe1 = lambda INDATA: rf.transform(
    INDATA, 
    rf.suffix(".fastq"),
    ".bam")(run_bwa)
pipe2 = lambda INDATA: rf.transform(
    INDATA, 
    rf.suffix(".bam"), 
    ".sorted.bam",
)(sort_bam)

try:
    rf.Pipeline.pipelines.pop('test')
except:
    pass
# pp = rf.Pipeline('test')
data_files = [(prefix + ".fastq") for prefix in list("abcdefghij")]
for df in data_files:
    open(df, "w").close()

job = pipe2(pipe1(data_files))

rf.pipeline_run([job ], multithread = 1)
