#import covid library
import covid
#import matplotlib library
import matplotlib
from covid import Covid
import matplotlib.pyplot as plt
covid = Covid() #calling function
name = input("Enter the country name to find : ")
virusdata = covid.get_status_by_country_name (name)
remove=['id','country','latitude','longitude','last_update'] #we need to remove unnecessary
for i in remove:
    virusdata.pop(i)    
all = virusdata.pop('confirmed')
print (virusdata)
id = list(virusdata.keys())
value = [str(i) for i in virusdata.values() ]
plt.pie(value, labels = id, colors =['r','y','g','b'] ,autopct='%1.1f%%')
plt.title("COUNTRY : "+name.upper() +"\n TOTAL CASES : "+str(all))
plt.legend()
plt.show()
#project done by Deepak Perla
