from func.func import *

def main():
    prepareFolder()
    extractInfo()
    generateWordCloud(extractAbstract())
    genHistogram(countFigures())

    with open("./out/links", 'w') as fd :
        fd.write(getCitations())

    print('main')

if __name__=="__main__":
    main()