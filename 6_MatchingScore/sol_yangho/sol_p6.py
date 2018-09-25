from html.parser import HTMLParser
import re

# set input data
# algorithm complexity O(nlogn)


word1 = 'blind'
indata1 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
result1 = 0

word2 = 'Muzi'
indata2 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
result2 = 1

word3 = 'blind'
indata3 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Blind Blind Blind Blind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nBlind Blind Blind Blind Blind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n</body>\n</html>"]
result3 = 0

word = word3
indata = indata3
result = result3

# make html paser
class MyHTMLParser(HTMLParser):
    def __init__(self, nameDict, scoreList, word):
        super(MyHTMLParser, self).__init__()
        self.word = word.lower()
        self.nameDict = nameDict
        self.scoreList = scoreList
        self.baseScore = 0
        self.outScore = 0
        self.numOflink = 0
        self.outUrl = []
        self.inbody = False


    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        # get base url
        if tag == 'meta':
            for attr in attrs:
                if 'content' in attr:
                    self.nameDict[attr[1]] = len(self.scoreList)
                    self.scoreList.append([len(self.scoreList), self.baseScore])
                print("     attr:", attr)

        elif tag == 'a':
            for attr in attrs:
                if 'href' in attr:
                    self.numOflink += 1
                    self.outUrl.append(attr[1])
                print("     attr:", attr)

        elif tag == 'body':
            print('body start point')
            self.inbody = True


    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
        # caliblate score
        if tag == 'html':
            if self.numOflink == 0:
                self.outScore = 0
            else:
                self.outScore = self.baseScore / self.numOflink
            self.scoreList[-1][1] += self.baseScore
        elif tag == 'body':
            print('body end point')
            self.inbody = False


    def give_score(self, newnameDict, newsxoreList):
        self.scoreList = newsxoreList
        self.nameDict = newnameDict
        for u in self.outUrl:
            if u in nameDict:
                self.scoreList[self.nameDict[u]][1] += self.outScore
        return (self.nameDict, self.scoreList)


    def handle_data(self, data):
        print("Encountered some data  :", data)
        # get baseScore
        if self.inbody:
            string = data.lower()
            sList = re.split('[^a-z]', string)
            self.baseScore += sList.count(self.word)


# build parser
nameDict = {}
scoreList = []
parserList = []
for htmldata in indata:
    parserList.append(MyHTMLParser(nameDict, scoreList, word))
    parserList[-1].feed(htmldata)


# sol
for parser in parserList:
    nameDict, scoreList = parser.give_score(nameDict, scoreList)
scoreList.reverse()
scoreList = sorted(scoreList, key=lambda x:x[1])
print('\nprediction : {}\nsolution : {}'.format(scoreList[-1][0], result))
