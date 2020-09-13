import jieba
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
# from scipy.misc import imread
from collections import Counter

word = 'PowerShell提供了多种选择结构和循环结构用于控制程序的运行，熟练掌握这些结构是构建复杂程序的基础。对于学习过其他语言的人来说，这些内容应该都不难理解。而对于学习PowerShell的人来说，学习过其他语言的应该占多数，所以本篇博客也尽量减少了那些无关紧要的废话，对其中一些与其他语言有区别的点相应地作了标记。每次写博客，博主都尽量找了更多更详细的资料，以求能把一些没人注意到的细节讲清楚（比如这篇博客中关于switch中的-file参数，pstips的在线教程中就没提到，是在一个外文网站ss64中翻到的），希望这些细节对读者们能有所帮助。'
a = jieba.lcut(word, cut_all = True)
# back_color = imread(r'C:\Users\fanhang\Desktop\learn_python\NP\1.jpg')
wc = WordCloud(background_color = 'white', max_words = 500, max_font_size = 300, random_state = 42, font_path = r"c:\Windows\Fonts\STFANGSO.TTF", width = 1920, height = 1080)
counts = Counter(a)
wc.generate_from_frequencies(counts)
# imcolor = ImageColorGenerator('red')
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()
