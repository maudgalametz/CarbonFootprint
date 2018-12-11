# Calculate your carbon footprint


### Description

Calculate your carbon footprint from a csv file containing your travels with Origin and Destination as two separate columns. 

The script calculates the geodesic distance return in km and multiplies by an average value of the CO2 equivalent passenger / km factor
depending on the distance of the flight. The average has been estimated using the values provided by the French DGAC estimator:
https://eco-calculateur.dta.aviation-civile.gouv.fr/

To take radiative forcing into account, we multiply the emission by 1.891 as recommended by the UK Department for Environment, Food \& Rural Affairs



## How to use the script Carbonfootprint.py:

**Inputs:** 

file: csv file containing the Origin and Destination as two separate columns

**Output** 

The total CO2 emission in tons including or nor the radiative forcing.


**Example** 

Carbonfootprint('ListFlight.csv')


## Versioning

We use python 2.7.12. 


## Authors

* **Maud Galametz** 

