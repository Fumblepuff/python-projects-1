import pandas as pd
import statsmodels.api as sms
import numpy

fast_food = pd.read_csv('fastfood.csv')
fast_food = fast_food[['total_fat','sat_fat','cholesterol','sodium','calories']]

fast_food.head()

x = fast_food[['total_fat','sat_fat','cholesterol','sodium']].values

y = fast_food[['calories']].values

x = sms.add_constant(x)

sms_model = sms.OLS(y,x)
model = sms_model.fit()

print(model.mse_total.round(2))

print(model.rsquared.round(2))

print("total_fat" + " {:.2f}".format(numpy.float64(model.params[1])))
print("sat_fat" + " {:.2f}".format(numpy.float64(model.params[2])))
print("cholesterol" + " {:.2f}".format(numpy.float64(model.params[3])))
print("sodium" + " {:.2f}".format(numpy.float64(model.params[4])))
print("dtype: "+ type(model.params[1]))


print("total_fat" + " {:.2f}".format(numpy.float64(model.pvalues[1])))
print("sat_fat" + " {:.2f}".format(numpy.float64(model.pvalues[2])))
print("cholesterol" + " {:.2f}".format(numpy.float64(model.pvalues[3])))
print("sodium" + " {:.2f}".format(numpy.float64(model.pvalues[4])))
print("dtype: "+ type(model.pvalues[1]))