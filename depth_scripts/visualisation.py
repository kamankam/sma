
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных
data = pd.read_csv("/app/data/combined_depth_data.csv")

# Фильтрация данных для генов SMN1 и SMN2
smn1_data = data[(data['Chromosome'] == 'chr5') & 
                 (data['Position'] >= 70924941) & 
                 (data['Position'] <= 70966375)]

# Функция для деления гена на интервалы по 500 нуклеотидов
def divide_gene_into_intervals(start, end):
    interval_length = 500
    intervals = list(range(start, end, interval_length))
    if intervals[-1] != end:
        intervals.append(end)  # Добавляем последний интервал
    return intervals

# Применение функции к генам SMN1
intervals_smn1 = divide_gene_into_intervals(70924941, 70966375)


# Пересчет средней глубины покрытия с новыми интервалами
def calculate_avg_depth_by_new_intervals(data, intervals):
    avg_depths = {sample: [] for sample in data['Sample'].unique()}
    for i in range(len(intervals)-1):
        interval_start = intervals[i]
        interval_end = intervals[i+1]
        interval_data = data[(data['Position'] >= interval_start) & (data['Position'] < interval_end)]
        for sample in avg_depths.keys():
            sample_data = interval_data[interval_data['Sample'] == sample]
            avg_depth = sample_data['Depth'].mean()
            avg_depths[sample].append(avg_depth)
    return avg_depths

# Расчет средней глубины покрытия для SMN1 
avg_depths_smn1_new = calculate_avg_depth_by_new_intervals(smn1_data, intervals_smn1)


colors = ['green', 'blue', 'red']

# Создание графиков с точками, соединенными линиями
plt.figure(figsize=(15, 10))

# График для SMN1
plt.subplot(2, 1, 1)
for i, (sample, depths) in enumerate(avg_depths_smn1_new.items()):
    plt.plot(intervals_smn1[:-1], depths, label=sample, color=colors[i % len(colors)], marker='o')
plt.title('Средняя глубина покрытия по интервалам для SMN1')
plt.xlabel('Позиция')
plt.ylabel('Средняя глубина покрытия')
plt.legend()
plt.savefig('/app/data/smn1_depth_coverage_plot.png')

