import matplotlib.pyplot as plt, yfinance as yf
df = yf .download(['PBR','CL=F'])['Adj Close']
ratio = df['CL=F']/df['PBR']
ratio_r =ratio.resample('M').mean()
pbr_r = df['PBR'].resample('M').mean()
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(ratio_r, label='ADRs x Barril')
ax.legend(loc='upper left')
ax2=ax.twinx()
ax2.plot(pbr_r, lw=0.2, c='g', label='Precio PBR')
ax2.fill_between(pbr_r.index, pbr_r, color='g',alpha=0.1)
ax2.legend(loc='upper right')
fig.suptitle('WTI/PBR', fontsize=20, y=0.95)
plt. show()
