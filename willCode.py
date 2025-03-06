import openai
import spacy
import difflib
import json

client = openai.OpenAI(api_key="[-YOUR-API-KEY-HERE-]")

# System message to instruct ChatGPT on transcription rules
SYSTEM_PROMPT = """You are an expert in transcribing early modern English printed texts. 
You receive raw OCR text and correct it based on human-verified transcriptions. 

Rules:
- Preserve original spelling.
- Do not translate Latin text into English.
- Expand abbreviations (e.g., 'wᵗʰ' → 'with').
- Convert 'ſ' (long s) to 's'.
- Separate ligatures into individual letters.
- Mark marginal notes as [MARGINAL NOTE: text].
- Retain formatting and line breaks where possible.

Here are some examples of corrections:"""

#few-shot training -- the more the better here
EXAMPLES = [
    {"ocr": "all things that shall be treated secretlie at y® Counsell",
     "corrected": "all things that shall be treated secretlie at the counsell"},
    
    {"ocr": "w shall be resolued vpon",
     "corrected": "which shall be resolved upon"}
]

# iterate over the few-shot data and format them as instructions (this will be sent to
# ChatGPT immediately after the SYSTEM_PROMPT text):
def format_few_shot_prompt(examples):
    """Formats the prompt using OCR and human-corrected transcriptions."""
    formatted_examples = "\n".join(
        f"Original OCR:\n{ex['ocr']}\nCorrected Transcription:\n{ex['corrected']}\n---"
        for ex in examples
    )
    return formatted_examples

# New OCR text to be corrected (hard-coded for demonstration purposes; this needs to be
# modular and accept a directory of text files as an argument
new_ocr_text = """
"""

def correct_transcription(ocr_text):
    """Sends OCR text to ChatGPT with few-shot learning to improve accuracy."""
    gptCleanedOCRDict = {}
    pageIterator = 0
    for singlePage in ocr_text:
        prompt = SYSTEM_PROMPT + "\n" + format_few_shot_prompt(EXAMPLES) + f"\nPlease correct the following:\n{singlePage}\nCorrected Transcription:"

        response = client.chat.completions.create(
            model="gpt-4-turbo", # TODO: try other models? turbo is cheap and fast, but can more expensive, "better" models help?
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2, # i.e., be more deterministic, less "creative"; change to experiment
            stream=True # show results as they appear
        )

        # Collect the streamed tokens:
        corrected_text = ""
        print("\n[INFO] Streaming response from ChatGPT...\n")
        for chunk in response:
            if hasattr(chunk.choices[0], "delta") and hasattr(chunk.choices[0].delta, "content"):
                text_part = chunk.choices[0].delta.content
                if text_part:  # is null at the end of the stream
                    print(text_part, end="", flush=True)  # print tokens as they arrive
                    corrected_text += text_part  # and accumulate tokens into the final string
        gptCleanedOCRDict[pageIterator] = corrected_text

    print("\n\n[INFO] Transcription correction complete.")
    return corrected_text.strip()

if __name__ == "__main__":
    uncleanedText = 
    finalDict = correct_transcription(uncleanedText)
    with open("finalGPTCleanedVCL.json", "w") as storageJSON:
        json.dump(finalDict, storageJSON, indent=4)
