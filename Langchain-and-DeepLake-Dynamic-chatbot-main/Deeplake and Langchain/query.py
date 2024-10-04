import gradio as gr
import os
#import getpass
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.vectorstores import DeepLake
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
os.environ['OPENAI_API_KEY'] = 'sk-evbehhhehwhshshsbsbsvsv'
os.environ['ACTIVELOOP_TOKEN'] = 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTY4NjU1ODk1MCwiZXhwIjoxNjg5NDk2NDM5fQ.eyJpZCI6Im1haWRhIn0.dS_b71zbnQk9REjFf2ZOCr1fWjt4w7FkfB12R90HIFIRk6q51Nq0Nl3UQTyn_o52Mi7asKLEtnsw6wDMa_0j_Q'
embeddings = OpenAIEmbeddings(disallowed_special=())
def Train():
    try:
        root_dir = '/Users/wasiq/Desktop/OIPRO/proactive-intervention/app/src/main/java/com/intuit/v4/help/selfhelp/pais'
        docs = []
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for file in filenames:
                try:
                    loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
                    docs.extend(loader.load_and_split())
                except Exception as e:
                    pass
        text_splitter = CharacterTextSplitter(chunk_size=4000, chunk_overlap=0)
        texts = text_splitter.split_documents(docs)
        username = "wasiq"
        db = DeepLake(dataset_path=f"hub://{username}/intt", embedding_function=embeddings)#dataset would be publicly available
        db.add_documents(texts)
    except Exception as e:
        print(e)
Train()