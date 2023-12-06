import redfish
import json

def get_temperatures(login_host, login_account, login_password):
    # 创建Redfish客户端对象
    redfish_client = redfish.redfish_client(base_url=login_host,
                                            username=login_account,
                                            password=login_password,
                                            default_prefix='/redfish/v1/')

    # 登录到Redfish服务器
    redfish_client.login(auth="session")

    # 获取环境温度
    response = redfish_client.get("/redfish/v1/Chassis/1/Thermal#/Temperatures/0", None)

    # 将 RestResponse 对象转换成 JSON 字符串
    json_str = json.dumps(response.dict)

    data_dict = json.loads(json_str)
    #print(data_dict)
    temperature_list = data_dict["Temperatures"]

    # 提取环境温度值
    environment_temperatures = [item['ReadingCelsius'] for item in temperature_list]
    

    # 获取CPU温度
    # 获取CPU温度
    max_temperature = None

    for i in range(1, 3):  # 双路CPU，循环两次
        processor_url = f"/redfish/v1/Systems/1/Processors/{i}/ProcessorMetrics"
        response = redfish_client.get(processor_url, None)
        json_str = json.dumps(response.dict)
        data_dict = json.loads(json_str)
        #print(data_dict)
        temperature = data_dict['TemperatureCelsius']
        # print(temperature)
        if max_temperature is None or temperature > max_temperature:
            max_temperature = temperature
    # 退出Redfish客户端连接    
    redfish_client.logout()


    return environment_temperatures, max_temperature

