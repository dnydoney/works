# 技术·文档 |Javascript基础概念
-----------------------------------------------------------------

## 闭包-什么是闭包



闭包是指在 JavaScript 中，内部函数总是可以访问其所在的外部函数中声明的参数和变量，即使在其外部函数被返回（寿命终结）了之后

闭包是一个集合（combination）；它由两部分组成：函数，以及**创建**该函数的环境。环境由闭包创建时在作用域中的任何局部变量组成。可以赋值给某个变量，可以作为参数传递给函数，也可以作为一个函数返回值返回。







```
// 三个处理函数
function start() {
    console.log('start');
}

function doing() {
    console.log('doing');
}

function end() {
    console.log('end');
}

// 外观函数，将一些处理统一起来，方便调用
function execute() {
    start();
    doing();
    end();
}


// 调用init开始执行
function init() {
    // 此处直接调用了高层函数，也可以选择越过它直接调用相关的函数
    execute();
}

init(); // start doing end
```
