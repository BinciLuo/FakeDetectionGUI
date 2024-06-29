import json
import os
from PIL import Image
from model import checkFake
import gradio as gr

with open("config.json", 'r') as json_file:
    config:dict = json.load(json_file)

FAKE_THRESHOLD = config.get("threshold", 0.7)

def checkProcess(img: Image.Image):
    fakeConfidenceLevel = checkFake(img)
    # TODO: implement your code here using function from model.py
    # For example
    # isFake = checkFake(img)
    if fakeConfidenceLevel > FAKE_THRESHOLD:
        gr.Warning("Fake")
    else:
        gr.Info("Real")
    
    return fakeConfidenceLevel


with gr.Blocks() as demo:
    gr.HTML(f"""<h1 align="center">{config.get("title","demo")}</h1>""")
    
    with gr.Row():
        with gr.Column():
            baseIMGViewer = gr.Image(label='Upload Image', type='pil', interactive=True)
            with gr.Accordion("Examples", open=False): 
                gr.Examples(["example/"+filename for filename in os.listdir("./example") if filename.split('.')[-1].lower() in ["jpeg","jpg","png"]], baseIMGViewer)
            RunBtn = gr.Button("Check", variant="primary")
        
            confidenceLevel = gr.Number(label='Fake Confidence Level', interactive=False)

        RunBtn.click(checkProcess, [baseIMGViewer],[confidenceLevel])


demo.queue().launch(share=False, 
                    inbrowser=True, 
                    server_name='0.0.0.0', 
                    server_port=config.get("port",27777), 
                    debug=True)