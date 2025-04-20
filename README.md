# Coding_project_fundamental_of_Data_science
📊 Newborn Weight Distribution Analysis
This project analyzes a dataset containing the weights of 400 newborns from a specific region in Europe. The weights are recorded in kilograms and are used to study the distribution pattern of newborn weight in that area over a certain period.

🔍 Objective
The main goal is to visualize the distribution of newborn weights using a histogram, and calculate key statistical values like the mean weight and the 33rd percentile (denoted as X). This helps in understanding how newborn weights are spread across the population and where most of the values lie.

🛠️ Tools and Libraries Used
NumPy – for numerical computations (mean, percentile)

Matplotlib – for data visualization (histogram)

CSV – for reading the dataset

📈 Visualization
The histogram displays:

X-axis: Newborn weights (in kg)

Y-axis: Approximate number of newborns having those weights

📌 Key Statistics

Mean Weight
The mean weight is calculated using the formula:

$$
\bar{W} = \frac{1}{n} \sum_{i=1}^{n} a_i
$$
 
Where n = 400, and a_i
is the weight of the i-th newborn.
Using np.mean(data), the calculated mean is approximately:

3.58573 kg
This value is shown as a blue vertical line in the histogram.

📉 Insights
The distribution appears to be approximately normal, centered around the mean.

The mean and the 33rd percentile give useful insights into how newborn weights are spread.

The histogram effectively illustrates that most of the newborns' weights cluster around the 3.5 to 3.6 kg range.
