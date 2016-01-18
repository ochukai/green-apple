## 交互属性
表单组件支持几个受用户交互影响的属性：

* value，用于 `<input>`、`<textarea>` 组件。
* checked，用于类型为 checkbox 或者 radio 的 `<input>` 组件。
* selected，用于 `<option>` 组件。

在 HTML 中，`<textarea>` 的值通过子节点设置；在 React 中则应该使用 value 代替。

表单组件可以通过 **onChange** 回调函数来监听组件变化。当用户做出以下交互时，**onChange** 执行并通过浏览器做出响应：

* `<input>` 或 `<textarea>` 的 value 发生变化时。
* `<input>` 的 checked 状态改变时。
* `<option>` 的 selected 状态改变时。

> 和所有 DOM 事件一样，所有的 HTML 原生组件都支持 onChange 属性，而且可以用来监听冒泡的 change 事件。

---

## 受限组件
```js
  getInitialState: function() {
    return {value: 'Hello!'};
  },

  handleChange: function(event) {
    this.setState({value: event.target.value});
  },

  render: function() {
    var value = this.state.value;
    return <input type="text" value={value} onChange={this.handleChange} />;
  }
```

## 不受限组件
```js
  render: function() {
    return <input type="text" />;
  }

  // or

  render: function() {
    return <input type="text" defaultValue="Hello!" />;
  }
```


## Textarea

```html
<textarea name="description" value="This is a description." />
```

## Select

```html
<select value="B">
    <option value="A">Apple</option>Â
    <option value="B">Banana</option>
    <option value="C">Cranberry</option>
  </select>
```
> ### 注意
> 给 value 属性传递一个数组，可以选中多个选项：`<select multiple={true} value={['B', 'C']}>`。
