LLM Data Parser
==================

This proof-of-concept script demonstrates how to use a language model (LLM) like GPT-3 or GPT-4 to find and extract meaningful data from HTML data without extensive HTML parsing, in this case is extracting relelvant data related to product stock and availability from a list of webpages. It uses the Langchain library to achieve this goal.

Installation
------------

To run this script, you need to have Python 3.11.3 and the following libraries installed:

* requests
* json
* openai
* time
* bs4
* langchain

The recommended approach is to use a Python virtual environment:

```bash
python3 -m venv venv
. venv/bin/activate
```

Then, install the required libraries using pip:

`pip install -r requirements.txt`

Additionally, you need to have an OpenAI API key, which can be obtained from their website.

Usage
-----

To use this script, simply run the `main()` function. The script will scrape product links from the target website and then use the LLM to query each product's availability.

The results will be printed to the console in the specified format.

As an alternative to OpenAI, you can use GPT4All with the Langchain library, which is a free and open-source model. For more information on using GPT4All with Langchain, refer to the following link:

[https://python.langchain.com/en/latest/modules/models/llms/integrations/gpt4all.html](https://python.langchain.com/en/latest/modules/models/llms/integrations/gpt4all.html)

For a detailed explanation of the code, you can visit the following resources:

*   Colab Notebook: [https://colab.research.google.com/drive/181BSOH6KF\_1o2lFG8DQ6eJd2MZyiSBNt?usp=sharing#scrollTo=3mtAth2jXNKO](https://colab.research.google.com/drive/181BSOH6KF_1o2lFG8DQ6eJd2MZyiSBNt?usp=sharing#scrollTo=3mtAth2jXNKO)
*   YouTube Video: [https://www.youtube.com/watch?v=TLf90ipMzfE](https://www.youtube.com/watch?v=TLf90ipMzfE)

Credits
-------

This script was extended by repollo from the original code by Prompt Engineering, as shown in this YouTube video: [https://www.youtube.com/watch?v=TLf90ipMzfE](https://www.youtube.com/watch?v=TLf90ipMzfE)
