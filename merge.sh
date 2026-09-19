#!/usr/bin/env bash

set -u

DIR1="./com1"
DIR2="./com3"
DEST="./unificado"

if [[ ! -d "$DIR1" || ! -d "$DIR2" ]]; then
    echo "Error: no existen $DIR1 y/o $DIR2"
    exit 1
fi

mkdir -p "$DEST"

conflicts=0

mapfile -t files < <(
    {
        find "$DIR1" -type f -printf '%P\n'
        find "$DIR2" -type f -printf '%P\n'
    } | sort -u
)

for file in "${files[@]}"; do

    f1="$DIR1/$file"
    f2="$DIR2/$file"
    dest="$DEST/$file"

    mkdir -p "$(dirname "$dest")"

    # Solo existe en com1
    if [[ -f "$f1" && ! -f "$f2" ]]; then
        echo "[COM1]      $file"
        cp -p "$f1" "$dest"
        continue
    fi

    # Solo existe en com3
    if [[ -f "$f2" && ! -f "$f1" ]]; then
        echo "[COM3]      $file"
        cp -p "$f2" "$dest"
        continue
    fi

    # Ambos existen
    time1=$(stat -c '%Y' "$f1")
    time2=$(stat -c '%Y' "$f2")

    if [[ "$time1" -gt "$time2" ]]; then
        echo "[COM1]      $file  (más reciente)"
        cp -p "$f1" "$dest"

    elif [[ "$time2" -gt "$time1" ]]; then
        echo "[COM3]      $file  (más reciente)"
        cp -p "$f2" "$dest"

    else
        # Misma fecha: comparar contenido
        if cmp -s "$f1" "$f2"; then
            echo "[IGUALES]   $file"
            cp -p "$f1" "$dest"
        else
            echo "[CONFLICTO] $file"
            echo "            No se copia ninguna versión"
            conflicts=$((conflicts + 1))
        fi
    fi

done

echo
echo "========================================"
echo "Unificación terminada"
echo "========================================"
echo "Conflictos: $conflicts"

if [[ "$conflicts" -gt 0 ]]; then
    echo
    echo "Los archivos en conflicto NO fueron copiados."
    echo "El directorio '$DEST' puede contener una unificación parcial."
else
    echo
    echo "No hubo conflictos."
fi
