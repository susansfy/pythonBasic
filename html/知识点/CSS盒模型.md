##认识
是css布局的基石，它规定了网页元素如何显示以及元素间相互关系

模式：标准模式和怪异模式

margin\border\padding：外边框、边框、内边框；单位是px；

##盒的内容
1、overflow:指定如果内容溢出一个元素的框（这里指框溢出），会发生什么
overflow:visible/hidden/scroll/auto;
visible:默认值，内容不会被剪裁，会呈现元素框之外
hidden：内容被剪裁，其余内容不可见
scroll:内容被剪裁，滚动条显示其余内容
auto:如果内容被剪裁，则浏览器以滚动条显示其余内容；跟scroll的区别是，scroll是在框里加滚动条，auto是在浏览器加滚动条

2、text-overflow:指定当文本溢出包含它的元素(这里指框内的文字等内容溢出)，应该发生什么
text-overflow：clip/elipsis/string;
clip：修剪文本
elipsis：显示省略符号来代表被修剪的文本
string:使用给定的字符串来代表被修剪的文本

注意：text-overflow必须和overflow:hidden;while-space:nowrap一起使用