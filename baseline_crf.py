
import corpus_tool
import pycrfsuite
import glob
import sys
import os
from copy import deepcopy
eval_list = []
y1 = []


def getFeatures(dialog, i):
    features = []
    # print(dialog)
    # speaker = dialog[i][1]
    # prev_speaker = dialog[i-1][1]

    if i == 0:
        features.append('change=False')
    else:
        if dialog[i]. speaker !=dialog[ i -1].speaker:
            features.append('change=True')
        else:
            features.append('change=False')

    if i == 0:
        features.append('first=True')
    else:
        features.append('first=False')



    if dialog[i].pos:
        for posTag in dialog[i].pos:
            # print(posTag)
            features.append( "TOKEN_" +posTag.token)

            features.append( "POS_" +posTag.pos)
            # if posTag.token == "?":
            # features.append("Question=True")
            # else:
            # features.append("Question=False")

    # count = count+1
    # print(features)
    return features


def trainData(x_train, y_train): trainer= pycrfsuite.Trainer(verbose=False)
    for xseq,yseq in zip(x_train, y_train):
        trainer.append(xseq,yseq )

    trainer.set_params({
        'c1': 1.0,
        'c2' :1e-3,
        'max_iterations':60,
        'feature.possible_transitions': True
    })

    trainer.train('abc.crfsuite')

# print(tokens)

def


predictTags(x1, y1, file_name):
    name1 = sys.argv[3]
    outfile = open(name1,'w' )
    tagger = pycrfsuite.Tagger()
    tagger.open('abc.crfsuite')
    fname = []
    for name in file_name:
        # print(name)
        f1 = name.split('/')[-1:]
        # print(f1)
        fname.append(f1[0])
    c=0

    for a in x1:
        tagged = []
        outfile.write('Filename="'+ str (fname[c])+ '"' + '\n')
        # print(fname[c])
        tagged = tagger.tag(a)
        ass = deepcopy(tagged)
        eval_list.append(ass)
        for i in range(0,len( tagged)):
            outfile.write(tagged.pop(0)+ "\n" )
        c = c+1
        outfile.write("\n")
        # print("Predicted:",' '.join(tagger.tag(a)))
        # print(fname)



def


send2features(dialog):
    return [getFeatures(dialog, i) for i in range(len(dialog))]


def send2labels(dialog):
    return [dialog[i].act_tag for i in range(len(dialog))]


# def getTrainData():
# for root, dirs, files, in os.walk('labeled data'):

def get_data(data_dir):
    x_train = []
    y_train = []

    total_list = hw3_corpus_tool.get_data(data_dir)
    dialog_filenames = sorted(glob.glob(os.path.join(data_dir, "*.csv")))
    # f1 = dialog_filenames.split('/')
    # print(dialogs)

    # print(fname)
    # start_time =time.time()

    for list1 in total_list:
        # print(dialog)
        x_train.append(send2features(list1))
        y_train.append(send2labels(list1))

    # print(y_train)
    # print (time.time() - start_time)
    return x_train, y_train, dialog_filenames


def main():
    # print('Getting Training Data')
    x, y, fname = get_data(sys.argv[1])
    # print('Training Data')
    trainData(x,y )
    # print('Getting Testing Data')
    x1, y1, fname1 = get_data(sys.argv[2])
    # print('Predicting Tags')
    # print(fname1)
    predictTags(x1, y1, fname1)
    return eval_list, y1


if __name__ == "__main__":
    main()










