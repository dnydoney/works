# 技术·文档 | 18个编写 JavaScript 好习惯！
-----------------------------------------------------------------

1.常量使用const代替var
```
    常量是永远不变的变量，这样声明变量可以确保它们永远不变。
    /* 旧方法 */
    var i = 1;

    /* 正确方式 */
    const i = 1;
 ```

2. 使用let替换变量，而不是var
   ```
    let语句声明了一个具有块作用域的局部作用域变量
    /* 不适当的*/
    var myVal = 1;
    for (var i; i < 10; i++){
        myVal = 1 + i;
    }

    /* 正确方式*/
    let myVal = 1;
    for (let i; i < 10; i++){
      myVal += i
    }
  ```
3.声明对象
  ```
    用快捷方式声明对象
    /* 
      旧方法
      The Object() class makes an unnecessary function call
    */

    const myObject = new Object();
    /* 正确方式*/
    const myObject = {};
    
  ```
5.连接字符串

```
    /* 旧方法 */
    const myStringToAdd = "world";
    const myString = "hello " + myStringToAdd;


    /* 正确方式*/
    const myStringToAdd = "world";
    const myString = `hello ${myStringToAdd}`;
    
```

6. 使用对象方法简写
    
```

    /* 不适当 */
    const customObject = {
        val: 1,
        addVal: function () {
       return customObject.val + 1;
        }
    }

    /* 正确方式*/
    const customObject = {
      val: 1,
      addVal(){
        return customObject.val++
      }
    }**加粗文字**
    
```

7.创建对象的值
```
    /* 旧方法*/
    const value = 1;
    const myObject = {
      value: value
    }
    /* 正确方式*/
    const value = 1;
    const myObject = {
      value
    }
    
```
8. 给对象赋值
```
    /* 旧方法 */
    const object1 = { val: 1, b: 2 };
    let object2 = { d: 3, z: 4 };
    object2.val = object1.val;
    object2.b = object1.b;

    /* 正确方式 */
    const object1 = { val: 1, b: 2 };
    const object2 = { ...object1, d: 3, z: 4 }
    
```
9. 给数组赋值

```

    /* 不适当*/
    const myArray = [];
    myArray[myArray.length] = "hello world";


    /* 正确方式 */
    const myArray = [];
    myArray.push('Hello world');
    
```
10. 连接数组
```
    /* 不适当*/
    const array1 = [1,2,3,4];
    const array2 = [5,6,7,8];
    const array3 = array1.concat(array2);


    /* 正确方式 */
    const array1 = [1,2,3,4];
    const array2 = [5,6,7,8];
    const array3 = [...array1, ...array2]
 ```
11.获取对象的多个属性

```
    /* 不适当*/
    function getFullName(client){
      return `${client.name} ${client.last_name}`;
    }

    /* 正确方式 */
    function getFullName({name, last_name}){
      return `${name} ${last_name}`;
    }
```
12.从对象获取值

```
    /* 不适当*/
    const object1 = { a: 1 , b: 2 };
    const a = object1.a;
    const b = object1.b;

    /* 正确方式 */
    const object1 = { a: 1 , b: 2 };
    const { a, b } = object1;

```

13. 创建函数

```
    /* 老办法，但很好 */
    function myFunc() {}

    /* 很好*/
    const myFunc = function() {}

    /* 最好 */
    const myFunct = () => {}

    // 重要说明：在某些情况下，建议不要将这些函数与箭头一起使用，以避免读取错误

```

14.默认值

```
    /* 不适当*/
    const myFunct = (a, b) => {
      if (!a) a = 1;
      if (!b) b = 1;
      return { a, b };
    }

    /* 正确方式 */
    const myFunct = (a = 1, b = 1) => {
      return { a, b };
    }
```
15. 使用reduce代替forEach和for来求和


```

    /* 不适当*/
    const values = [1, 2, 3, 4, 5];
    let total = 0;
    values.forEach( (n) => { total += n})

    /* 不适当*/
    const values = [1, 2, 3, 4, 5];
    let total = 0;
    for (let i; i < values.length; i++){
      total += values[i];
    }

    /* 正确方式 */
    const values = [1, 2, 3, 4, 5];
    const total = values.reduce((total, num) => total + num);

```
16. 是否存在数组中

```
    /* 不适当*/
    const myArray = [{a: 1}, {a: 2}, {a: 3}];
    let exist = false;
    myArray.forEach( item => {
     if (item.a === 2) exist = true
    })

    /* 正确方式 */
    const myArray = [{a: 1}, {a: 2}, {a: 3}];
    const exist = myArray.some( item => item.a == 2)

```
17.布尔值的快捷方式

```
    /* 不适当*/
    const a = 5;
    let b;
    if (a === 5){
      b = 3;
    } else {
      b = 2;
    }

    /* 正确方式 */
    const a = 5;
    const b = a === 5 ? 3 : 2;


```