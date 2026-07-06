#Q2a -------------------------------------------------------------------

print("Before addition, 2e16 == 2 * 10 ** 16 returns", 2e16 == 2 * 10 ** 16)

print("After addition, 2e16 + 1 == 2 * 10 ** 16 + 1 returns", 2e16 + 1 == 2 * 10 ** 16 + 1)

#Q2b -------------------------------------------------------------------

import numpy as np
import plotnine as p9
import pandas as pd

x0 = 3
h = np.logspace(-10, 0)
f = lambda x: x**3

error = abs(((f(x0 + h) - f(x0)) / h) - 3 * x0**2)

print(
    p9.ggplot(pd.DataFrame({"h": h, f"abs error at {x0}": error}))
    + p9.geom_line(p9.aes(x="h", y=f"abs error at {x0}"))
    + p9.scale_x_log10()
    + p9.scale_y_log10()
)