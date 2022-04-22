
import codecs
import spacy
nlp = spacy.load('en_core_web_sm')

def detect_object_and_attribute(input_file):
    readfile = codecs.open(input_file, 'r', 'utf-8')
    for line in readfile:
        parts = line.strip().split('txt: ')
        file_id = parts[0]+'txt'
        sent = parts[1].strip()
        print(sent, '>>>\n')
        piano_doc = nlp(sent)
        for token in piano_doc:
            print (token.text, token.tag_, token.head.text, token.dep_)
        exit(0)


if __name__ == '__main__':
    detect_object_and_attribute('/home/tup51337/dataset/50k_hotel/all_caps.txt')
