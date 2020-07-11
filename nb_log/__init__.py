from nb_log import easy_log_config_default
from nb_log.monkey_print import nb_print
from nb_log.log_manager import LogManager, LoggerLevelSetterMixin, LoggerMixin, LoggerMixinDefaultWithFileHandler, get_logger, get_logger_with_filehanlder

simple_logger = LogManager('simple').get_logger_and_add_handlers()
defaul_logger = LogManager('defaul').get_logger_and_add_handlers(do_not_use_color_handler=True, formatter_template=7)
default_file_logger = LogManager('default_file_logger').get_logger_and_add_handlers(log_filename='default_file_logger.log')

logger_dingtalk_common = LogManager('钉钉通用报警提示').get_logger_and_add_handlers(
    ding_talk_token=easy_log_config_default.DING_TALK_TOKEN,
    log_filename='dingding_common.log')
