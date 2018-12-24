from public.mysql import MysqlHandle
sql = MysqlHandle.get_xml_sql(xml_path='select_sql', xml_tag='select', xml_id='select_mobile_enable')
print(sql.format(mobile='xy9482e8393b6e98ff2d8c7e0080c599a320160926'))
tag = MysqlHandle.select_mysql_data()
print(tag)