# Text_Preprocessor
# Text Preprocessing and Stemmer Implementation

This project focuses on preprocessing a large block of text by performing a series of operations such as tokenization, stemming, and cleaning unwanted words or symbols. It aims to simplify and standardize the text, ensuring that it is suitable for further natural language processing tasks.

## Features

1. **Tokenization**: The text is broken down into individual words or punctuation marks, enabling easy analysis and manipulation.
2. **Stemming**: A custom stemming function is implemented to reduce words to their root form. This includes handling common suffixes (like 'ing', 'ness', 's') and irregular words (such as abbreviations and special terms).
3. **Cleaning**: Common stopwords (such as 'the', 'and', 'is') are removed to focus on more meaningful terms. Additionally, unnecessary punctuation marks are eliminated.
4. **Abbreviation Expansion**: Some commonly used abbreviations and acronyms (such as 'U.S.' for 'United States', 'TV' for 'television') are expanded to their full form to improve clarity.
5. **Handling Special Terms**: Special terms such as 'S.O.E.' (Special Operations, Executive) and 'M.' (monsieur) are retained or corrected for consistency.
6. **Numerical Data Removal**: Numerical values are removed from the text to avoid introducing noise into the analysis.

## Steps Performed

1. **Data Extraction**: The provided text is processed to extract words and punctuation.
2. **Stemming Function**: Words are transformed by a custom stemmer which removes common suffixes and standardizes the text.
3. **Cleaning of Unwanted Characters**: Common stopwords are removed, and unnecessary punctuation is discarded. This is done using regular expressions to ensure smooth cleaning.
4. **Abbreviation Expansion**: Certain abbreviations like 'U.S.' are expanded to their full form, enhancing the clarity of the text.
5. **Normalization**: All words are converted to lowercase to ensure consistency.
6. **Whitespace Normalization**: Extra spaces are trimmed and reduced to a single space for a clean output.

