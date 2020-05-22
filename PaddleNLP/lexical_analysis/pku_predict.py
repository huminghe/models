import pkuseg
for i in range(1000):
    num = "%05d" % i
    pkuseg.test("/data1/huminghe/models/PaddleNLP/lexical_analysis/data/corpus_new/part-" + num, "./results/pku/result-" + num, nthread=10, postag=True)
