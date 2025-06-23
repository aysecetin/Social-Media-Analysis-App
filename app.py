import gradio as gr
import pandas as pd
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

# Veri yükleme
df_opinions = pd.read_csv("classified_opinions.csv")
df_topics = pd.read_csv("conclusions.csv")

# Modelleri yükleme
semantic_model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L6-v2")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
summarizer = pipeline("summarization", model="google/flan-t5-large")

# Kullanıcı yorumlarını geçici olarak bellekte tut
user_comments = []

# Yorum ekleme fonksiyonu
def add_comment(comment_text):
    topic_texts = df_topics["topic"].tolist()
    embeddings1 = semantic_model.encode([comment_text], convert_to_tensor=True)
    embeddings2 = semantic_model.encode(topic_texts, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(embeddings1, embeddings2)[0]
    best_idx = cos_scores.argmax().item()
    best_topic = df_topics.iloc[best_idx]["topic"]

    label_result = classifier(comment_text, candidate_labels=["Claim", "Evidence", "Counterclaim", "Rebuttal"])
    predicted_label = label_result["labels"][0]

    user_comments.append({
        "topic": best_topic,
        "comment": comment_text,
        "type": predicted_label
    })
    return f"✅ Yorum eklendi.\n\n🔎 Tahmini tür: {predicted_label}\n📌 İlgili konu: {best_topic}"

# Konu analiz fonksiyonu
def analyze_topic(topic_query):
    matching_comments = [uc for uc in user_comments if topic_query.lower() in uc["topic"].lower()]
    if not matching_comments:
        return "⚠️ Bu konuyla ilgili yorum bulunamadı.", ""

    comments_text = " ".join([c["comment"] for c in matching_comments])
    summary = summarizer(comments_text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
    df = pd.DataFrame(matching_comments)
    return df, summary

# Gradio Arayüzü
with gr.Blocks() as demo:
    with gr.Tab("➕ Add Comment"):
        input_text = gr.Textbox(label="Yorumunuzu girin")
        output_text = gr.Textbox()
        btn = gr.Button("Yorumu Ekle")
        btn.click(fn=add_comment, inputs=input_text, outputs=output_text)

    with gr.Tab("📊 Analyze Topic"):
        topic_in = gr.Textbox(label="Konu başlığından bir parça girin")
        table_out = gr.Dataframe()
        summary_out = gr.Textbox(label="Konu Özeti")
        analyze_btn = gr.Button("Analiz Et")
        analyze_btn.click(fn=analyze_topic, inputs=topic_in, outputs=[table_out, summary_out])

demo.launch()