#!/bin/bash
git add .
read -p "Enter Commit Message: " msg
git commit -m "$msg"
git push origin main
[ -z "$1" ] && git push origin main || git push origin "$1"
echo "[+] Successfully pushed to GitHub!"
