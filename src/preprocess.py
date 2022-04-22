
import codecs
import spacy
nlp = spacy.load('en_core_web_sm')

def detect_object_and_attribute(input_file):
    readfile = codecs.open(input_file, 'r', 'utf-8')
    writefile = codecs.open('/home/tup51337/dataset/50k_hotel/detected_objects_with_attributes.txt', 'w', 'utf-8')
    for line in readfile:
        parts = line.strip().split('txt: ')
        file_id = parts[0]+'txt'
        sent = parts[1].strip()
        print(sent, '>>>\n')
        piano_doc = nlp(sent)

        chunk_list = []
        for chunk in piano_doc.noun_chunks:
            words =chunk.split()
            if words[0].lower() not in set(['the', 'a', 'an']):
                chunk_list.append(chunk)
        writefile.write('file_id: ', file_id)
        writefile.write('query: ', sent)
        writefile.write('objects: ', '; '.join(chunk_list)+'\n')
        # exit(0)


if __name__ == '__main__':
    detect_object_and_attribute('/home/tup51337/dataset/50k_hotel/all_caps.txt')
