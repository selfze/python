from django.db import models

# Create your models here.

from django.db import models

# 主机表
class Hosttable(models.Model):
    ip = models.CharField(max_length=16, help_text='ip必须唯一', unique=True)
    hostname = models.CharField(max_length=32)

    use = (('web', 'web'), ('db', 'db'), ('cache', 'cache'))

    environment_science = (('testing_environment', '测试环境'),
                           ('production_environment', '生产环境'),
                           ('quasi_production_environment', '准生产环境'))
    edition = models.CharField(max_length=32)

    ssh_user = models.CharField(max_length=32)
    ssh_post = models.CharField(max_length=12)

    # 服务器状态
    state = (('on_line', '在线'),
             ('offline', '下线'),
             ('repair', '维修'))


# 用户表
class UserInfo(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=25)
    email = models.EmailField(max_length=32)
    roles = (('test', '测试'),
             ('development', '开发'),
             ('oam', '运维'))
    admin = (('yes', '是'),
             ('no', '否'))


# 命令表
class CommandList(models.Model):
    command = models.CharField(max_length=100)
    executor = models.CharField(max_length=16)  # 关联用户表
    result = (('success', '成功'),
              ('fail', '失败'))
    # host = models.CharField(max_length=32)  # 关联主机表，多对一
    host = models.ForeignKey(to="Hosttable")
    time = models.DateTimeField()


# 任务表
class PlanningTasks(models.Model):
    time = models.DateTimeField()
    job = models.CharField()  # 是否需要关联命令表？
    user = models.CharField(max_length=32)
    # creator = models.CharField(max_length=32)  # 关联用户表,多对一
    creator = models.ForeignKey(to="UserInfo")
    information = models.TextField(max_length=100)
    name = models.CharField()


# 初始化表
class InitializationTable(models.Model):
    # 脚本的位置
    scriptlocation = models.CharField(max_length=32)
    # 创建者
    creator = models.CharField(max_length=32)  # 关联用户表
    time = models.DateTimeField()
    name = models.CharField()  # 名字
    # 描述信息
    describe = models.TextField()


# 初始化日志表
class InitLog(models.Model):
    time = models.DateTimeField()
    # executor = models.CharField(max_length=32)  # 关联用户表,多对一
    executor = models.ForeignKey(to="UserInfo")
    # 执行的脚本
    executionscript = models.CharField()
    # 执行脚本的结果
    executionresult = (('success', '成功'),
                       ('fail', '失败'))


# 项目表
class ItmeSheet(models.Model):
    projectname = models.CharField()
    descride = models.TextField()
    # 创建时间
    creationtime = models.DateTimeField()
    host = models.CharField()  # 关联主机表
    projectlocation = models.CharField()
    gitpath = models.CharField()
    # 负责人
    # chargeperson = models.CharField(max_length=64)  # 关联用户表,多对一
    chargeperson = models.ForeignKey(to="UserInfo")
    dev = models.CharField()
    test = models.CharField()
    oam = models.CharField()
    nginx = models.CharField()


# 发布表
class PublishingTable(models.Model):
    publishingtime = models.DateTimeField()
    publishingperson = models.Model()  # 关联用户表
    project = models.CharField()
    state = (('in_release', '发布中'),
             ('waiting_release', '等待发布'),
             ('release_completed', '发布完成'),
             ('publishing_failure', '发布失败'),
             ('waiting-testing', '等待测试'),
             ('test_passed', '测试通过'),
             ('rollback', '回滚'))
    describe = models.TextField()
    edition = models.CharField()

