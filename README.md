# ColorLog
轻量级彩色log输出模块，需要的时候直接复制粘贴到自己项目中即可。

## usage

``` python
from log import logger

logger.debug("Hello!")
logger.info("233")
```

## config
颜色的配置均在`log.py`的起始部分。

日志格式中的`%(log_color)s`代表颜色的占位符，请勿删除。

可用颜色列表存放在`ColoredFormatter.COLOR_MAP`中。

默认配置已经可以满足大部分情况的需求。
