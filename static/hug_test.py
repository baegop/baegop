import torch
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch
import numpy as np
import urllib.request
from tqdm import tqdm
tqdm.pandas()

model = SentenceTransformer("Huffon/sentence-klue-roberta-base")
# 모델 저장 변수 이름.save_pretrained(원하는 디렉토리) 형태

Chatbot_Data=pd.read_csv("ChatBotData.csv") 
#
# Chatbot_Data['EmbVector'] = Chatbot_Data['Q'].progress_map(lambda x : model.encode(x))
# #print(Chatbot_Data.head())
# EmbData = torch.tensor(Chatbot_Data['EmbVector'].tolist())
# Chatbot_Data.to_csv("ChatBotData_emb.csv",encoding="utf-8-sig")
#np.save('emb_file',EmbData)

EmbData =np.load('emb_file.npy')

def chat(sent="0"):
    print('=====행복한 대화시간 되세요=====')
    while 1:
        q = input("사용자 > ").strip()
        if q == "quit":
            break
        a = ""
        # Sentense Embedding으로 텍스트 유사도를 구합니다.
        q = model.encode(q)
        # 질문을 Tensor로 바꿉니다.
        q = torch.tensor(q)
        # 코사인 유사도 
        cos_sim = util.pytorch_cos_sim(q, EmbData)

        #유사도가 가장 비슷한 질문 인덱스를 구합니다.
        best_sim_idx = int(np.argmax(cos_sim))

        # 질문의 유사도와 가장 비슷한  답변 제공
        answer = Chatbot_Data['A'][best_sim_idx]
        print("챗봇 >", answer)


chat()


# docs = [
#     "1992년 7월 8일 손흥민은 강원도 춘천시 후평동에서 아버지 손웅정과 어머니 길은자의 차남으로 태어나 그곳에서 자랐다.",
#     "형은 손흥윤이다.",
#     "춘천 부안초등학교를 졸업했고, 춘천 후평중학교에 입학한 후 2학년때 원주 육민관중학교 축구부에 들어가기 위해 전학하여 졸업하였으며, 2008년 당시 FC 서울의 U-18팀이었던 동북고등학교 축구부에서 선수 활동 중 대한축구협회 우수선수 해외유학 프로젝트에 선발되어 2008년 8월 독일 분데스리가의 함부르크 유소년팀에 입단하였다.",
#     "함부르크 유스팀 주전 공격수로 2008년 6월 네덜란드에서 열린 4개국 경기에서 4게임에 출전, 3골을 터뜨렸다.",
#     "1년간의 유학 후 2009년 8월 한국으로 돌아온 후 10월에 개막한 FIFA U-17 월드컵에 출전하여 3골을 터트리며 한국을 8강으로 이끌었다.",
#     "그해 11월 함부르크의 정식 유소년팀 선수 계약을 체결하였으며 독일 U-19 리그 4경기 2골을 넣고 2군 리그에 출전을 시작했다.",
#     "독일 U-19 리그에서 손흥민은 11경기 6골, 2부 리그에서는 6경기 1골을 넣으며 재능을 인정받아 2010년 6월 17세의 나이로 함부르크의 1군 팀 훈련에 참가, 프리시즌 활약으로 함부르크와 정식 계약을 한 후 10월 18세에 함부르크 1군 소속으로 독일 분데스리가에 데뷔하였다.",
# ]
# urllib.request.urlretrieve(
#     "https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv",
#     filename="ChatBotData.csv",
# )
#document_embeddings = model.encode(docs)


'''
query = "손흥민은 어린 나이에 유럽에 진출하였다."
query_embedding = model.encode(query)

top_k = min(5, len(docs))
cos_scores = util.pytorch_cos_sim(query_embedding, document_embeddings)[0]
top_results = torch.topk(cos_scores, k=top_k)

print(f"입력 문장: {query}")
print(f"<입력 문장과 유사한 {top_k} 개의 문장>")

for i, (score, idx) in enumerate(zip(top_results[0], top_results[1])):
    print(f"{i+1}: {docs[idx]} {'(유사도: {:.4f})'.format(score)}")
'''