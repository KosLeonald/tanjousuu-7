import json
import random
#import time , datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

option_1 = "【誕生数７】\nあなたが結果を求めていることに関しては、もう少し時間が必要なようです。状況は悲観的ではありませんが、時間を必要としているのです。もともとこの道はゴールまでの道のりが果てしなく遠いものだったので、先々のことを考えたり先走ったりするのはあまり意味のないことでした。とは言え、結果は必ず出るよと告げられていますので、今は忍耐の時と割り切って、焦らず状況を楽しむくらいの感覚でいてください。芽が出たら花が咲く時が必ずやって来ます。"
option_2 = "【誕生数７】\n「今だよ」と合図をされているのが聞こえますか？すべての準備が整って、進む時が来ました。きっとあなたの思考も感情も何らかの否定や不安を感じることなく、何の障害を感じる事もなく、整った感覚があるのではないでしょうか。その感覚や理由を言葉で説明できなくても、あなたがそう感じるなら今がその時なのです。あなたが選択した道に、さあ進みましょう！"
option_3 = "【誕生数７】\nあなたは今、あなたの人間関係の中で、ギブ・アンド・テイクのバランスをいかにして保つかを学ぶ過程にいて、あなたのやり方を評価する時期です。あなたは与えすぎて、自分に憤りや怒りが残っていませんか？\nあるいは、もっと与えることが出来るのに掴んで離さず、自分はそのことに対して罪の意識や自己防衛の意識に悩まされていませんか？ギブ・アンド・テイクのレッスンは習得するのが一番難しい\n技能ではありますが、全ての人間関係において、いかに与え受け取るべきか、もっと気づくことが出来るようになりましょう。\n\n「愛を与えることと愛を受け取ることに違いはありません」"
#option_4 = "確率分散 1"
#option_5 = "確率分散 2"
#option_6 = "確率分散 3"

def main():
    USER_ID = info['USER_ID']
    mylist = [ option_1,option_2,option_3]    
    messages1= TextSendMessage(random.choice(mylist))
    #messages = TextSendMessage(text=random.choice(mylist))
    #messages2= TextSendMessage(text = "今日も1日頑張りましょう♪")
    # today = datetime.datetime.fromtimestamp(time.time())
    #time  = today.strftime('%H')      
 
     #   if int(time) > 20 :
    line_bot_api.broadcast(messages1)
     #   else :
    #line_bot_api.broadcast(messages2)  
    
if __name__ == "__main__" :
    main()
