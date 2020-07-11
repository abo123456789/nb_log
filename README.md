#### Function description
a simple logging tool(support file,email,dingtalk) ,mutil thread and process safe

#### Version description
* Supported version: Python 3.0+

#### Pip installation
```shell
pip install easy_log
```

#### Demo
```python
    from easy_log import LogManager

    logger = LogManager('test1').get_logger_and_add_handlers(log_filename='test1.log')
    logger.info('aaaa')
    logger.debug('bbbb')
    logger.warning('cccc')
    logger.error('dddd')
```