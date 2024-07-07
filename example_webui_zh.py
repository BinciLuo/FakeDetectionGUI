'''
关键部分解释
1. 配置文件读取：读取 config.json 文件中的配置信息，用于初始化界面。
2. 信息处理函数：InfoProcess 用于处理图片上传事件。
3. 推理处理函数：InferenceProcess 实现对图片和其他输入的处理，并返回处理结果。
4. Gradio 界面创建：使用 gr.Blocks() 定义界面布局，包括图像上传、滑动条、文本框等组件。
5. 事件绑定：使用 click 方法将按钮点击事件绑定到处理函数上，使用 change 方法将图片变化事件绑定到信息处理函数上。
6. 启动界面：使用 demo.queue().launch() 启动 Gradio 界面，允许用户通过 Web 浏览器访问。
'''

import json  # 导入 JSON 库
import os  # 导入操作系统接口模块
from PIL import Image  # 从 PIL 库导入 Image 模块
from example_model import inference  # 从 example_model 导入 inference 函数
import gradio as gr  # 导入 Gradio 库并命名为 gr

# 读取配置文件中的配置信息
with open("config.json", 'r') as json_file:  # 打开 config.json 文件
    config: dict = json.load(json_file)  # 将 JSON 文件中的数据加载到 config 字典中

# 定义信息处理函数，用于处理图片上传事件
def InfoProcess():  # 定义 InfoProcess 函数
    gr.Info("InfoProcess")  # 调用 Gradio 的 Info 函数，显示 "InfoProcess" 信息

# 定义推理处理函数，处理图片和其他输入，并返回处理结果
def InferenceProcess(img: Image.Image, input: str, float_value1: float, float_value2: float, str_value: str):  # 定义 InferenceProcess 函数，带有五个参数
    # 检查参数
    if img is None:  # 如果 img 为 None
        gr.Warning("Image: None")  # 调用 Gradio 的 Warning 函数，显示警告信息 "Image: None"
        return None, ''  # 返回 None 和空字符串

    # TODO: 实现预处理代码
    #
    #

    # 调用推理函数，得到输出图像和输出文本
    output_img, output_text = inference(img, input, float_value1, float_value2, str_value)  # 调用 inference 函数，传入参数并接收返回的输出图像和输出文本

    # TODO: 实现期望的返回代码
    #
    #

    gr.Info("Finish Inference Process")  # 调用 Gradio 的 Info 函数，显示 "Finish Inference Process" 信息
    return output_img, output_text  # 返回输出图像和输出文本

# 创建 Gradio 界面
with gr.Blocks() as demo:  # 使用 Gradio 的 Blocks 创建界面，并命名为 demo
    # 设置页面标题
    gr.HTML(f"""<h1 align="center">{config.get("title","title")}</h1>""")  # 使用 Gradio 的 HTML 组件设置页面标题，居中显示

    # TODO: 设置组件布局
    # ------------------------------------------------------------------------------------------
    with gr.Column():  # 设置列布局

        with gr.Accordion("Settings"):  # 可折叠的设置部分
            exampleSilder = gr.Slider(label='ExampleSilder', minimum=0, maximum=100, step=0.5, value=config['inference']['example_silder_default_value'])  # 创建一个滑动条组件
            exampleFloatValue = gr.Number(label='ExampleFloatValue', value=config['inference']['example_number_default_value'])  # 创建一个数字输入组件
            exampleDropdown = gr.Dropdown(  # 创建一个下拉菜单组件
                label='ExampleDropdown', 
                value=config['inference']['example_dropdown_default_value'],
                choices=config['inference']['example_dropdown_enum']
                )
            
        with gr.Row():  # 设置行布局
            with gr.Column():  # 在行内设置列布局
                baseIMGViewer = gr.Image(label='Upload Image', type='pil', interactive=True)  # 创建一个图像上传组件
                with gr.Accordion("Examples", open=False):  # 创建一个可折叠的示例部分
                    gr.Examples(["example/" + filename for filename in os.listdir("./example") if filename.split('.')[-1].lower() in ["jpeg","jpg","png"]], baseIMGViewer)  # 显示示例图像
            resultIMGViewer = gr.Image(label='Result Image', type='pil', interactive=False)  # 创建一个不可交互的图像显示组件

        inputTextbox = gr.Textbox(label='Input', interactive=True)  # 创建一个可交互的文本输入框
        inferenceBtn = gr.Button("Check", variant="primary")  # 创建一个主要按钮
        resultTextbox = gr.Textbox(label='Result Text', interactive=False)  # 创建一个不可交互的文本显示框
    # ------------------------------------------------------------------------------------------

    # TODO: 绑定事件
    # ---------------------------------------------
    inferenceBtn.click(  # 为按钮的点击事件绑定处理函数
        InferenceProcess,  # 绑定的处理函数
        [baseIMGViewer, inputTextbox, exampleSilder, exampleFloatValue, exampleDropdown],  # 输入组件
        [resultIMGViewer, resultTextbox]  # 输出组件
        )
    baseIMGViewer.change(InfoProcess, [], [])  # 为图像上传组件的变化事件绑定信息处理函数
    # ---------------------------------------------

# 启动 Gradio 界面
if __name__ == '__main__':
    demo.queue().launch(share=False,  # 设置是否分享
                        inbrowser=True,  # 设置是否在浏览器中启动
                        server_name='0.0.0.0',  # 设置服务器名称
                        server_port=config.get("port", 27777),  # 设置服务器端口
                        debug=True)  # 设置调试模式
