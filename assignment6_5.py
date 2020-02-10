text = "X-DSPAM-Confidence:    0.8475"
startindex = text.find('0')
result = text[startindex:]
res = float(result)
print(res)
