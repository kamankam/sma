# -*- coding: utf-8 -*-
import pandas as pd
import os

# Путь к директории с файлами глубины покрытия
directory = '/app/data'

# Создаем пустой DataFrame
combined_data = pd.DataFrame()

for filename in os.listdir(directory):
    if filename.endswith('_depth_output.txt'):
        # Путь к файлу
        file_path = os.path.join(directory, filename)

        # Загрузка данных из файла
        data = pd.read_csv(file_path, sep='\t', header=None, names=['Chromosome', 'Position', 'Depth'])

        # Добавление колонки с именем образца
        sample_name = filename.replace('_depth_output.txt', '')
        data['Sample'] = sample_name

        # Добавление данных в общий DataFrame
        combined_data = pd.concat([combined_data, data])

# Сохраняем объединенные данные в новый файл
combined_data.to_csv('/app/data/combined_depth_data.csv', index=False)
