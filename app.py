import os
import requests
import json
import bs4
import time
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI as OpenAILLM
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")


# Get the json data from the website
def get_data():
    current_time_milliseconds = int(time.time() * 1000)
    url = "https://rpilocator.com/data.cfm"
    querystring = {"method": "getProductTable", "token": "9pxkgncqyjpsfg2v6ekmsbkw1pfwf0929skq28si", "_": current_time_milliseconds}
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Sec-Fetch-Site": "same-origin",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Mode": "cors",
        "Host": "rpilocator.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4.1 Safari/605.1.15",
        "Connection": "keep-alive",
        "Referer": "https://rpilocator.com/",
        "Cookie": "_ga_JWVD0LRP64=GS1.1.1681654548.5.0.1681654548.0.0.0; _ga=GA1.1.136564858.1681170765; RPILOCATOR=0; CFID=f3a9a0f9-d1de-4533-a1e6-c75fce5e177e; CFTOKEN=0; cfid=f3a9a0f9-d1de-4533-a1e6-c75fce5e177e; cftoken=0",
        "X-Requested-With": "XMLHttpRequest"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.content


# Get all the product links from the json data
def get_price_links(data):
    json_data = json.loads(data)
    data_list = json_data["data"]
    return [entry["link"] for entry in data_list]


# Get stock info from a single each product link
def get_stock_info(link):
    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    body = soup.find("body")

    text_splitter = CharacterTextSplitter(separator="", chunk_size=1000, chunk_overlap=200, length_function=len)
    texts = text_splitter.split_text(str(body))

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    docsearch = FAISS.from_texts(texts, embeddings)

    chain = load_qa_chain(OpenAILLM(openai_api_key=openai_api_key), chain_type="stuff")
    query = "Is the main product on the website in stock and how many are in stock? Only respond with the following format: `Product Name: Raspberry Pi 4 model B WiFi DualBand Bluetooth 2GB RAM 1,5GHz Availabity: Yes, 10 or No, 0.` Do not include the backticks in your response and do not deviate from the format given even if you dont know the answer just put 0 when is not in stok and when is in stock but doesnt provide quantity just put Unknown."
    docs = docsearch.similarity_search(query)
    answer = chain.run(input_documents=docs, question=query)
    print(answer)

def main():
    data = get_data()
    price_links = get_price_links(data)
    print(len(price_links), "price links found")
    
    for link in price_links:
        get_stock_info(link)
    
if __name__ == "__main__":
    main()