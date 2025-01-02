from sentence_transformers import SentenceTransformer, util

class TextProcessor:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text):
        return self.model.encode(text, convert_to_tensor=True)

class Categorizer:
    def __init__(self, index):
        self.index = index
        self.processor = TextProcessor()
        self.category_embeddings = self._build_index(index)

    def _build_index(self, index):
        # Precompute embeddings for index categories
        return {category: self.processor.embed_text(description)
                for category, description in index.items()}

    def chunk_and_embed(self, text, chunk_size=256):
        sentences = text.split('. ')
        embeddings = []
        for i in range(0, len(sentences), chunk_size):
            chunk = '. '.join(sentences[i:i+chunk_size])
            embeddings.append(self.processor.embed_text(chunk))
        return sum(embeddings) / len(embeddings)

    def summarize_and_embed(self, text, summarizer):
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
        return self.processor.embed_text(summary)

    def assign_category(self, text, method='chunk', summarizer=None):
        if method == 'chunk':
            article_embedding = self.chunk_and_embed(text)
        elif method == 'summary':
            if summarizer is None:
                raise ValueError("Summarizer must be provided for 'summary' method.")
            article_embedding = self.summarize_and_embed(text, summarizer)
        else:
            article_embedding = self.processor.embed_text(text)

        # Compute similarity with categories
        similarities = {
            category: util.cos_sim(article_embedding, embedding).item()
            for category, embedding in self.category_embeddings.items()
        }
        return max(similarities, key=similarities.get)
