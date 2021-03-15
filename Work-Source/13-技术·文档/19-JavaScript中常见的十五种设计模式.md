# 技术·文档 | JavaScript十五种设计模式
-----------------------------------------------------------------
在程序设计中有很多实用的设计模式，而其中大部分语言的实现都是基于“类”。

在JavaScript中并没有类这种概念，JS中的函数属于一等对象，在JS中定义一个对象非常简单（var obj = {}），而基于JS中闭包与弱类型等特性，在实现一些设计模式的方式上与众不同。

设计原则
单一职责原则（SRP）

一个对象或方法只做一件事情。如果一个方法承担了过多的职责，那么在需求的变迁过程中，需要改写这个方法的可能性就越大。

应该把对象或方法划分成较小的粒度

最少知识原则（LKP）

一个软件实体应当 尽可能少地与其他实体发生相互作用 

应当尽量减少对象之间的交互。如果两个对象之间不必彼此直接通信，那么这两个对象就不要发生直接的 相互联系，可以转交给第三方进行处理

开放-封闭原则（OCP）

软件实体（类、模块、函数）等应该是可以 扩展的，但是不可修改

当需要改变一个程序的功能或者给这个程序增加新功能的时候，可以使用增加代码的方式，尽量避免改动程序的源代码，防止影响原系统的稳定

 

 什么是设计模式
 学习设计模式，有助于写出可复用和可维护性高的程序

设计模式的原则是“找出 程序中变化的地方，并将变化封装起来”，它的关键是意图，而不是结构。

不过要注意，使用不当的话，可能会事倍功半。



一、单例模式
1. 定义

保证一个类仅有一个实例，并提供一个访问它的全局访问点

2. 核心

确保只有一个实例，并提供全局访问

3. 实现

假设要设置一个管理员，多次调用也仅设置一次，我们可以使用闭包缓存一个内部变量来实现这个单例

```
function SetManager(name) {
    this.manager = name;
}


SetManager.prototype.getName = function() {
    console.log(this.manager);
};

var SingletonSetManager = (function() {
    var manager = null;

    return function(name) {
        if (!manager) {
            manager = new SetManager(name);
        }
    
        return manager;
    } 
})();

SingletonSetManager('a').getName(); // a
SingletonSetManager('b').getName(); // a
SingletonSetManager('c').getName(); // a

```

这是比较简单的做法，但是假如我们还要设置一个HR呢？就得复制一遍代码了

所以，可以改写单例内部，实现地更通用一些

```
// 提取出通用的单例
function getSingleton(fn) {
    var instance = null;

    return function() {
        if (!instance) {
            instance = fn.apply(this, arguments);
        }
    
        return instance;
    }
}

```
再进行调用，结果还是一样

```
// 获取单例
var managerSingleton = getSingleton(function(name) {
    var manager = new SetManager(name);
    return manager;
});

managerSingleton('a').getName(); // a
managerSingleton('b').getName(); // a
managerSingleton('c').getName(); // a
```
这时，我们添加HR时，就不需要更改获取单例内部的实现了，仅需要实现添加HR所需要做的，再调用即可

```
function SetHr(name) {
    this.hr = name;
}

SetHr.prototype.getName = function() {
    console.log(this.hr);
};

var hrSingleton = getSingleton(function(name) {
    var hr = new SetHr(name);
    return hr;
});

hrSingleton('aa').getName(); // aa
hrSingleton('bb').getName(); // aa
hrSingleton('cc').getName(); // aa
```
或者，仅想要创建一个div层，不需要将对象实例化，直接调用函数

结果为页面中仅有第一个创建的div

```
function createPopup(html) {
    var div = document.createElement('div');
    div.innerHTML = html;
    document.body.append(div);

    return div;
}

var popupSingleton = getSingleton(function() {
    var div = createPopup.apply(this, arguments);
    return div;
});

console.log(
    popupSingleton('aaa').innerHTML,
    popupSingleton('bbb').innerHTML,
    popupSingleton('bbb').innerHTML
); // aaa  aaa  aaa
```


二、策略模式
1. 定义

定义一系列的算法，把它们一个个封装起来，并且使它们可以相互替换。

2. 核心

将算法的使用和算法的实现分离开来。

一个基于策略模式的程序至少由两部分组成：

第一个部分是一组策略类，策略类封装了具体的算法，并负责具体的计算过程。

第二个部分是环境类Context，Context接受客户的请求，随后把请求委托给某一个策略类。要做到这点，说明Context 中要维持对某个策略对象的引用

3. 实现

策略模式可以用于组合一系列算法，也可用于组合一系列业务规则

假设需要通过成绩等级来计算学生的最终得分，每个成绩等级有对应的加权值。我们可以利用对象字面量的形式直接定义这个组策略

```
// 加权映射关系
var levelMap = {
    S: 10,
    A: 8,
    B: 6,
    C: 4
};

// 组策略
var scoreLevel = {
    basicScore: 80,

    S: function() {
        return this.basicScore + levelMap['S']; 
    },
    
    A: function() {
        return this.basicScore + levelMap['A']; 
    },
    
    B: function() {
        return this.basicScore + levelMap['B']; 
    },
    
    C: function() {
        return this.basicScore + levelMap['C']; 
    }
}

// 调用
function getScore(level) {
    return scoreLevel[level] ? scoreLevel[level]() : 0;
}

console.log(
    getScore('S'),
    getScore('A'),
    getScore('B'),
    getScore('C'),
    getScore('D')
); // 90 88 86 84 0
```
在组合业务规则方面，比较经典的是表单的验证方法。这里列出比较关键的部分

```
// 错误提示
var errorMsgs = {
    default: '输入数据格式不正确',
    minLength: '输入数据长度不足',
    isNumber: '请输入数字',
    required: '内容不为空'
};

// 规则集
var rules = {
    minLength: function(value, length, errorMsg) {
        if (value.length < length) {
            return errorMsg || errorMsgs['minLength']
        }
    },
    isNumber: function(value, errorMsg) {
        if (!/\d+/.test(value)) {
            return errorMsg || errorMsgs['isNumber'];
        }
    },
    required: function(value, errorMsg) {
        if (value === '') {
            return errorMsg || errorMsgs['required'];
        }
    }
};

// 校验器
function Validator() {
    this.items = [];
};

Validator.prototype = {
    constructor: Validator,
    
    // 添加校验规则
    add: function(value, rule, errorMsg) {
        var arg = [value];
    
        if (rule.indexOf('minLength') !== -1) {
            var temp = rule.split(':');
            arg.push(temp[1]);
            rule = temp[0];
        }
    
        arg.push(errorMsg);
    
        this.items.push(function() {
            // 进行校验
            return rules[rule].apply(this, arg);
        });
    },
    
    // 开始校验
    start: function() {
        for (var i = 0; i < this.items.length; ++i) {
            var ret = this.items[i]();
            
            if (ret) {
                console.log(ret);
                // return ret;
            }
        }
    }
};

// 测试数据
function testTel(val) {
    return val;
}

var validate = new Validator();

validate.add(testTel('ccc'), 'isNumber', '只能为数字'); // 只能为数字
validate.add(testTel(''), 'required'); // 内容不为空
validate.add(testTel('123'), 'minLength:5', '最少5位'); // 最少5位
validate.add(testTel('12345'), 'minLength:5', '最少5位');

var ret = validate.start();

console.log(ret);
```
4. 优缺点

优点

可以有效地避免多重条件语句，将一系列方法封装起来也更直观，利于维护

缺点

往往策略集会比较多，我们需要事先就了解定义好所有的情况

 

三、代理模式
1. 定义

为一个对象提供一个代用品或占位符，以便控制对它的访问

2. 核心

当客户不方便直接访问一个 对象或者不满足需要的时候，提供一个替身对象 来控制对这个对象的访问，客户实际上访问的是 替身对象。

替身对象对请求做出一些处理之后， 再把请求转交给本体对象

代理和本体的接口具有一致性，本体定义了关键功能，而代理是提供或拒绝对它的访问，或者在访问本体之前做一 些额外的事情

3. 实现

代理模式主要有三种：保护代理、虚拟代理、缓存代理

保护代理主要实现了访问主体的限制行为，以过滤字符作为简单的例子

```
// 主体，发送消息
function sendMsg(msg) {
    console.log(msg);
}

// 代理，对消息进行过滤
function proxySendMsg(msg) {
    // 无消息则直接返回
    if (typeof msg === 'undefined') {
        console.log('deny');
        return;
    }
    
    // 有消息则进行过滤
    msg = ('' + msg).replace(/泥\s*煤/g, '');
    
    sendMsg(msg);
}


sendMsg('泥煤呀泥 煤呀'); // 泥煤呀泥 煤呀
proxySendMsg('泥煤呀泥 煤'); // 呀
proxySendMsg(); // deny
```
它的意图很明显，在访问主体之前进行控制，没有消息的时候直接在代理中返回了，拒绝访问主体，这数据保护代理的形式

有消息的时候对敏感字符进行了处理，这属于虚拟代理的模式

 

虚拟代理在控制对主体的访问时，加入了一些额外的操作

在滚动事件触发的时候，也许不需要频繁触发，我们可以引入函数节流，这是一种虚拟代理的实现

```
// 函数防抖，频繁操作中不处理，直到操作完成之后（再过 delay 的时间）才一次性处理
function debounce(fn, delay) {
    delay = delay || 200;
    
    var timer = null;
    
    return function() {
        var arg = arguments;
          
        // 每次操作时，清除上次的定时器
        clearTimeout(timer);
        timer = null;
        
        // 定义新的定时器，一段时间后进行操作
        timer = setTimeout(function() {
            fn.apply(this, arg);
        }, delay);
    }
};

var count = 0;

// 主体
function scrollHandle(e) {
    console.log(e.type, ++count); // scroll
}

// 代理
var proxyScrollHandle = (function() {
    return debounce(scrollHandle, 500);
})();

window.onscroll = proxyScrollHandle;
```


缓存代理可以为一些开销大的运算结果提供暂时的缓存，提升效率

来个栗子，缓存加法操作

```
// 主体
function add() {
    var arg = [].slice.call(arguments);

    return arg.reduce(function(a, b) {
        return a + b;
    });
}

// 代理
var proxyAdd = (function() {
    var cache = [];

    return function() {
        var arg = [].slice.call(arguments).join(',');
        
        // 如果有，则直接从缓存返回
        if (cache[arg]) {
            return cache[arg];
        } else {
            var ret = add.apply(this, arguments);
            return ret;
        }
    };
})();

console.log(
    add(1, 2, 3, 4),
    add(1, 2, 3, 4),

    proxyAdd(10, 20, 30, 40),
    proxyAdd(10, 20, 30, 40)
); // 10 10 100 100
```


四、迭代器模式
1. 定义

迭代器模式是指提供一种方法顺序访问一个聚合对象中的各个元素，而又不需要暴露该对象的内部表示。

2. 核心

在使用迭代器模式之后，即使不关心对象的内部构造，也可以按顺序访问其中的每个元素

3. 实现

JS中数组的map forEach 已经内置了迭代器

[1, 2, 3].forEach(function(item, index, arr) {
    console.log(item, index, arr);
});
不过对于对象的遍历，往往不能与数组一样使用同一的遍历代码

我们可以封装一下

```
function each(obj, cb) {
    var value;

    if (Array.isArray(obj)) {
        for (var i = 0; i < obj.length; ++i) {
            value = cb.call(obj[i], i, obj[i]);
    
            if (value === false) {
                break;
            }
        }
    } else {
        for (var i in obj) {
            value = cb.call(obj[i], i, obj[i]);
    
            if (value === false) {
                break;
            }
        }
    }
}

each([1, 2, 3], function(index, value) {
    console.log(index, value);
});

each({a: 1, b: 2}, function(index, value) {
    console.log(index, value);
});

// 0 1
// 1 2
// 2 3

// a 1
// b 2
```
再来看一个例子，强行地使用迭代器，来了解一下迭代器也可以替换频繁的条件语句

虽然例子不太好，但在其他负责的分支判断情况下，也是值得考虑的

```
function getManager() {
    var year = new Date().getFullYear();

    if (year <= 2000) {
        console.log('A');
    } else if (year >= 2100) {
        console.log('C');
    } else {
        console.log('B');
    }
}

getManager(); // B
```
将每个条件语句拆分出逻辑函数，放入迭代器中迭代

```
function year2000() {
    var year = new Date().getFullYear();

    if (year <= 2000) {
        console.log('A');
    }
    
    return false;
}

function year2100() {
    var year = new Date().getFullYear();

    if (year >= 2100) {
        console.log('C');
    }
    
    return false;
}

function year() {
    var year = new Date().getFullYear();

    if (year > 2000 && year < 2100) {
        console.log('B');
    }
    
    return false;
}

function iteratorYear() {
    for (var i = 0; i < arguments.length; ++i) {
        var ret = arguments[i]();

        if (ret !== false) {
            return ret;
        }
    }
}

var manager = iteratorYear(year2000, year2100, year); // B
```


五、发布-订阅模式
1. 定义

也称作观察者模式，定义了对象间的一种一对多的依赖关系，当一个对象的状态发 生改变时，所有依赖于它的对象都将得到通知

2. 核心

取代对象之间硬编码的通知机制，一个对象不用再显式地调用另外一个对象的某个接口。

与传统的发布-订阅模式实现方式（将订阅者自身当成引用传入发布者）不同，在JS中通常使用注册回调函数的形式来订阅

3. 实现

JS中的事件就是经典的发布-订阅模式的实现

```
// 订阅
document.body.addEventListener('click', function() {
    console.log('click1');
}, false);

document.body.addEventListener('click', function() {
    console.log('click2');
}, false);

// 发布
document.body.click(); // click1  click2
```
自己实现一下

小A在公司C完成了笔试及面试，小B也在公司C完成了笔试。他们焦急地等待结果，每隔半天就电话询问公司C，导致公司C很不耐烦。

一种解决办法是 AB直接把联系方式留给C，有结果的话C自然会通知AB

这里的“询问”属于显示调用，“留给”属于订阅，“通知”属于发布

```
// 观察者
var observer = {
    // 订阅集合
    subscribes: [],

    // 订阅
    subscribe: function(type, fn) {
        if (!this.subscribes[type]) {
            this.subscribes[type] = [];
        }
        
        // 收集订阅者的处理
        typeof fn === 'function' && this.subscribes[type].push(fn);
    },
    
    // 发布  可能会携带一些信息发布出去
    publish: function() {
        var type = [].shift.call(arguments),
            fns = this.subscribes[type];
        
        // 不存在的订阅类型，以及订阅时未传入处理回调的
        if (!fns || !fns.length) {
            return;
        }
        
        // 挨个处理调用
        for (var i = 0; i < fns.length; ++i) {
            fns[i].apply(this, arguments);
        }
    },
    
    // 删除订阅
    remove: function(type, fn) {
        // 删除全部
        if (typeof type === 'undefined') {
            this.subscribes = [];
            return;
        }
    
        var fns = this.subscribes[type];
    
        // 不存在的订阅类型，以及订阅时未传入处理回调的
        if (!fns || !fns.length) {
            return;
        }
    
        if (typeof fn === 'undefined') {
            fns.length = 0;
            return;
        }
    
        // 挨个处理删除
        for (var i = 0; i < fns.length; ++i) {
            if (fns[i] === fn) {
                fns.splice(i, 1);
            }
        }
    }
};

// 订阅岗位列表
function jobListForA(jobs) {
    console.log('A', jobs);
}

function jobListForB(jobs) {
    console.log('B', jobs);
}

// A订阅了笔试成绩
observer.subscribe('job', jobListForA);
// B订阅了笔试成绩
observer.subscribe('job', jobListForB);


// A订阅了笔试成绩
observer.subscribe('examinationA', function(score) {
    console.log(score);
});

// B订阅了笔试成绩
observer.subscribe('examinationB', function(score) {
    console.log(score);
});

// A订阅了面试结果
observer.subscribe('interviewA', function(result) {
    console.log(result);
});

observer.publish('examinationA', 100); // 100
observer.publish('examinationB', 80); // 80
observer.publish('interviewA', '备用'); // 备用

observer.publish('job', ['前端', '后端', '测试']); // 输出A和B的岗位


// B取消订阅了笔试成绩
observer.remove('examinationB');
// A都取消订阅了岗位
observer.remove('job', jobListForA);

observer.publish('examinationB', 80); // 没有可匹配的订阅，无输出
observer.publish('job', ['前端', '后端', '测试']); // 输出B的岗位
```
4. 优缺点

优点

一为时间上的解耦，二为对象之间的解耦。可以用在异步编程中与MV*框架中

缺点

创建订阅者本身要消耗一定的时间和内存，订阅的处理函数不一定会被执行，驻留内存有性能开销

弱化了对象之间的联系，复杂的情况下可能会导致程序难以跟踪维护和理解

 

六、命令模式
1. 定义

用一种松耦合的方式来设计程序，使得请求发送者和请求接收者能够消除彼此之间的耦合关系

命令（command）指的是一个执行某些特定事情的指令

2. 核心

命令中带有execute执行、undo撤销、redo重做等相关命令方法，建议显示地指示这些方法名

3. 实现

简单的命令模式实现可以直接使用对象字面量的形式定义一个命令

var incrementCommand = {
    execute: function() {
        // something
    }
};
不过接下来的例子是一个自增命令，提供执行、撤销、重做功能

采用对象创建处理的方式，定义这个自增

```
// 自增
function IncrementCommand() {
    // 当前值
    this.val = 0;
    // 命令栈
    this.stack = [];
    // 栈指针位置
    this.stackPosition = -1;
};

IncrementCommand.prototype = {
    constructor: IncrementCommand,

    // 执行
    execute: function() {
        this._clearRedo();
        
        // 定义执行的处理
        var command = function() {
            this.val += 2;
        }.bind(this);
        
        // 执行并缓存起来
        command();
        
        this.stack.push(command);
    
        this.stackPosition++;
    
        this.getValue();
    },
    
    canUndo: function() {
        return this.stackPosition >= 0;
    },
    
    canRedo: function() {
        return this.stackPosition < this.stack.length - 1;
    },
    
    // 撤销
    undo: function() {
        if (!this.canUndo()) {
            return;
        }
        
        this.stackPosition--;
    
        // 命令的撤销，与执行的处理相反
        var command = function() {
            this.val -= 2;
        }.bind(this);
        
        // 撤销后不需要缓存
        command();
    
        this.getValue();
    },
    
    // 重做
    redo: function() {
        if (!this.canRedo()) {
            return;
        }
        
        // 执行栈顶的命令
        this.stack[++this.stackPosition]();
    
        this.getValue();
    },
    
    // 在执行时，已经撤销的部分不能再重做
    _clearRedo: function() {
        this.stack = this.stack.slice(0, this.stackPosition + 1);
    },
    
    // 获取当前值
    getValue: function() {
        console.log(this.val);
    }
};
```
再实例化进行测试，模拟执行、撤销、重做的操作

```
var incrementCommand = new IncrementCommand();

// 模拟事件触发，执行命令
var eventTrigger = {
    // 某个事件的处理中，直接调用命令的处理方法
    increment: function() {
        incrementCommand.execute();
    },

    incrementUndo: function() {
        incrementCommand.undo();
    },
    
    incrementRedo: function() {
        incrementCommand.redo();
    }
};


eventTrigger['increment'](); // 2
eventTrigger['increment'](); // 4

eventTrigger['incrementUndo'](); // 2

eventTrigger['increment'](); // 4

eventTrigger['incrementUndo'](); // 2
eventTrigger['incrementUndo'](); // 0
eventTrigger['incrementUndo'](); // 无输出

eventTrigger['incrementRedo'](); // 2
eventTrigger['incrementRedo'](); // 4
eventTrigger['incrementRedo'](); // 无输出

eventTrigger['increment'](); // 6
```


此外，还可以实现简单的宏命令（一系列命令的集合）

```
var MacroCommand = {
    commands: [],

    add: function(command) {
        this.commands.push(command);
    
        return this;
    },
    
    remove: function(command) {
        if (!command) {
            this.commands = [];
            return;
        }
    
        for (var i = 0; i < this.commands.length; ++i) {
            if (this.commands[i] === command) {
                this.commands.splice(i, 1);
            }
        }
    },
    
    execute: function() {
        for (var i = 0; i < this.commands.length; ++i) {
            this.commands[i].execute();
        }
    }
};

var showTime = {
    execute: function() {
        console.log('time');
    }
};

var showName = {
    execute: function() {
        console.log('name');
    }
};

var showAge = {
    execute: function() {
        console.log('age');
    }
};

MacroCommand.add(showTime).add(showName).add(showAge);

MacroCommand.remove(showName);

MacroCommand.execute(); // time age
```


七、组合模式
1. 定义

是用小的子对象来构建更大的 对象，而这些小的子对象本身也许是由更小 的“孙对象”构成的。

2. 核心

可以用树形结构来表示这种“部分- 整体”的层次结构。

调用组合对象 的execute方法，程序会递归调用组合对象 下面的叶对象的execute方法



但要注意的是，组合模式不是父子关系，它是一种HAS-A（聚合）的关系，将请求委托给 它所包含的所有叶对象。基于这种委托，就需要保证组合对象和叶对象拥有相同的 接口

此外，也要保证用一致的方式对待 列表中的每个叶对象，即叶对象属于同一类，不需要过多特殊的额外操作

3. 实现

使用组合模式来实现扫描文件夹中的文件

```
// 文件夹 组合对象
function Folder(name) {
    this.name = name;
    this.parent = null;
    this.files = [];
}

Folder.prototype = {
    constructor: Folder,

    add: function(file) {
        file.parent = this;
        this.files.push(file);
    
        return this;
    },
    
    scan: function() {
        // 委托给叶对象处理
        for (var i = 0; i < this.files.length; ++i) {
            this.files[i].scan();
        }
    },
    
    remove: function(file) {
        if (typeof file === 'undefined') {
            this.files = [];
            return;
        }
    
        for (var i = 0; i < this.files.length; ++i) {
            if (this.files[i] === file) {
                this.files.splice(i, 1);
            }
        }
    }
};

// 文件 叶对象
function File(name) {
    this.name = name;
    this.parent = null;
}

File.prototype = {
    constructor: File,

    add: function() {
        console.log('文件里面不能添加文件');
    },
    
    scan: function() {
        var name = [this.name];
        var parent = this.parent;
    
        while (parent) {
            name.unshift(parent.name);
            parent = parent.parent;
        }
    
        console.log(name.join(' / '));
    }
};
```
构造好组合对象与叶对象的关系后，实例化，在组合对象中插入组合或叶对象

```
var web = new Folder('Web');
var fe = new Folder('前端');
var css = new Folder('CSS');
var js = new Folder('js');
var rd = new Folder('后端');

web.add(fe).add(rd);

var file1 = new File('HTML权威指南.pdf');
var file2 = new File('CSS权威指南.pdf');
var file3 = new File('JavaScript权威指南.pdf');
var file4 = new File('MySQL基础.pdf');
var file5 = new File('Web安全.pdf');
var file6 = new File('Linux菜鸟.pdf');

css.add(file2);
fe.add(file1).add(file3).add(css).add(js);
rd.add(file4).add(file5);
web.add(file6);

rd.remove(file4);

// 扫描
web.scan();
```
扫描结果为



 

 4. 优缺点

优点

可 以方便地构造一棵树来表示对象的部分-整体 结构。在树的构造最终 完成之后，只需要通过请求树的最顶层对 象，便能对整棵树做统一一致的操作。

缺点

创建出来的对象长得都差不多，可能会使代码不好理解，创建太多的对象对性能也会有一些影响

 

八、模板方法模式
1. 定义

模板方法模式由两部分结构组成，第一部分是抽象父类，第二部分是具体的实现子类。

2. 核心

在抽象父类中封装子类的算法框架，它的 init方法可作为一个算法的模板，指导子类以何种顺序去执行哪些方法。

由父类分离出公共部分，要求子类重写某些父类的（易变化的）抽象方法

3. 实现

模板方法模式一般的实现方式为继承

以运动作为例子，运动有比较通用的一些处理，这部分可以抽离开来，在父类中实现。具体某项运动的特殊性则有自类来重写实现。

最终子类直接调用父类的模板函数来执行

```
// 体育运动
function Sport() {

}

Sport.prototype = {
    constructor: Sport,
    
    // 模板，按顺序执行
    init: function() {
        this.stretch();
        this.jog();
        this.deepBreath();
        this.start();
    
        var free = this.end();
        
        // 运动后还有空的话，就拉伸一下
        if (free !== false) {
            this.stretch();
        }
        
    },
    
    // 拉伸
    stretch: function() {
        console.log('拉伸');
    },
    
    // 慢跑
    jog: function() {
        console.log('慢跑');
    },
    
    // 深呼吸
    deepBreath: function() {
        console.log('深呼吸');
    },
    
    // 开始运动
    start: function() {
        throw new Error('子类必须重写此方法');
    },
    
    // 结束运动
    end: function() {
        console.log('运动结束');
    }
};

// 篮球
function Basketball() {

}

Basketball.prototype = new Sport();

// 重写相关的方法
Basketball.prototype.start = function() {
    console.log('先投上几个三分');
};

Basketball.prototype.end = function() {
    console.log('运动结束了，有事先走一步');
    return false;
};


// 马拉松
function Marathon() {

}

Marathon.prototype = new Sport();

var basketball = new Basketball();
var marathon = new Marathon();

// 子类调用，最终会按照父类定义的顺序执行
basketball.init();
marathon.init();
```




九、享元模式
1. 定义

享元（flyweight）模式是一种用于性能优化的模式，它的目标是尽量减少共享对象的数量
2. 核心

运用共享技术来有效支持大量细粒度的对象。

强调将对象的属性划分为内部状态（属性）与外部状态（属性）。内部状态用于对象的共享，通常不变；而外部状态则剥离开来，由具体的场景决定。

3. 实现

在程序中使用了大量的相似对象时，可以利用享元模式来优化，减少对象的数量

举个栗子，要对某个班进行身体素质测量，仅测量身高体重来评判

```
// 健康测量
function Fitness(name, sex, age, height, weight) {
    this.name = name;
    this.sex = sex;
    this.age = age;
    this.height = height;
    this.weight = weight;
}

// 开始评判
Fitness.prototype.judge = function() {
    var ret = this.name + ': ';

    if (this.sex === 'male') {
        ret += this.judgeMale();
    } else {
        ret += this.judgeFemale();
    }
    
    console.log(ret);
};

// 男性评判规则
Fitness.prototype.judgeMale = function() {
    var ratio = this.height / this.weight;

    return this.age > 20 ? (ratio > 3.5) : (ratio > 2.8);
};

// 女性评判规则
Fitness.prototype.judgeFemale = function() {
    var ratio = this.height / this.weight;
    
    return this.age > 20 ? (ratio > 4) : (ratio > 3);
};


var a = new Fitness('A', 'male', 18, 160, 80);
var b = new Fitness('B', 'male', 21, 180, 70);
var c = new Fitness('C', 'female', 28, 160, 80);
var d = new Fitness('D', 'male', 18, 170, 60);
var e = new Fitness('E', 'female', 18, 160, 40);

// 开始评判
a.judge(); // A: false
b.judge(); // B: false
c.judge(); // C: false
d.judge(); // D: true
e.judge(); // E: true
```
评判五个人就需要创建五个对象，一个班就几十个对象

可以将对象的公共部分（内部状态）抽离出来，与外部状态独立。将性别看做内部状态即可，其他属性都属于外部状态。

这么一来我们只需要维护男和女两个对象（使用factory对象），而其他变化的部分则在外部维护（使用manager对象）

```
// 健康测量
function Fitness(sex) {
    this.sex = sex;
}

// 工厂，创建可共享的对象
var FitnessFactory = {
    objs: [],

    create: function(sex) {
        if (!this.objs[sex]) {
            this.objs[sex] = new Fitness(sex);
        }
    
        return this.objs[sex];
    }
};

// 管理器，管理非共享的部分
var FitnessManager = {
    fitnessData: {},
    
    // 添加一项
    add: function(name, sex, age, height, weight) {
        var fitness = FitnessFactory.create(sex);
        
        // 存储变化的数据
        this.fitnessData[name] = {
            age: age,
            height: height,
            weight: weight
        };
    
        return fitness;
    },
    
    // 从存储的数据中获取，更新至当前正在使用的对象
    updateFitnessData: function(name, obj) {
        var fitnessData = this.fitnessData[name];
    
        for (var item in fitnessData) {
            if (fitnessData.hasOwnProperty(item)) {
                obj[item] = fitnessData[item];
            }
        }
    }
};

// 开始评判
Fitness.prototype.judge = function(name) {
    // 操作前先更新当前状态（从外部状态管理器中获取）
    FitnessManager.updateFitnessData(name, this);

    var ret = name + ': ';
    
    if (this.sex === 'male') {
        ret += this.judgeMale();
    } else {
        ret += this.judgeFemale();
    }
    
    console.log(ret);
};

// 男性评判规则
Fitness.prototype.judgeMale = function() {
    var ratio = this.height / this.weight;

    return this.age > 20 ? (ratio > 3.5) : (ratio > 2.8);
};

// 女性评判规则
Fitness.prototype.judgeFemale = function() {
    var ratio = this.height / this.weight;
    
    return this.age > 20 ? (ratio > 4) : (ratio > 3);
};


var a = FitnessManager.add('A', 'male', 18, 160, 80);
var b = FitnessManager.add('B', 'male', 21, 180, 70);
var c = FitnessManager.add('C', 'female', 28, 160, 80);
var d = FitnessManager.add('D', 'male', 18, 170, 60);
var e = FitnessManager.add('E', 'female', 18, 160, 40);

// 开始评判
a.judge('A'); // A: false
b.judge('B'); // B: false
c.judge('C'); // C: false
d.judge('D'); // D: true
e.judge('E'); // E: true
```
不过代码可能更复杂了，这个例子可能还不够充分，只是展示了享元模式如何实现，它节省了多个相似的对象，但多了一些操作。

factory对象有点像单例模式，只是多了一个sex的参数，如果没有内部状态，则没有参数的factory对象就更接近单例模式了

 

十、职责链模式
1. 定义

使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系，将这些对象连成一条链，并沿着这条链 传递该请求，直到有一个对象处理它为止
2. 核心

请求发送者只需要知道链中的第一个节点，弱化发送者和一组接收者之间的强联系，可以便捷地在职责链中增加或删除一个节点，同样地，指定谁是第一个节点也很便捷

3. 实现

以展示不同类型的变量为例，设置一条职责链，可以免去多重if条件分支

```
// 定义链的某一项
function ChainItem(fn) {
    this.fn = fn;
    this.next = null;
}

ChainItem.prototype = {
    constructor: ChainItem,
    
    // 设置下一项
    setNext: function(next) {
        this.next = next;
        return next;
    },
    
    // 开始执行
    start: function() {
        this.fn.apply(this, arguments);
    },
    
    // 转到链的下一项执行
    toNext: function() {
        if (this.next) {
            this.start.apply(this.next, arguments);
        } else {
            console.log('无匹配的执行项目');
        }
    }
};

// 展示数字
function showNumber(num) {
    if (typeof num === 'number') {
        console.log('number', num);
    } else {
        // 转移到下一项
        this.toNext(num);
    }
}

// 展示字符串
function showString(str) {
    if (typeof str === 'string') {
        console.log('string', str);
    } else {
        this.toNext(str);
    }
}

// 展示对象
function showObject(obj) {
    if (typeof obj === 'object') {
        console.log('object', obj);
    } else {
        this.toNext(obj);
    }
}

var chainNumber = new ChainItem(showNumber);
var chainString = new ChainItem(showString);
var chainObject = new ChainItem(showObject);

// 设置链条
chainObject.setNext(chainNumber).setNext(chainString);

chainString.start('12'); // string 12
chainNumber.start({}); // 无匹配的执行项目
chainObject.start({}); // object {}
chainObject.start(123); // number 123
```
这时想判断未定义的时候呢，直接加到链中即可

```
// 展示未定义
function showUndefined(obj) {
    if (typeof obj === 'undefined') {
        console.log('undefined');
    } else {
        this.toNext(obj);
    }
}

var chainUndefined = new ChainItem(showUndefined);
chainString.setNext(chainUndefined);

chainNumber.start(); // undefined
```
由例子可以看到，使用了职责链后，由原本的条件分支换成了很多对象，虽然结构更加清晰了，但在一定程度上可能会影响到性能，所以要注意避免过长的职责链。

 

十一、中介者模式
1. 定义

所有的相关 对象都通过中介者对象来通信，而不是互相引用，所以当一个对象发生改变时，只需要通知中介者对象即可
2. 核心

使网状的多对多关系变成了相对简单的一对多关系（复杂的调度处理都交给中介者）



使用中介者后

 

 



 

 

3. 实现

多个对象，指的不一定得是实例化的对象，也可以将其理解成互为独立的多个项。当这些项在处理时，需要知晓并通过其他项的数据来处理。

如果每个项都直接处理，程序会非常复杂，修改某个地方就得在多个项内部修改

我们将这个处理过程抽离出来，封装成中介者来处理，各项需要处理时，通知中介者即可。

```
var A = {
    score: 10,

    changeTo: function(score) {
        this.score = score;
    
        // 自己获取
        this.getRank();
    },
    
    // 直接获取
    getRank: function() {
        var scores = [this.score, B.score, C.score].sort(function(a, b) {
            return a < b;
        });
    
        console.log(scores.indexOf(this.score) + 1);
    }
};

var B = {
    score: 20,

    changeTo: function(score) {
        this.score = score;
    
        // 通过中介者获取
        rankMediator(B);
    }
};

var C = {
    score: 30,

    changeTo: function(score) {
        this.score = score;
    
        rankMediator(C);
    }
};

// 中介者，计算排名
function rankMediator(person) {
    var scores = [A.score, B.score, C.score].sort(function(a, b) {
        return a < b;
    });

    console.log(scores.indexOf(person.score) + 1);
}

// A通过自身来处理
A.changeTo(100); // 1

// B和C交由中介者处理
B.changeTo(200); // 1
C.changeTo(50); // 3
```
ABC三个人分数改变后想要知道自己的排名，在A中自己处理，而B和C使用了中介者。B和C将更为轻松，整体代码也更简洁

最后，虽然中介者做到了对模块和对象的解耦，但有时对象之间的关系并非一定要解耦，强行使用中介者来整合，可能会使代码更为繁琐，需要注意。

 

十二、装饰者模式
1. 定义

以动态地给某个对象添加一些额外的职责，而不会影响从这个类中派生的其他对象。
是一种“即用即付”的方式，能够在不改变对 象自身的基础上，在程序运行期间给对象动态地 添加职责
2. 核心

是为对象动态加入行为，经过多重包装，可以形成一条装饰链

3. 实现

最简单的装饰者，就是重写对象的属性

var A = {
    score: 10
};

A.score = '分数：' + A.score;
可以使用传统面向对象的方法来实现装饰，添加技能

```
function Person() {}

Person.prototype.skill = function() {
    console.log('数学');
};

// 装饰器，还会音乐
function MusicDecorator(person) {
    this.person = person;
}

MusicDecorator.prototype.skill = function() {
    this.person.skill();
    console.log('音乐');
};

// 装饰器，还会跑步
function RunDecorator(person) {
    this.person = person;
}

RunDecorator.prototype.skill = function() {
    this.person.skill();
    console.log('跑步');
};

var person = new Person();

// 装饰一下
var person1 = new MusicDecorator(person);
person1 = new RunDecorator(person1);

person.skill(); // 数学
person1.skill(); // 数学 音乐 跑步
```
在JS中，函数为一等对象，所以我们也可以使用更通用的装饰函数

```
// 装饰器，在当前函数执行前先执行另一个函数
function decoratorBefore(fn, beforeFn) {
    return function() {
        var ret = beforeFn.apply(this, arguments);
        
        // 在前一个函数中判断，不需要执行当前函数
        if (ret !== false) {
            fn.apply(this, arguments);
        }
    };
}


function skill() {
    console.log('数学');
}

function skillMusic() {
    console.log('音乐');
}

function skillRun() {
    console.log('跑步');
}

var skillDecorator = decoratorBefore(skill, skillMusic);
skillDecorator = decoratorBefore(skillDecorator, skillRun);

skillDecorator(); // 跑步 音乐 数学
```


十三、状态模式
1. 定义

事物内部状态的改变往往会带来事物的行为改变。在处理的时候，将这个处理委托给当前的状态对象即可，该状态对象会负责渲染它自身的行为
2. 核心

区分事物内部的状态，把事物的每种状态都封装成单独的类，跟此种状态有关的行为都被封装在这个类的内部

3. 实现

以一个人的工作状态作为例子，在刚醒、精神、疲倦几个状态中切换着

```
// 工作状态
function Work(name) {
    this.name = name;
    this.currentState = null;

    // 工作状态，保存为对应状态对象
    this.wakeUpState = new WakeUpState(this);
    // 精神饱满
    this.energeticState = new EnergeticState(this);
    // 疲倦
    this.tiredState = new TiredState(this);
    
    this.init();
}

Work.prototype.init = function() {
    this.currentState = this.wakeUpState;
    
    // 点击事件，用于触发更新状态
    document.body.onclick = () => {
        this.currentState.behaviour();
    };
};

// 更新工作状态
Work.prototype.setState = function(state) {
    this.currentState = state;
}

// 刚醒
function WakeUpState(work) {
    this.work = work;
}

// 刚醒的行为
WakeUpState.prototype.behaviour = function() {
    console.log(this.work.name, ':', '刚醒呢，睡个懒觉先');
    
    // 只睡了2秒钟懒觉就精神了..
    setTimeout(() => {
        this.work.setState(this.work.energeticState);
    }, 2 * 1000);
}

// 精神饱满
function EnergeticState(work) {
    this.work = work;
}

EnergeticState.prototype.behaviour = function() {
    console.log(this.work.name, ':', '超级精神的');
    
    // 才精神1秒钟就发困了
    setTimeout(() => {
        this.work.setState(this.work.tiredState);
    }, 1000);
};

// 疲倦
function TiredState(work) {
    this.work = work;
}

TiredState.prototype.behaviour = function() {
    console.log(this.work.name, ':', '怎么肥事，好困');
    
    // 不知不觉，又变成了刚醒着的状态... 不断循环呀
    setTimeout(() => {
        this.work.setState(this.work.wakeUpState);
    }, 1000);
};


var work = new Work('曹操');
```
点击一下页面，触发更新状态的操作



 

4. 优缺点

优点

状态切换的逻辑分布在状态类中，易于维护

缺点

多个状态类，对于性能来说，也是一个缺点，这个缺点可以使用享元模式来做进一步优化

将逻辑分散在状态类中，可能不会很轻易就能看出状态机的变化逻辑

 

十四、适配器模式
1. 定义

是解决两个软件实体间的接口不兼容的问题，对不兼容的部分进行适配
2. 核心

解决两个已有接口之间不匹配的问题

3. 实现

比如一个简单的数据格式转换的适配器

```
// 渲染数据，格式限制为数组了
function renderData(data) {
    data.forEach(function(item) {
        console.log(item);
    });
}

// 对非数组的进行转换适配
function arrayAdapter(data) {
    if (typeof data !== 'object') {
        return [];
    }

    if (Object.prototype.toString.call(data) === '[object Array]') {
        return data;
    }
    
    var temp = [];
    
    for (var item in data) {
        if (data.hasOwnProperty(item)) {
            temp.push(data[item]);
        }
    }
    
    return temp;
}

var data = {
    0: 'A',
    1: 'B',
    2: 'C'
};

renderData(arrayAdapter(data)); // A B C
```


十五、外观模式
1. 定义

为子系统中的一组接口提供一个一致的界面，定义一个高层接口，这个接口使子系统更加容易使用
2. 核心

可以通过请求外观接口来达到访问子系统，也可以选择越过外观来直接访问子系统

3. 实现

外观模式在JS中，可以认为是一组函数的集合

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
