#!/bin/bash

# Путь к директории с BAM файлами
BAM_DIR="/data"

# Путь к BED файлу
BED_FILE="./smn1_regions.bed"

# Перебираем все BAM файлы в директории
for BAM_FILE in $BAM_DIR/*.bam
do
    # Извлекаем имя файла без расширения
    BASE_NAME=$(basename $BAM_FILE .bam)

    # Выполняем samtools depth
    samtools depth -a -b $BED_FILE $BAM_FILE > "${BAM_DIR}/${BASE_NAME}_depth_output.txt"
done

# Выполняем Python скрипты после команды samtools
   python3 ./depth_scripts/combine_depth_files.py
   python3 ./depth_scripts/visualisation.py
