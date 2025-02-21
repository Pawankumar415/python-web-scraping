
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_population"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract column headers
columns = [th.text.split("[")[0].strip() for th in soup.find_all('th', rowspan='2')]

# Extract table rows
rows = soup.find_all('tbody')[1].find_all('tr')[2:38]

# Extract data using list comprehensions
data = [[td.text.strip() for td in row.find_all('td')] for row in rows]

# Unpacking data into respective lists
Rank, State_or_Union_Territory, Population, India, Growth_2001_2012, Population_estimate_2023, *_ , Density, Sex_ratio = zip(*data)

# Convert tuples to lists for tabulate compatibility
data_dict = {
    columns[0]: list(Rank),
    columns[1]: list(State_or_Union_Territory),
    columns[2]: list(Population),
    columns[3]: list(India),
    columns[4]: list(Growth_2001_2012),
    columns[5]: list(Population_estimate_2023),
    columns[6]: list(Density),
    columns[7]: list(Sex_ratio)
}

# Generate a formatted table
table = tabulate(data_dict, headers="keys", tablefmt="pipe", colalign=("center",))

# Print the table
print(table)
