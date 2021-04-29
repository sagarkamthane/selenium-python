import logging

def test_logger_demo():
    log = logging.getLogger(__name__)
    file = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file.setFormatter(formatter)
    log.addHandler(file)

    log.setLevel(logging.DEBUG) #used to set level, if level if info logs below info will be printed, by default it's set to warning
    #below order needs to be followed strictly
    # log.debug('debug statement')
    # log.info('information statement')
    # log.warning('warning')
    # log.error('error')
    # log.critical('critical error')



