from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class FEVER(AbsTaskRetrieval):
    @property
    def metadata_dict(self):
        return {
            "name": "FEVER",
            "hf_hub_name": "mteb/fever",
            "description": (
                "FEVER (Fact Extraction and VERification) consists of 185,445 claims generated by altering sentences"
                " extracted from Wikipedia and subsequently verified without knowledge of the sentence they were"
                " derived from."
            ),
            "reference": "https://fever.ai/",
            "type": "Retrieval",
            "category": "s2p",
            "eval_splits": ["train", "dev", "test"],
            "eval_langs": ["en"],
            "main_score": "ndcg_at_10",
            "revision": "bea83ef9e8fb933d90a2f1d5515737465d613e12",
        }
