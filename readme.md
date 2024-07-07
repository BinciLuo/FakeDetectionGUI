## Demo
### Usage
#### Settings
Set default values in `config.json`. 
#### Run
1. `cd ${PATH2THIS_FOLDER}`
2. If you need to use proxy, please set Environment Variable. For example run `export all_proxt='URL2YOUR_SOCKS5_PROXY'`
3. `conda activate ${YOUR_VENV} && python example_webui.py`
### Annotation
The demo should be built with existed functions and code. You shouldn't change existed code and if you must modify some existed code, please create amother file and use functions in your existed code. 

If you want to build a webui for your project, you should know these:
#### Components
The webui was built with many components of `gradio`. For example, `gr.Textbox` can be used as a textual input and output, `gr.Image` can be used as an image input and output, and `gr.Slider` can be used as a value input. 

For more usage of components, you can visit this [website](https://www.gradio.app/docs/gradio/blocks) 

#### Event
When you click some `components` or `components` were changed, `event` occurs. You should bind every useful `event` with `processing function` , of which input and output should be `components` of `Gradio`. 
![](./resource/image1.png)

For example, `{$COMPONENTS}.click({$PROCESSING_FUNCTION},[{$INPUTS}],[$OUTPUTS])` or `{$COMPONENTS}.change({$PROCESSING_FUNCTION},[{$INPUTS}],[$OUTPUTS])`
`example_webui.py` shows where the components exist and how will they react with each other.

## 演示
### 用法
#### 设置
在 `config.json` 中设置默认值。
#### 运行
1. `cd ${PATH2THIS_FOLDER}`
2. 如果需要使用代理，请设置环境变量。例如，运行 `export all_proxy='URL2YOUR_SOCKS5_PROXY'`
3. `conda activate ${YOUR_VENV} && python example_webui.py`
### 注释
该演示应基于现有的函数和代码构建。你不应该更改现有代码，如果必须修改某些现有代码，请创建另一个文件并使用现有代码中的函数。

如果你想为你的项目构建一个 Web 界面，你应该知道这些：
#### 组件
Web 界面由许多 `gradio` 组件构建。例如，`gr.Textbox` 可用作文本输入和输出，`gr.Image` 可用作图像输入和输出，`gr.Slider` 可用作值输入。

有关组件的更多用法，请访问这个 [网站](https://www.gradio.app/docs/gradio/blocks)

#### 事件
当你点击某些 `组件` 或 `组件` 发生变化时，会触发 `事件`。你应该将每个有用的 `事件` 与 `处理函数` 绑定，其输入和输出应为 `Gradio` 的 `组件`。

例如，`{$COMPONENTS}.click({$PROCESSING_FUNCTION},[{$INPUTS}],[$OUTPUTS])` 或 `{$COMPONENTS}.change({$PROCESSING_FUNCTION},[{$INPUTS}],[$OUTPUTS])`
`example_webui_zh.py` 显示了组件的存在位置以及它们如何相互反应。
