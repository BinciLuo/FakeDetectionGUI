import json
import os
from PIL import Image
from model import checkFake
import gradio as gr

with open("config.json", 'r') as json_file:
    config:dict = json.load(json_file)

def checkProcess(img: Image.Image):
    isFake = False # FIXME: Set this line to annotation.
    # TODO: implement your code here using function from model.py
    # For example
    # isFake = checkFake(img)
    if isFake:
        gr.Warning("Fake")
    else:
        gr.Info("Real")


with gr.Blocks() as demo:
    gr.HTML(f"""<h1 align="center">{config.get("title","demo")}</h1>""")
    
    with gr.Row():
        with gr.Column():
            baseIMGViewer = gr.Image(label='Upload Image', type='pil', interactive=True)
            with gr.Accordion("Examples", open=False): 
                gr.Examples(["example/"+filename for filename in os.listdir("./example") if filename.split('.')[-1].lower() in ["jpeg","jpg","png"]], baseIMGViewer)
            RunBtn = gr.Button("Check Server Status", variant="primary")

        RunBtn.click(checkFake, [baseIMGViewer],[])


demo.queue().launch(share=False, inbrowser=True, server_name='0.0.0.0', server_port=config.get("port",27777), debug=True)