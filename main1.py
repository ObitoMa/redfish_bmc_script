import getReadingVolts
import getwatt
import getTmp
import pandas as pd

# 循环生成BMC地址
login_hosts = []
for i in range(1, 5):
    host = f"https://10.254.2.{i}"
    login_hosts.append(host)

# BMC统一登陆账号密码
login_account = "USERID"
login_password = "ceni@123456"

# 获取电压&功率
data = []
for host in login_hosts:
    Tmp = getTmp.get_temperatures(host, login_account, login_password)
    Volts = getReadingVolts.get_reading_volts(host, login_account, login_password)
    Volts_str = ', '.join(str(v) for v in Volts)
    Watt = getwatt.get_watt(host, login_account, login_password)
    data.append([host] + Tmp + Volts + [Watt])

df = pd.DataFrame(data, columns=['Host', 'Tmp1', 'Tmp2', 'Volts1', 'Volts2', 'Volts3', 'Volts4', 'Watt'])
df = df.set_index('Host')

# 将数据保存到Excel文件
df.to_excel('output.xlsx')

# 转置行和列
df_transposed = df.transpose()

# 将转置后的数据保存到新的Excel文件
df_transposed.to_excel('output_transposed.xlsx')