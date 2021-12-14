from textblob import TextBlob
fields = ['text', 'timestamp', 'polarity', 'subjectivity', 'sentiment']  # field names
#writer.writerow(fields)  # writes field
data_python = ["I am feeling very happy today","I am sad","Good Night","I am feeling very stress","I am very frustrated","Fuck off"]

def get_label(analysis, threshold=0):
    if analysis.sentiment[0] > threshold:
        return 'Positive'
    elif analysis.sentiment[0] < threshold:
        return 'Negative'
    else:
        return 'Neutral'

for line in data_python:
    # performs the sentiment analysis and classifies it
    #print(line.get('text').encode('unicode_escape'))
    analysis = TextBlob(line)
    print(analysis.sentiment, get_label(analysis))  # print the results
    print("  ")
