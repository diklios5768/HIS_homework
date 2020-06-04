## 医院信息系统大作业
### 必备知识
* 你可能会疑惑为什么以下介绍的准备或者启动好多都是终端输入命令，因为在实际部署的时候，你是没有pycharm的，你没有任何的IDE可以使用。
* 本项目大部分主要是CURD的操作(我们也没空做其他额外的操作了)，会使用antd和bootstrap进行开发
    * [jquery](https://www.jquery123.com/)
    * [antd](https://ant.design/docs/react/introduce-cn)
    * [bootstrap](https://v4.bootcss.com/)
    * [flask](https://dormousehole.readthedocs.io/en/latest/)
### 项目准备
* 首先在python的主环境中需要安装`pipenv`包，`pip install pipenv`
    * 在终端当前项目文件夹输入`pipenv install`，因为有`Pipfile`文件，所以顺便会把需要的包也装上
        * 你可能会发现这次的虚拟环境并不在根目录，而是在用户文件夹下面的`.virtualenvs`文件夹中，这是因为`pipenv` 统一管理所有的虚拟环境
        * 如果你想只在本文件夹根目录下建立虚拟环境，可以在系统环境变量中添加`PIPENV_VENV_IN_PROJECT`
    * 需要手动设置解释器的路径，添加用户文件夹目录的`.virtualenvs`文件夹中对应的解释器即可
        * 你可能会发现add的时候pycharm自动帮你找到了，这是因为pycharm扫描到了pipfile中的内容
* 本项目自然也提供`requirements.txt`文件，供你用原生的`virtualenvironment`进行虚拟环境管理
    * 你可以先利用pycharm创建新的虚拟环境，随后在终端使用 `pip install -r requirements.txt` 命令
    * 当然我可能会更新慢了，导致没有对应的包，运行不了(这就是为什么不用`virtualenvironment`的原因之一)
* 在.env文件中，修改`DATABASE_URL`的内容，对应自己数据库的用户名密码和库名
### 项目启动
* 项目启动方法是在根目录下,终端输入`flask run`命令(注意终端前面应该是有括号，里面写着项目文件夹的名字，否则就是没激活虚拟环境，需要手动输入`flask shell`)