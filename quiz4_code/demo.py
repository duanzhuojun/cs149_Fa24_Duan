def my_favorite_library(libraries, index):
    count = len(libraries)
    print(f"There are {count} at JMU open now. My favorite library is {libraries[index]}")

jmu_libraries = ["Rose Library", "Express Library", "Music Library", "ETMC"]
under_construction = "Carrier Library"

for item in enumerate(jmu_libraries):
    print(f"JMU library {item[0] + 1}: {item[1]}")
    
print(f"JMU library 5: {under_construction} under construction")

my_favorite_library(jmu_libraries, 0)

    
