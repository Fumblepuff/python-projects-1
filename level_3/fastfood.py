import pandas as pd
import statsmodels.api as sms

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

#print(model.params.round(2))

for i in range(len(model.params)):
    print("{:.2f}".format(model.params[i]))

#print(model.pvalues.round(2))

for i in range(len(model.pvalues)):
    print("{:.2f}".format(model.pvalues[i]))