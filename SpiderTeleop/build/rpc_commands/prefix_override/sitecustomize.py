import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wshengggg/spiderPI/SpiderTeleop/install/rpc_commands'
