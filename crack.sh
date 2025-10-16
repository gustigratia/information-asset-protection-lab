#!/bin/bash
set -euo pipefail


WORKDIR="$HOME/hash-crack"
mkdir -p "$WORKDIR"
cd "$WORKDIR"


touch cracked.txt
printf '%s\n' "28cc09d8d8959871a97b24a07d87bcb05b9f3e7ac6d9f20ff82196ca5f908b2c" > hash1.txt
printf '%s\n' "6c569aabbf7775ef8fc570e228c16b98" > hash2.txt

ROCKYOU="/home/delpiera/Downloads/rockyou.txt"
if [ ! -f "$ROCKYOU" ]; then
echo "Error: rockyou wordlist not found at $ROCKYOU"
exit 1
fi


hashcat -m 17800 -a 0 -o cracked.txt hash1.txt "$ROCKYOU" 

hashcat -m 0 -a 0 -o cracked.txt hash2.txt "$ROCKYOU"

cat cracked.txt

exit 0
