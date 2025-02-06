import pandas as pd
import matplotlib.pyplot as plt


methods_to_plot = ["Actual", "ARIMA", "SARIMA", "LSTM", "BiLSTM","SARLSTM"]
trend_topics = ['BNP\'s speech about election', 'Election polling by Awami league candidates', 'Some Awami league leaders out of election','Jatiya Party', 'Pakistan Campaign',
                'Refugee Detention in Bangladesh', 'BNP boycott election', 'BNP leaders condolation on injured people', 'Comilla City election',
                'Awami league\'s meeting or briefing about election',   'Police case filing against BNP leaders','Election monitor by foreign observers',
                'Parliament setup after election for AL', 'BNP leader\'s meeting', 'Khaleda Zia\'s treatment',    'BNP rally']

df = pd.read_csv("trend_forecasting_plot(Sheet1).csv")
df.columns = ["Method", "May", "June", "July", "August"]
df.set_index("Method", inplace=True)
df = df.apply(pd.to_numeric, errors='coerce')
# print(df)
xVal = ["May", "June", "July", "August"]
j = 0
print(len(df))
for i in range (0,len(df),6):

    batch = df.iloc[i:i+6]
    plt.figure(figsize=(8,5))

    yVal1 = batch.iloc[0].values
    yVal2 = batch.iloc[1].values
    yVal3 = batch.iloc[2].values
    yVal4 = batch.iloc[3].values
    yVal5 = batch.iloc[4].values
    yVal6 = batch.iloc[5].values

    plt.plot(xVal, yVal1, color = 'blue', linestyle='-',  label=methods_to_plot[0])
    plt.plot(xVal, yVal2, color='orange', linestyle='--', label=methods_to_plot[1])
    plt.plot(xVal, yVal3, color='green', linestyle=':', label=methods_to_plot[2])
    plt.plot(xVal, yVal4, color='red', linestyle='-.', label=methods_to_plot[3])
    plt.plot(xVal, yVal5, color='purple', linestyle='-', dashes=(5, 2, 1, 2), label=methods_to_plot[4])
    plt.plot(xVal, yVal6, color='cyan', linestyle='-', dashes=(3, 1, 5, 1), label=methods_to_plot[5])

    plt.title(f"{trend_topics[j]}", fontsize=14)
    plt.xlabel('Month', fontsize = 12)
    plt.ylabel('Value', fontsize = 12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    plt.legend(fontsize=12)

    plt.gca().set_facecolor('white')

    plt.grid(True, linestyle='--', color='gray', alpha=0.5)

    plt.savefig(f"{trend_topics[j]}.png", dpi = 300,bbox_inches='tight')
    plt.close()
    # plt.show()
    j = j+1


