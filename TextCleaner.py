import re
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from nltk.corpus import wordnet as wn

class TextCleaner:
    def __init__(self):
        self.tag_map = defaultdict(lambda: wn.NOUN)
        self.tag_map['J'] = wn.ADJ
        self.tag_map['V'] = wn.VERB
        self.tag_map['R'] = wn.ADV
        self.stopwords = stopwords.words('english')

    def clean_abstract(self, text):
        text = str(text)
        text = text.lower().strip()
        text = text.replace("\n", " ").replace("\t", " ").replace("\r", " ")
        text = self.regex_cleaning(text)
        return text

    def regex_cleaning(self, text):
        replacements = {
    r'\bhosp\b': 'hospital',
    r'\bhospitals\b': 'hospital',
    r'\bhosps\b': 'hospital',
    r'\buni\b': 'university',
    r'\buniv\b': 'university',
    r'\bunis\b': 'university',
    r'\bunivrs\b': 'university',
    r'\bunivrsity\b': 'university',
    r'\buniversities\b': 'university',
    r'\buniversitys\b': 'university',
    r'\bassoc\b': 'association',
    r'\bsoc\b': 'society',
    r'\bft\b': 'foundation trust',
    r'\bnhsft\b': 'nhs foundation trust',
    r'\btrst\b': 'trust',
    r'\btrs\b': 'trust',
    r'\bnhstrst\b': 'nhs trust',
    r'\bnhstrs\b': 'nhs trust',
    r'\&\b': 'and',
    r'\bmed\b': 'medical',
    r'\bdr\b': 'doctor',
    r'\bdrs\b': 'doctors',
    r'\bdept\b': 'department',
    r'\bctr\b': 'centre',
    r'\brheumatol\b': 'rheumatology',
    r'\bassoc\b': 'association',
    r'\bhlth\b': 'health',
    r'\bltd\b': 'limited',
    r'\bpcn\b': 'primary care network',
    r'\blmc\b': 'local medical committee',
    r'\brcgp\b': 'royal college of general practitioners'
    }

        for pattern, replacement in replacements.items():
            text = re.sub(pattern, replacement, text)
        text = text.split('-')[0].strip()
        text = re.sub(r'[^a-z\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

