This Project I have used the llama ggmlv models to run it locally 

" The Url where I have used to download the model" - https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

Post downloading the appropropriate model with .bin format from above location in hugging face. Place that dowloaded model.bin file under Model folder.

Then provide the appropriate model path in the app.py file to instantiate/Load the model.

This is not mandatory step but still its better to create the virtual environment - Create a virtual environment and activate the environment from the terminal in editor you are loading this project it can be pycharm/VSCode

Once activating the virtual env and in same terminal install all the required libraries by running the command "pip install -r requirements.txt"

Then once all the libraries are downloaded then open the terminal on the editor and ensure that your terminal points to the activated virtual env if you have created the virtual environment if not no issues directly you can just run "streamlit run app.py" command.

Post this you can see the app UI is loaded in the chrome using local host.

At this point you are good to play around the UI by providing the appropriate inputs.

This is a simple project used to chat with AI-Model for text generation as like in chat GPT
