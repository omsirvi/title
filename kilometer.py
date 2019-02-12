# Python Program to Convert Kilometers to Mile 

#KM to Mile 
def kmToMile(km):
    return km * 0.6237

#Mile to KM 
def mileToKm(mile):
    return mile*1.609

km = 24 
mile = kmToMile(km)
print('Mile: ', mile)

km = mileToKm(mile)
print('Km: ', km)
