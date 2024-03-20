from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks import AbsTaskBitextMining, CrosslingualTask

_LANGUAGES = [
    "sqi-eng",
    "fry-eng",
    "kur-eng",
    "tur-eng",
    "deu-eng",
    "nld-eng",
    "ron-eng",
    "ang-eng",
    "ido-eng",
    "jav-eng",
    "isl-eng",
    "slv-eng",
    "cym-eng",
    "kaz-eng",
    "est-eng",
    "heb-eng",
    "gla-eng",
    "mar-eng",
    "lat-eng",
    "bel-eng",
    "pms-eng",
    "gle-eng",
    "pes-eng",
    "nob-eng",
    "bul-eng",
    "cbk-eng",
    "hun-eng",
    "uig-eng",
    "rus-eng",
    "spa-eng",
    "hye-eng",
    "tel-eng",
    "afr-eng",
    "mon-eng",
    "arz-eng",
    "hrv-eng",
    "nov-eng",
    "gsw-eng",
    "nds-eng",
    "ukr-eng",
    "uzb-eng",
    "lit-eng",
    "ina-eng",
    "lfn-eng",
    "zsm-eng",
    "ita-eng",
    "cmn-eng",
    "lvs-eng",
    "glg-eng",
    "ceb-eng",
    "bre-eng",
    "ben-eng",
    "swg-eng",
    "arq-eng",
    "kab-eng",
    "fra-eng",
    "por-eng",
    "tat-eng",
    "oci-eng",
    "pol-eng",
    "war-eng",
    "aze-eng",
    "vie-eng",
    "nno-eng",
    "cha-eng",
    "mhr-eng",
    "dan-eng",
    "ell-eng",
    "amh-eng",
    "pam-eng",
    "hsb-eng",
    "srp-eng",
    "epo-eng",
    "kzj-eng",
    "awa-eng",
    "fao-eng",
    "mal-eng",
    "ile-eng",
    "bos-eng",
    "cor-eng",
    "cat-eng",
    "eus-eng",
    "yue-eng",
    "swe-eng",
    "dtp-eng",
    "kat-eng",
    "jpn-eng",
    "csb-eng",
    "xho-eng",
    "orv-eng",
    "ind-eng",
    "tuk-eng",
    "max-eng",
    "swh-eng",
    "hin-eng",
    "dsb-eng",
    "ber-eng",
    "tam-eng",
    "slk-eng",
    "tgl-eng",
    "ast-eng",
    "mkd-eng",
    "khm-eng",
    "ces-eng",
    "tzl-eng",
    "urd-eng",
    "ara-eng",
    "kor-eng",
    "yid-eng",
    "fin-eng",
    "tha-eng",
    "wuu-eng",
]


class TatoebaBitextMining(AbsTaskBitextMining, CrosslingualTask):
    metadata = TaskMetadata(
        name="Tatoeba",
        hf_hub_name="facebook/flores",
        description="1,000 English-aligned sentence pairs for each language based on the Tatoeba corpus",
        reference="https://huggingface.co/datasets/facebook/flores",
        type="BitextMining",
        category="s2s",
        eval_splits=["test"],
        eval_langs=["eng", "de", "en"],
        main_score="f1",
        revision="80dc3040d19756742c9a18267ab30f54fb8e226b",
        date=None,
        form=None,
        domains=None,
        task_subtypes=None,
        license=None,
        socioeconomic_status=None,
        annotations_creators=None,
        dialect=None,
        text_creation=None,
        bibtex_citation=None,
    )

    @property
    def metadata_dict(self) -> dict[str, str]:
        return dict(self.metadata)
