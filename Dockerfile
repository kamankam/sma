FROM python:3.9

#install Python, samtools
RUN apt-get update && apt-get install -y \
  samtools 

#move to app folder (docker run -v папка снаружи:/data)
WORKDIR /app

#copy all our folders into workdir
COPY . .

# Устанавливаем samtools и другие зависимости
RUN pip3 install -r requirements.txt

# Даем права на выполнение скриптам
RUN chmod +x /app/depth_scripts/depth_analysis.sh
RUN chmod +x /app/depth_scripts/combine_depth_files.py 
RUN chmod +x /app/depth_scripts/visualisation.py

#run bash script at start moument
CMD ["/app/depth_scripts/depth_analysis.sh"]