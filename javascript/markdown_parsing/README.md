# Markdown parsing

In Node.js, you could parse markdown with "marked.js" into HTML.

Here is an example:

```js  
var marked = require('marked');
var markdown = '# Hello World';
var html = marked(markdown);
console.log(html);
```

[Sample code](./marked_js_example.js)
