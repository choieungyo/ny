import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, help='choose flight mode follow or scanning')

args = parser.parse_args()
if args.mode == "follow":
    print("start following")
elif args.mode == "scan":
    print("start scanning")
    
