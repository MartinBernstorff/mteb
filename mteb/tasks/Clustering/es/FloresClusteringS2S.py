from ....abstasks.AbsTaskClustering import AbsTaskClustering


class FloresClusteringS2S(AbsTaskClustering):
    metadata = TaskMetadata()

    @property
    def metadata_dict(self) -> dict[str, str]:
        return dict(self.metadata)
        return {
            "name": "FloresClusteringS2S",
            "hf_hub_name": "jinaai/flores_clustering",
            "description": (
                "Clustering of sentences from various web articles, 32 topics in total."
            ),
            "reference": "https://huggingface.co/datasets/facebook/flores",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["es"],
            "main_score": "v_measure",
            "revision": "480b580487f53a46f881354a8348335d4edbb2de",
        }
