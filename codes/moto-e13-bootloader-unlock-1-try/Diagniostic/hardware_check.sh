#!/bin/bash
# codes/diagnostics/hardware_check.sh

echo "[*] Inizio diagnostica hardware Hulara..."

# Verifica connessione ADB
if ! adb get-state > /dev/null 2>&1; then
    echo "[!] Errore: Nessun dispositivo trovato in modalità ADB."
    exit 1
fi

# Estrazione dati critici
echo "--- INFO DISPOSITIVO ---"
adb shell getprop ro.product.model
adb shell getprop ro.product.board
echo "--- STATO BOOTLOADER ---"
adb shell getprop ro.boot.flash.locked

echo "[+] Diagnostica completata."
