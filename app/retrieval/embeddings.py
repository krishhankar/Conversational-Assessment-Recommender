from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            cls._model = SentenceTransformer("all-MiniLM-L6-v2")
        return cls._model

    @classmethod
    def encode(cls, text:str):
        model = cls.get_model()

        return model.encode(text, normalize_embeddings=True)