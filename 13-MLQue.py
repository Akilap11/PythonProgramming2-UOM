#python libraries
#jupyter notebooks,pandas,numpy,scipy,scikit-learn,matplotlib

# Unknown new data point that needs to be labeled for rain or no rain
new_data_rain = int(input())
new_data_humidity = int(input())
# Training Data Examples for rain and no_rain
rain_temp,rain_humidity = [45,55,55],[60,65,55]  #second part's lowest number is the number that not rain
no_rain_temp,no_rain_humidity=[35,50,40],[45,30,35]

# Simple distance based approach to lable the unknown new data point
rain=0
no_rain=0
sz=len(rain_temp)
for i in range(sz):
  rain+=abs(rain_temp[i]-new_data_rain)
  rain+=abs(rain_humidity[i]-new_data_humidity)
  no_rain+=abs(no_rain_temp[i]-new_data_rain)
  no_rain+=abs(no_rain_humidity[i]-new_data_humidity)
# print("Distance to Rain data =", rain)
# print("Distance to No Rain data = ", no_rain)

# Print the label of unknown new data point based on the total distance to each group
if rain < no_rain: 
  print("RAIN")
else:
  print("NO RAIN")