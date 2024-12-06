#Imports

import subprocess
import pandas as pd
import os
import sys


class MyFileLoader():
    def __init__(self, bed_file: str, counts_file: str, assembly: str):
        self.bed_file = bed_file
        self.counts_file = counts_file
        self.assembly = assembly
    
    def load_bed_file(self) -> pd.DataFrame:
        """
        Load BED file.
        
        Parameters:
        ----------
        bedfile: str
            Full path to the BED file

        Return:
        ----------
        bed_df: pd.DataFrame
            Pandas dataframe containing BED file
            | chr | start | end | target |
        """
        bed_df: pd.DataFrame = pd.read_csv(
            self.bed_file,
            sep='\t',
            header=0,
            names=["chr", "start", "end", "target"],
            dtype={"chr": str, "start": int, "end": int, "target": str}
        )
        return bed_df
    
    def load_counts_file(self) -> pd.DataFrame:
        """
        Load Count file.
        
        Parameters:
        ----------
        bedfile: str
            Full path to the BED file

        Return:
        ----------
        bed_df: pd.DataFrame
            Pandas dataframe containing BED file
            | chr | start | end | count |
        """
        Bed: pd.DataFrame = pd.read_csv(
            self.counts_file,
            sep='\t',
            header=0,
            names=["chr", "start", "end", "count"],
            dtype={"chr": str, "start": int, "end": int, "count": int}
        )
        return Bed

def main():
    bed_file: str = "/home/bed/bedfile.bed"
    counts_file: str = "/home/count/countfile.txt"
    assembly: str = "GRCh38"

    #Instantiate Class
    Files_loaded: MyFileLoader = MyFileLoader(bed_file=bed_file, counts_file=counts_file, assembly=assembly)
    bed_df: pd.DataFrame = Files_loaded.load_bed_file()
    count_df: pd.DataFrame = Files_loaded.load_counts_file()

if __name__ == "__main__":
    main()