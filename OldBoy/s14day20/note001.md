#补充
fileobj = request.Files.get()
fileobj.size    文件大小(字节)

urls.py 中regex的表达式要加`$`符号防止覆盖

QuerySet.values(columns) 返回字典列表

QuerySet.values_list(columns) 返回元组列表

```
__gt  大于
__lt  小于
__gte 大于等于
__lte 小于等于
```
models.TableName.objects.get()    //获取TableName单条数据对象
返回的是一个TableName数据对象, 没有数据会触发异常

QuerySet是TableName对象的集合

#外键
models.ForeignKey(to, to_field=None)

#双下__
Django中用字符串中的双下划线代用点号,
filter()中的参数,
values()参数,
values_list()参数

#forloop模板变量
是一个字典, 有六个键:

forloop.counter       //循环计数器, 从1开始
forloop.counter0      //循环计数器, 从0开始
forloop.revcounter    //循环计数器, 倒数到1为止
forloop.revcounter0   //循环计数器, 倒数到0为止
forloop.first         //本次是否是第一次循环
forloop.last          //本次是否是最后一次循环
forloop.parentloop    //上层循环对象

#ajax
$.ajax({
  url:"/xxx/",
  type:"post",
  data:{},
  success:function(data){}
  })
$.get()
$.post()