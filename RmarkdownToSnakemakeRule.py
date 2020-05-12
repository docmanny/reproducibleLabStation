#! /usr/bin/env python3

# import Click
# 
from pathlib import Path
import re

def __main__(Rmd_file, output="pdf"):
  '''Function converts an RMarkdown file into a snakemake rule for compiling it. 
  Function looks for "read" and "write" functions to create "input" and "output" rules; 
  it will also add a final output for the desired knit type.
  '''
    rmd_file = Path(Rmd_file)
    # pattern
    pat.input = re.compile("^\s*(?P<varName>)(?:\s*->\s*read[._])")
    
    
    with rmd_file.open() as rmd:
        for line in rmd:
            line = line.strip()
            if line.startsWith("read")
