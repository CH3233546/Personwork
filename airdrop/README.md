# 手机电脑文件互传（类airdrop）

- 我们主要基于python的`HttpServer`实现
- 通过软件中嵌入Botton触发网页跳转实现


# 手机电脑共享剪切板（PC复制mobile粘贴 or PC复制mobile粘贴）

- 云剪切板可以跨设备共享数据，因此我们可以通过它来实现一个设备复制另一个设备粘贴

- 环境：PC（windows)/mobile(Andriod)

# 运行
## PC端
- 安装依赖库

```bash
pip install requests pyperclip
```

- clone库，终端打开项目所在路径，运行cloudcb.py

```bash
python cloudcb.py register <用户名> <密码>
```
- 输入自己的用户名密码——将用于移动端登录

### 设置快捷方式

#### ctrl+Alt+C——上传剪切板内容至云剪切板上

- 桌面右键-新建-快捷方式
- 添加路径

```bash
C:\Windows\System32\cmd.exe /c python (项目路径)\cloudcb.py copy <用户名> <密码>
```
- 下一步，完成

#### ctrl+Alt+P——加载云剪切板内容至本地剪切板上

- 桌面右键-新建-快捷方式
- 添加路径

```bash
C:\Windows\System32\cmd.exe /c python (项目路径)\cloudcb.py paste <用户名> <密码>
```
- 下一步，完成

### 运行HTTPServer


## 移动端
- 在ubuntu中生成apk后手机端下载使用即可
- 移动端和PC端需要在同一局域网下


