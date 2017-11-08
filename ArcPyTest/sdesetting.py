# -- coding: utf-8 --
import arcpy

# arcpy连接ArcSDE字符串 127.0.0.1.sde 为ArcCatlog中配置的连接信息
admin_sde = "Database Connections/127.0.0.1.sde"
# 使用空间数据库管理管sde设置是否允许普通用户连接企业级地理数据库
arcpy.AcceptConnections(admin_sde, False)
# 断开所有断开活动连接
arcpy.DisconnectUser(admin_sde, 'ALL')
# 地理数据库压缩程序参数设置
arcpy.Compress_management(admin_sde)

arcpy.ReconcileVersions_management(admin_sde, 'ALL_VERSIONS','sde.DEFAULT', with_post='POST')
# 使用空间数据库管理管sde设置是否允许普通用户连接企业级地理数据库
arcpy.AcceptConnections(admin_sde, True)
# 连接数据库并获取连接信息
users = arcpy.ListUsers(admin_sde)
for user in users:
    print(user)
    print("Username: {0}, Connected at: {1},Connected ID:{2}".format(
        user.Name, user.ConnectionTime,user.ID))
#读取数据库连接信息
sde=r'Database Connections/127.0.0.1.sde'
#连接数据库
sde_conn=arcpy.ArcSDESQLExecute(sde)
#要执行的sql
sql='''select {0},count({0}) from {1} GROUP BY {0}'''.format("OBJECTID","FEATURE_LINE")
#执行sql
result=sde_conn.execute(sql)
for item in result:
    print(item)

