import os
import subprocess

# Задаем путь к папке с данными
data_dir = '/app/data'  # измените на актуальный путь к папке data
bed_file = os.path.join(data_dir, 'smn1_regions.bed')  # Предполагаем, что file.bed находится в папке data

# Получаем список всех BAM-файлов в папке
bam_files = [file for file in os.listdir(data_dir) if file.endswith('.bam')]

# Перебираем все BAM-файлы и выполняем команду samtools depth для каждого
for bam_file in bam_files:
    bam_path = os.path.join(data_dir, bam_file)
    output_path = os.path.join(data_dir, f'{bam_file}_depth_output.txt')
    
    # Формируем команду для выполнения
    command = f'samtools depth -a -b {bed_file} {bam_path} > {output_path}'
    
    # Запускаем команду
    subprocess.run(command, shell=True)

# Запуск других скриптов можно осуществить после выполнения всех команд samtools
subprocess.run('python3 depth_scripts/combine_depth_files.py', shell=True)
subprocess.run('python3 depth_scripts/visualisation.py', shell=True)
