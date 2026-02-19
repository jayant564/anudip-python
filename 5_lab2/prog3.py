# Hospital Emergency Triage 
# Patients are categorized as: 
# • Critical (heart rate abnormal OR severe injury) 
# • Moderate 
# • Normal 
# If age > 65 and condition is moderate → Upgrade priority. 
age = int(input("Enter age: "))
heart_rate_abnormal = input("Is heart rate abnormal? (yes/no): ").lower()
severe_injury = input("Is there severe injury? (yes/no): ").lower()
condition = input("Enter condition (normal/moderate): ").lower()

if heart_rate_abnormal == "yes" or severe_injury == "yes":
    print("Category: Critical")
elif condition == "moderate":
    if age > 65:
        print("Category: Critical (Upgraded due to age)")
    else:
        print("Category: Moderate")
else:
    print("Category: Normal")
