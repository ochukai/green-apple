
```js
Checkbox.propTypes = {
  prefixCls: React.PropTypes.string,
  style: React.PropTypes.object,
  type: React.PropTypes.string,
  className: React.PropTypes.string,
  defaultChecked: React.PropTypes.oneOfType([React.PropTypes.number, React.PropTypes.bool]),
  checked: React.PropTypes.oneOfType([React.PropTypes.number, React.PropTypes.bool]),
  onChange: React.PropTypes.func,
};

Checkbox.defaultProps = {
  prefixCls: 'rc-checkbox',
  style: {},
  type: 'checkbox',
  className: '',
  defaultChecked: 0,
  onChange: () => {
  },
};

```