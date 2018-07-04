#-*- coding:utf-8 -*-
import textwrap
sample_text = u'''helloworld hel 你好 lodjfjafhasdhfhsd;fja;ljsdflajdflajsdklfja;lsjflk;ajdfl;jkal;dfjl;jdadflk;kjakfdljajfk;ajflakjf;ajkfajfa;jfkdsjfskajf;ajdfj;akfj
'''

print(textwrap.fill(sample_text, 18))
print(textwrap.dedent(sample_text))
