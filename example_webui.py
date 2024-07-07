import json
import os
from PIL import Image
from example_model import inference
import gradio as gr

with open("config.json", 'r') as json_file:
    config:dict = json.load(json_file)

def InfoProcess():
    gr.Info("InfoProcess")

def InferenceProcess(img: Image.Image, input: str, float_value1: float, float_value2: float, str_value: str):
    # TODO: Check Args:
    if img == None:
        gr.Warning("Image: None")
        return None, ''

    # TODO: implement your preprocess code
    #
    #

    output_img, output_text = inference(img, input, float_value1, float_value2, str_value)

    # TODO: implement your code here for expected return
    #
    #

    gr.Info("Finish Inference Process")    
    return output_img, output_text

with gr.Blocks() as demo:
    gr.HTML(f"""<h1 align="center">{config.get("title","title")}</h1>""")
    
    # TODO: Set Components Layout Here
    # ------------------------------------------------------------------------------------------
    with gr.Column(): # TODO: Column Layout

        with gr.Accordion("Settings"): # TODO: Can be fold
            exampleSilder = gr.Slider(label='ExampleSilder', minimum=0, maximum=100, step=0.5, value=config['inference']['example_silder_default_value'])
            exampleFloatValue = gr.Number(label='ExampleFloatValue', value=config['inference']['example_number_default_value'])
            exampleDropdown = gr.Dropdown(
                label='ExampleDropdown', 
                value=config['inference']['example_dropdown_default_value'],
                choices=config['inference']['example_dropdown_enum']
                )
            
        with gr.Row(): # TODO: Row Layout
            with gr.Column():
                baseIMGViewer = gr.Image(label='Upload Image', type='pil', interactive=True)
                with gr.Accordion("Examples", open=False): 
                    gr.Examples(["example/"+filename for filename in os.listdir("./example") if filename.split('.')[-1].lower() in ["jpeg","jpg","png"]], baseIMGViewer)
            resultIMGViewer = gr.Image(label='Result Image', type='pil', interactive=False)

        inputTextbox = gr.Textbox(label='Input', interactive=True)
        inferenceBtn = gr.Button("Check", variant="primary")
        resultTextbox = gr.Textbox(label='Result Text', interactive=False)
    # ------------------------------------------------------------------------------------------


    # TODO: Bind Event Here
    # ---------------------------------------------
    inferenceBtn.click(
        InferenceProcess, 
        [baseIMGViewer, inputTextbox, exampleSilder, exampleFloatValue, exampleDropdown], 
        [resultIMGViewer, resultTextbox]
        )
    baseIMGViewer.change(InfoProcess, [], [])
    # ---------------------------------------------

if __name__ == '__main__':
    demo.queue().launch(share=False, 
                        inbrowser=True, 
                        server_name='0.0.0.0', 
                        server_port=config.get("port",27777), 
                        debug=True)