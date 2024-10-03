from langchain.document_loaders import PyPDFDirectoryLoader
import pinecone 

def read_doc(directory):
    file_loader=PyPDFDirectoryLoader(directory)
    documents=file_loader.load()
    return documents


docs = read_doc("give the path of the dir")
print(len)

#Perform chunking/overlaping here. 


#Use embeddings models to embed the text 

index=Pinecone.from_documents(doc,embeddings,index_name=index_name)


## Cosine Similarity Retreive Results from VectorDB
# def retrieve_query(query,k=2):
#     matching_results=index.similarity_search(query,k=k)
#     return matching_results

# from langchain.chains.question_answering import load_qa_chain
# from langchain import OpenAI



# Retrieval function
def retrieve_answers(query):
    doc_search=retrieve_query(query)
    print(doc_search)
    response=chain.run(input_documents=doc_search,question=query)
    return response
our_query = "What is the failure policy of a job at prohance? "
answer = retrieve_answers(our_query)
print(answer)