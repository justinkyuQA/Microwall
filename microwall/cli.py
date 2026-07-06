import argparse
from pathlib import Path

def analyze(path):

    p=Path(path)

    if not p.exists():
        print("Rule file not found.")
        return

    rules=[]

    with open(p) as f:
        for line in f:
            line=line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            rules.append(line)

    print()
    print("MicroWall")
    print("="*40)
    print("Rules Loaded :",len(rules))
    print()

    allow=0
    deny=0

    for rule in rules:

        text=rule.lower()

        if "accept" in text or "allow" in text:
            allow+=1

        if "drop" in text or "deny" in text or "reject" in text:
            deny+=1

        print(rule)

    print()
    print("="*40)
    print("Summary")
    print("="*40)
    print("Allow :",allow)
    print("Block :",deny)

def main():

    parser=argparse.ArgumentParser(
        prog="microwall",
        description="Tiny firewall rule analyzer"
    )

    parser.add_argument(
        "rules",
        help="iptables/nftables rule file"
    )

    args=parser.parse_args()

    analyze(args.rules)
