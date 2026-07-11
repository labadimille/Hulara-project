#!/bin/bash
# codes/backup/sync_data.sh

DEST="data/backup_$(date +%Y%m%d)"
mkdir -p $DEST

echo "[*] Sincronizzazione in corso..."
adb pull /sdcard/Download $DEST
echo "[+] Backup completato in $DEST"
