def price_of_tomato(price_per_kg):
    land_of_30=16 *(30/100)
    production_of_30=land_of_30*10*1000
    land_of_70=16-land_of_30
    production_of_70=land_of_70*12*1000
    total_kg=production_of_30+production_of_70
    return price_per_kg*total_kg

def price_of_potato(price_per_kg):
    production=16*10*1000
    return price_per_kg*production

def price_of_cabbage(price_per_kg):
    production=16*14*1000
    return price_per_kg*production

def price_of_sunflower(price_per_kg):
    production=16*0.7*1000
    return production*price_per_kg

def price_of_sugar_cane(price_per_tonnes):
    production=45*16
    return production*price_per_tonnes

print("Sales Amount of Tomato:",price_of_tomato(7))
print("Sales Amount of Potatoes:",price_of_potato(20))
print("Sales Amount of cabbage:",price_of_cabbage(24))
print("Sales Amount of Sunflower:",price_of_sunflower(200))
print("Sales Amount of Sugar Cane:",price_of_sugar_cane(4000))

total=price_of_tomato(7)+price_of_potato(20)+price_of_cabbage(24)+price_of_sunflower(200)+price_of_sugar_cane(4000)
print("Total:",total)

print("Sales realisation from chemical-free farming at the end of 11 months", total-price_of_sugar_cane(4000))