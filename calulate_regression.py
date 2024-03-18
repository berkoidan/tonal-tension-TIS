import numpy as np
import statsmodels.api as sm

def calculate_regression(y, x1, x2):
    X = np.vstack((x1, x2)).T
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()
    w = results.params[1:]
    stats = {
        'r_squared': results.rsquared,
        'p_values': results.pvalues[1:]
    }
    return w, stats

