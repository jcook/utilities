# CSTOOL

CSTOOL - CHECKING house ownership certificate STATUS TOOL

## Background

上海地区， 房产交易中心完成过户后， 等待出产证官方说法是20个自然工作日。
官方提供网络接口查询状态： [http://202.109.79.211:8002](http://202.109.79.211:8002)。

每次查询需要输入收件收据的12位编号，意味着也可以输入前后几个编号，看看别人的状态作为参考。这个过程需要人工多次输入收件收据编号。
对于心急的购房者而言，每天查看几次状态为常态。这个工具可以让我们做到一次输入，就可以查询多个结果。

## 使用

    cstool.py -i 201612345678 -f 10

  将查询编号 **201612345678** 之前的 **10** 个编号即：**201612345668** 到 **201612345678** 的状态。

## 交流

目前仅满足自己的正常使用，并没有很多容错。

发现BUG，贡献代码等，请联系维护者：<zengjie.cj@live.cn>

## TODO

TODO

## LICENSE

[MIT License](https://github.com/jcook/utilities/blob/master/LICENSE).
