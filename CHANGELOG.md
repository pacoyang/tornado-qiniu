#Changelog

## 7.0.3 (2014-03-11)
### 增加
* 可以配置 io/rs/api/rsf host

## 7.0.2 (2014-12-24)
### 修正
* 内部http get当没有auth会出错
* python3下的qiniupy 没有参数时 arg parse会抛异常
* 增加callback policy

## 7.0.1 (2014-11-26)
### 增加
* setup.py从文件中读取版本号，而不是用导入方式
* 补充及修正了一些单元测试

## 7.0.0 (2014-11-13)

### 增加
* 简化上传接口
* 自动选择断点续上传还是直传
* 重构代码，接口和内部结构更清晰
* 同时支持python 2.x 和 3.x
* 支持pfop
* 支持verify callback
* 改变mime
* 代码覆盖度报告
* policy改为dict, 便于灵活增加，并加入过期字段检查
* 文件列表支持目录形式
