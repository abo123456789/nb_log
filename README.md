#### Function description
a simple logging tool(support file,email,dingtalk) ,mutil thread and process safe

#### Version description
* Supported version: Python 3.0+

#### Pip installation
```shell
pip install py-log
```

#### Demo
```python
    # log write file
    from py_log import LogManager
    logger = LogManager('test1').get_logger_and_add_handlers(log_filename='test1.log')
    logger.info('aaaa')
    logger.debug('bbbb')
    logger.warning('cccc')
    logger.error('dddd')
```

```python
    # log send dingding
    from py_log import LogManager
    ding_talk_token = 'xxxxxxxx'
    logger = LogManager('ding_talk_test').get_logger_and_add_handlers(ding_talk_token=ding_talk_token)
    logger.info('钉钉调试')
```

```python
    # log send email
    from py_log import LogManager
    from py_log.log_manager import MailHandlerConfig
    mail_config = MailHandlerConfig()
    mail_config.mailhost = ('smtp.sohu.com', 465)
    mail_config.fromaddr = 'aaa@sohu.com'
    mail_config.toaddrs = 'bbb@qq.com'
    mail_config.credentials = ('mail_username', 'mail_password')
    logger_mail = LogManager('log_mail_test').get_logger_and_add_handlers(mail_handler_config=mail_config,
                                                                          is_add_mail_handler=True)
    logger_mail.info('test send mail content')
```

