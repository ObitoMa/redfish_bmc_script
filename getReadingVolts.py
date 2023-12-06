import redfish
import json

def get_reading_volts(login_host, login_account, login_password):
    REDFISH_OBJ = redfish.redfish_client(base_url=login_host, username=login_account, password=login_password, default_prefix='/redfish/v1/')
    REDFISH_OBJ.login(auth="session")
    response = REDFISH_OBJ.get("/redfish/v1/Chassis/1/Power#/PowerControl/0", None)

    # 将 RestResponse 对象转换成 JSON 字符串
    json_str = json.dumps(response.dict)

    data_dict = json.loads(json_str)
    data_list = data_dict["Voltages"]

    reading_volts = [item["ReadingVolts"] for item in data_list if "ReadingVolts" in item]

    # 退出登录
    REDFISH_OBJ.logout()

    return reading_volts