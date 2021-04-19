from py_log import get_logger

if __name__ == '__main__':
    ding_talk_token = 'xxxxxxxx'
    logger = get_logger('ding_talk_test', ding_talk_token=ding_talk_token, at_mobiles=('13798565670',),
                        show_code_line=True)
    logger.info('钉钉调试')
