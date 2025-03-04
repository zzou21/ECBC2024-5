import spacy

def spacyNER(text):
    nlp = spacy.load("en_core_web_sm")
    processedText = nlp(text)
    allNERLabels = nlp.get_pipe("ner").labels
    labelDict = {label: [] for label in allNERLabels}
    for ent in processedText.ents:
        labelDict[ent.label_].append(ent.text)
    print("Named Entities by Category:")
    for label in allNERLabels:
        explanation = spacy.explain(label)  # Get explanation of the label
        entity_list = labelDict[label]

        if entity_list:  # If entities were found
            print(f"\n{label} ({explanation}):")
            print(", ".join(entity_list))
        else:  # If no entities were found
            print(f"\n{label} ({explanation}): No entities found")

    
if __name__ == "__main__":
    text = "thither, is to no purpose. God in his wisdome prouided, and in his mercie prouoked, godly and able men to furnish both these functions: and such as might at home haue liued in places of honour and command, or in fashion competent and conuenient to their conditions. And this, Right Honorable, is one of the foure Arguments, and as it were plaine demonstrations, that haue conuinced mee to beleeue that assuredly God himselfe is the founder, and fauourer of this Plantation. And I will craue leaue of your Lordship to put them downe, because I am of minde, that the want either of knowledge, or consideration hereof, hath beene, and is the cause of the error and misprision of the world, touching this busines; and doe thinke that if men did ruminate, and aduisedly consider of these particulars, they would reprooue themselues for their former thoughts, and say plainly, Digitus Dei est hic. 1 The maruellous and indeed miraculous deliuerance of our worthy Gouernours, Sir Thomas Gates, Liefetenant generall, and Sir George Somers, Admirall, with all their company, of some hundred and fiftie persons, vpon the feared and abhorred Ilands of the Barmudaes, without losse of one person, when the same houre nothing was before their eyes, but imminent and ineuitable death; as neuer ship came there that perished not, so neuer was it heard of, that any ship wrackt there, but with the death of all or most of the people, saue onely this of ours. Oh how the world should haue rung of it ere this, if a farre lesse deliuerance had happened to"

    print(spacyNER(text))