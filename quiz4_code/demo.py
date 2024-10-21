def my_favorite_library(libraries, i):
    count = len(libraries)
    print(f"I love {libraries[i]} Library out of the {count} libraries.")

jmu_libraries = ["Rose", "Express", "Music", "ETMC"]
construction = "Carrier"

for item in enumerate(jmu_libraries):
    print(f"{item[0] + 1}: {item[1]} library")
    
print(f"5: {construction} library under construction")

my_favorite_library(jmu_libraries, 0)

    
