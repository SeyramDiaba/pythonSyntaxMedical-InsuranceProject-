# create the initial variables below
age=28
sex=0
bmi=26.2
num_of_children=3
smoker=0

# Add insurance estimate formula below
insurance_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500
print("This person's insurance cost is "+str(insurance_cost)+" dollars.")
# Age Factor
age += 4
new_insurance_cost=insurance_cost
change_in_insurance_cost=new_insurance_cost-insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is "+str(change_in_insurance_cost)+" dollars.")
age=28
# BMI Factor
bmi +=3.1
new_insurance_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500
change_in_insurance_cost=new_insurance_cost-insurance_cost
print("The change in estimated insurace cost after increasing BMI by 3.1 is "+str(change_in_insurance_cost)+" dollars.")
bmi=26.2
# Male vs. Female Factor
sex=1
new_insurance_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500
change_in_insurance_cost=new_insurance_cost-insurance_cost
print("The change in estimated cost for being male instead of female is "+str(change_in_insurance_cost)+" dollars.")
num_of_children +=1
# Extra Practice
new_insurance_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500

change_in_insurance_cost=new_insurance_cost-insurance_cost
print("The change in estimated cost for change in number of children is "+str(change_in_insurance_cost)+" dollars.")
smoker=1
#smoker change in cost
new_insurance_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500
change_in_insurance_cost=new_insurance_cost-insurance_cost
print("The change in estimated cost for smokers is "+str(change_in_insurance_cost)+" dollars.")