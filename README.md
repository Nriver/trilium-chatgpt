# Trilium-ChatGPT

This project enables communication between Trilium Notes and ChatGPT, acting as a middle service that facilitates
querying ChatGPT and saving the responses to your Trilium Notes.

## How to Use

1. Install Python 3 on your machine.
2. Clone the code repository:

   ```
   git clone https://github.com/Nriver/trilium-chatgpt
   ```

3. Install the required dependencies:

   ```
   cd trilium-chatgpt
   pip install -r requirements.txt
   ```

4. Open the `settings.py.sample` file, modify the configurations according to your needs, and rename it
   to `settings.py`. You will need to set your OpenAI API key, Trilium's ETAPI token, and other relevant settings.

5. Run the application:

   ```
   python3 main.py
   ```

6. Open your web browser and test the functionality by accessing `http://127.0.0.1:5000/query?keyword=Trilium+Notes`.
   This should create a new note under the specified note ID.

7. Optionally, you can set the search engine to `http://127.0.0.1:5000/query?keyword={keyword}` in Trilium. This allows
   you to select some text, right-click, and search ChatGPT with the selected text.

Please note that you may need to customize the configurations further to suit your specific environment and
requirements.
