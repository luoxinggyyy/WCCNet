import pywt
import numpy as np
import pandas as pd
from plotnine import (
    ggplot,
    aes,
    geom_line,
    labs,
    arrow
)



data1 = np.loadtxt(r"C:\Users\UPC\Desktop\demo.txt")

wavelet = 'db4'
level = 2

df = pd.DataFrame({
    'col1': np.arange(len(data1)),
    'col2': data1
})


date = np.arange(0,len(data1)-1)
coeffs = pywt.wavedec(data1, wavelet, level=level)
ggplot(economics, aes(x='col1', y='col2')) + geom_line() 

    # line plot

reconstructed_signal = pywt.waverec(coeffs, wavelet)