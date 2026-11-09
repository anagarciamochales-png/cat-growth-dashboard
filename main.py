# ================

# IMPORTS

# ================ 

import matplotlib.pyplot as plt
from datetime import datetime
# ================

# CONSTANTS

# ================ 

birth_dates = {
    "Misty": "2023-07-22",
    "Ash": "2023-10-27"
}

ideal_ranges = {
    "Misty": (4.8, 5.8),
    "Ash": (6.8, 7.5)
}



# ================

# HELPER FUNCTIONS

# ================ 

def calculate_age_months(cat_name, date):
    birth = datetime.strptime(
        birth_dates[cat_name],
        "%Y-%m-%d"
    )

    measurement = datetime.strptime(
        date,
        "%Y-%m-%d"
    )

    age_months = (
        measurement - birth
    ).days / 30.44

    return age_months

def calculate_age_years_months(age_months):
    total_months = round(age_months)

    years = total_months // 12
    months = total_months % 12

    return years, months


# ================

# DASHBOARD FUNCTIONS

# ================

def dashboard_summary():
    cat_data = {}
    with open("cat_data.csv", "r") as file:
        next(file)
        
        for line in file:
            row = line.strip().split(",")
            
            name = row[0]
            date = row[1]
            weight = float(row[2])
            
            if name not in cat_data:
                cat_data[name] = []

            cat_data[name].append((date, weight))
        
    print("\n==== Cat Growth Dashboard Summary ====")
   
    for cat, measurements in cat_data.items():
        weights = []
        
        for date, weight in measurements:
               weights.append(weight)

        first_weight = weights[0]
        current_weight = weights[-1]
        recent_weights = weights[-3:]

        if recent_weights[-1] > recent_weights[0]:
            trend = "📈 Increasing"
        elif recent_weights[-1] < recent_weights[0]:
            trend = "📉 Decreasing"
        else:
            trend = "➡️ Stable"

        

        highest_weight = max(weights)
        gain = current_weight - first_weight
        measurement_count = len(weights)

        latest_date = measurements[-1][0]
        
        age_months = calculate_age_months(
            cat,
            latest_date
            
            )
        
        years, months = calculate_age_years_months(age_months)

        ideal_min, ideal_max = ideal_ranges[cat]

        if current_weight < ideal_min:
            status = "⚠️ Below Range"
        elif current_weight > ideal_max:
            status = "⚠️ Above Range"
        else:
            status = "✅ Healthy"

        print(f"\n{cat}")
        print("-" * 25)
        print(f"Age: {years}y {months}m")
        print(f"Current Weight: {current_weight:.2f} kg")
        print(f"Ideal Range: {ideal_min:.1f} - {ideal_max:.1f} kg")
        print(f"Status: {status}")
        print(f"Trend: {trend}")

        print()

        print(f"First Weight: {first_weight:.2f} kg")
        print(f"Highest Weight: {highest_weight:.2f} kg")
        print(f"Weight Gain: {gain:.2f} kg")

        print()

        print(f"Measurements: {measurement_count}")


# ================
 
# GRAPH FUNCTIONS

# ================

def create_growth_graph(cat_name):
    ages = []
    weights = []

    with open("cat_data.csv", "r") as file:
        next(file)

        for line in file:
            row = line.strip().split(",")

            name = row[0]
            date = row[1]
            weight = float(row[2])
            
            age_months = calculate_age_months(
                name,
                date
                )

            if name == cat_name:
                ages.append(age_months)
                weights.append(weight)
    

    
    current_age = ages[-1]
    current_weight = weights[-1]

    ideal_min, ideal_max = ideal_ranges[cat_name]
    if current_weight < ideal_min:
        status = "Below Range"
    elif current_weight > ideal_max:
        status = "Above Range"
    else:
        status = "Healthy"

    
    plt.figure(figsize=(12, 6))
    
    current_age = ages[-1]
    years, months = calculate_age_years_months(current_age)

    summary = (
        f"Age: {years}y {months}m\n"
        f"Current Weight: {current_weight:.2f} kg\n"
        f"Status: {status}"
        )

    plt.text(
        0.98,
        0.02,
        summary,
        transform=plt.gca().transAxes,
        ha="right",
        va="bottom",
        bbox=dict(
            facecolor="white",
            alpha=0.8,
            edgecolor="gray"
            )
        )


    plt.title(f"{cat_name} Weight Growth")
    plt.xlabel("Age (months)")
    plt.text(6, -0.12, "Kitten", transform=plt.gca().get_xaxis_transform())
    adult_center = (12 + max(ages)) / 2
    plt.text(adult_center, -0.12, "Adult", transform=plt.gca().get_xaxis_transform())
    plt.ylabel("Weight (kg)")
    plt.xticks(range(int(min(ages)), int(max(ages)) + 1, 2))
    plt.axvline(x=12, color="red", linestyle="--")
    plt.text(
    12.2,
    max(weights) - 0.2,
    "12 Months\nAdult",
    )
    plt.plot(
    ages,
    weights,
    color="tab:blue",
    marker="o",
    markersize=4
    )
  
    #plt.axvspan(0, 12, alpha=0.18, color="lightblue")
    #plt.axvspan(12, max(ages), alpha=0.18, color="lightgreen")
    plt.fill_between(
        ages,
        ideal_min,
        ideal_max,
        where=[age >= 12 for age in ages],
        color="gold",
        alpha=0.20
        )



    plt.grid(axis="y", alpha=0.4)
    plt.tight_layout()
    plt.savefig(f"charts/{cat_name.lower()}_growth.png")
    plt.show()


dashboard_summary()
create_growth_graph("Misty")
create_growth_graph("Ash")
