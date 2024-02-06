# flask-swagger-example

## Getting started

### 本机开发环境启动
```
Windows 运行 app.py 即可

Linux
cd [path] # 进入项目目录
python3 -m flask run -h 0.0.0.0
```

### 部署 uwsgi 服务 仅Linux系统
uwsgi 不会运行 app.py `if __name__ == "__main__":` 里面的程序代码
```shell
# 启动
uwsgi --ini start.ini
# 修改代码提交后重新加载代码重启
## /var/run/uwsgi.pid 为 start.ini 配置好的pid主进程存放位置
uwsgi --reload /var/run/uwsgi.pid
# 停止
uwsgi --stop /var/run/uwsgi.pid
```