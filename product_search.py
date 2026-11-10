import pandas as pd

# قراءة ملف البيانات
df = pd.read_excel("Product_Data.xlsx")

print("Search By:")
print("1 - Product ID")
print("2 - Product Name")

choice = input("Choose Search Type (1 or 2): ")

if choice == "1":

    product_id = int(input("Enter Product ID: "))

    result = df[df["ProductID"] == product_id]

    if not result.empty:
        print("\nProduct Found:")
        print(result[["ProductID", "Name", "ListPrice"]])

    else:
        print("Product not found.")

elif choice == "2":

    product_name = input("Enter Product Name: ")

    result = df[df["Name"].str.contains(product_name, case=False, na=False)]

    if not result.empty:
        print("\nProduct Found:")
        print(result[["ProductID", "Name", "ListPrice"]])

    else:
        print("Product not found.")

else:
    print("Invalid choice.")
