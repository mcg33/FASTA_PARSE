#!/usr/bin/env python

"""
Basic argparser structure:

A script showing the basic structure of an argparser function
"""

# Imports
import argparse
import sys
import os
import pandas as pd
from Basic_class_fileLoader import MyFileLoader

SCRIPT_DIR: str = os.path.dirname(__file__)
sys.path.append(os.path.dirname(SCRIPT_DIR))
FILE_ROOT: str = os.path.dirname(SCRIPT_DIR)

# Read package version
with open(f"{os.path.dirname(SCRIPT_DIR)}/path/to/version_file/__version__", "r") as version_file:
    __version__: str = version_file.read().strip()

# Parse input arguments
def parse_arguments() -> argparse.Namespace:
    """
    Parse arguments passed to the script.

    Returns:
        namespace: namespace object with options parsed from the command line.
    """
    argv = None

    argv = argv if argv is not None else sys.argv[1:]
    # Checking for "--version" in arguments
    if "--version" in argv:
        print("Version: %s" % __version__)
        sys.exit(0)
    
    parser = argparse.ArgumentParser(prog="somatic_qc_coverage")

    parser.add_argument(
        "-c",
        "--conf_file",
        dest="conffile",
        required=False,
        type=str,
        default="BACKEND CONFIG PATH",
        help="Path to back configuration file"
    )
    parser.add_argument(
        "-i",
        "--vcf",
        dest="input_vcf",
        required=True,
        type=str,
        help="Path to input VCF list of variants VCF file with SNVs and Indels."
    )
    parser.add_argument(
        "-o",
        "--outdir",
        dest="outdir",
        required=True,
        type=str,
        help="Path to output directpry"
    )
    parser.add_argument(
        "-l",
        "--log_file",
        required=False,
        dest="log_file",
        type=str,
        default="PATH TO LOG_FILE in BACKEND",
        help="Path to file where messages are logged"
    )
    parser.add_argument(
        "-f",
        required=False,
        dest="force",
        type=bool,
        help="If output/log files already exist, they are overwritten."
    )
    parser.add_argument(
        "-v",
        "--version",
        dest="version",
        required=False,
        type=str,
        help="If output/log files already exist, they are overwritten."
    )

    # If no args provided, print help & exit
    if len(argv) == 0:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    parser.set_defaults()
    options = parser.parse_args(argv)

    return options

def main():
    """
    This is the main function where I load my paser to a Namespace object
    """
    # Parse CLI arguments
    args: argparse.Namespace = parse_arguments()

    # Clean in case --force-overwrite
    suffix_list: list[str] = [".coverageQC.tab", ".coverageQC_efficiency.log", "etc.etc", "this.txt", "_that.tab"]

    if args.force == True:
        for file in os.listdir(args.outdir):
            if any(file.endswith(suffix) for suffix in suffix_list):
                file_path = os.path.join(args.outdir, file)
                os.remove(file_path)

    #Run the main function
    run(config_path=args.conffile, input_vcf=args.vcf_file, outdir=args.outdir)

def run(config_path: str, input_vcf: str, outdir: str) -> None:
    """
    The main function

    Parameters
    ----------
    config_path : str
        Class containing the contents of the backend config file.
    input_vcf : FilePath
        Path to the input list of variants VCF file with SNVs and Indels.
    VCF_SV : FilePath
        (optional) Path to VCF file with SVs.
    logger : PypeLogger
        Loggin class that sends script updates to a log file

    Returns:
    ----------
    countsfile : filePath
        File path to sample_name_counts.txt file
    """
    #Load file
    Loaded_files: MyFileLoader = MyFileLoader(vcf_file=input_vcf)

    vcf_df: pd.DataFrame = Loaded_files.load_vcf_file()

    #Hello there
    print("Add the relevant stuff in here")

    return None

if __name__ == "__main__":
    main()