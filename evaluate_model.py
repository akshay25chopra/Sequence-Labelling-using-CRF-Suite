import sys
import baseline_crf.py
import advanced_crf.py

pred_list = []
actual_list = []
filename = sys.argv[1]
pred_list, actual_list = filename.main()


# print(len(actual_list))
# print(len(pred_list))

def getAccuracy(pred_list, actual_list):
    correct = 0
    total = 0

    for i, j in zip(pred_list, actual_list):
        # print(len(i),len(j))
        for k in range(0, len(i)):
            if (i[k] == j[k]):
                correct = correct + 1
            total = total + 1
    # print(correct,total)
    accuracy = (correct / total) * 100
    print(accuracy)


getAccuracy(pred_list, actual_list)
