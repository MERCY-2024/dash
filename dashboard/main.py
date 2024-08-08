import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("./sample.xlsx")
print(df.to_string())

# Create a bar chart
plt.bar(df['product'], df['price'], color='skyblue')
plt.title('product vs price')
plt.xlabel('product')
plt.ylabel('price')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()