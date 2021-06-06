from py_log import get_logger


def t_dingtalk():
    ding_talk_token = 'xxxxxxxx'
    logger = get_logger('ding_talk_test', ding_talk_token=ding_talk_token, at_mobiles=('13798565670',),
                        show_code_line=True, secret='SECwsaxerter')
    logger.info('钉钉调试')


def t_wechat():
    logger = get_logger('weichat_test', agentid='xxx', at_users='aa|bb', corpid='yyy', corpsecret='zzz')
    logger.info('钉钉调试')


if __name__ == '__main__':
    t_dingtalk()
    t_wechat()
