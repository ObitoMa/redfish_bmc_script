import getReadingVolts
import getwatt
import pandas as pd

# 循环生成BMC地址
login_hosts = []
for i in range(1, 32):
    host = f"https://10.254.2.{i}"
    login_hosts.append(host)

# print(login_hosts)

# BMC统一登陆账号密码
login_account = "USERID"
login_password = "ceni@123456"


# 获取电压&功率
for host in login_hosts:
    Volts = getReadingVolts.get_reading_volts(host, login_account, login_password)
    Volts_str = ', '.join(str(v) for v in Volts)
    Watt = getwatt.get_watt(host, login_account, login_password)
    data = []
    data.append([host] + Volts + [Watt])
    # print(headers)

    #df = pd.DataFrame(data, columns=['Host', 'Volts1', 'Volts2', 'Volts3', 'Volts4', 'Watt'])
    #df.to_excel('output.xlsx', index=False)
    
    print(f"{host}, {Volts_str}, {Watt}")

