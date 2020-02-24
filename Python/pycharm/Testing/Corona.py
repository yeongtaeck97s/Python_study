# Installing collected packages: pystan, ephem, LunarCalendar, pymeeus, convertdate, holidays, setuptools-git, fbprophet
# conda install -c conda-forge fbprophet
# pip install plotly
# pip install ipython
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.offline as py
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, add_changepoints_to_plot
import matplotlib.pyplot as plt
import Corona_naver


# 하루에 한번만 실행.
# Corona_naver.naver_corona()

df_korea = pd.read_csv('korea_corona.csv')
df_prophet = df_korea.rename(columns={
    'date': 'ds',
    'confirmed': 'y'
})

m = Prophet(
    changepoint_prior_scale=0.2, # 증가시 유연
    changepoint_range=0.90, # 시계열의 첫 90%에 잠재적 변화점을 두다.
    yearly_seasonality=False,
    weekly_seasonality=False,
    daily_seasonality=True,
    seasonality_mode='additive'
)

m.fit(df_prophet)

future = m.make_future_dataframe(periods=7)
forecast = m.predict(future)

fig = m.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), m, forecast)
fig2 = plot_plotly(m, forecast, xlabel='일자', ylabel='감염자수(예상)')
#py.iplot(fig2, filename='corona19.html')
plotly.offline.plot(fig2, filename='corona19.html')
plt.show()
