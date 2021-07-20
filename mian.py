import json 
import random
#import time , datetime


from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    mylist = [ "【誕生数１】\nこれまでの人生の中で、あなたはいくつも姿を変えて今日まで来ました。何もかも人任せで自分というものがなかった時期があったかも知れませんし、ただ我武者羅に頑張ることだけにエネルギーを注いだ時期もあったかも知れません。紆余曲折を経て今、新たな平穏が訪れつつあるようです。あなたが直感で感じることと心で願う事が一致し、気後れしたり虚勢を張ったりする必要もなく、力を抜いてごく自然体でいられる、つまり本来のあなた自身に戻れる時のようです。\n\n【誕生数２】\nあなたの心に強いストレスがかかっている様子が出ています。後でこんな風になったらよくないから、あれが心配だから、不安を消したいから・・・あらゆる不安や心配が心を占め、その予防のためにやるべき多くの事が身体を占め、あなたはもう一杯いっぱいですね。でも、不安や心配というのはそれがやって来てから対処をするので間に合います。先々の来るかどうか分からない事で悩むよりも、あなたの心の望むままに、「今」を生きてくださいね。\n\n【誕生数３】\nこれまであなたは難しい状況に屈することなく、あらゆる力を出して頑張ってきました。その成果が今にも現れようとしている時に、どうして自分を責めてしまっているのですか？自分の力不足や、他人への迷惑を思い、自己嫌悪に陥っているのでしょうか。そうであれば「３」の人らしい傾向ではありますが、誰もあなたに憤ってはいません。迷惑でもありません。さぁ頭を抱えて閉じた目を開けて、あなたがもたらした素晴らしい成果と称賛を受け取りましょう✨\n\n【誕生数４】\nあなたの心の声に耳を傾けてください。誰かの迷惑や噂や評価、顔色などを全く気にしなくてよい状況ならあなたはどんな答えを出すか、その声を聴いてみてください。本当はきっとあなたには分かっているのではないでしょうか。自分が何をしたいか、どう動きたいか。もしもそれが実行出来ていないとしたら、周りの環境のせいではなく、あなた自身への信頼不足なだけでしょう。今は、自分の心の声に素直になること、自分を信じてそれに飛び込んで行くことです。\n\n【誕生数５】\n今週は、あなたの情熱を注げることに対して行動することがカギとなるようです。その情熱は今はもう手放してしまっていること、あるいはその胸の内に抑え込んでいる事かも知れません。今もホットな状態で維持しているものの可能性もあります。あなたのエネルギーの中心にあって、マグマのように熱くうごめいているその情熱を今週は思い切り出していきましょう。迷いを捨ててワクワクする時です。情熱と共に光をまとって突き進みましょう。\n\n【誕生数６】\n痛みと苦しみに耐えていた時期が過ぎて、あなたの前に新たな展開、展望が広がってきました。これまで辛かった分を上回るほど、あなたは新たな展開に大きく期待が出来ますし、現在のところに留まらず、どこへでも飛んで行ける自由さも手に入れました。閉ざされ引き止められていた自分の根から起き上がり、これからはあまり深刻にならずに、もっともっと人生を楽しむ方向に舵を切りましょう。明るいきらめきの世界が広がっていることを信じてください。\n\n【誕生数７】\nあなたが結果を求めていることに関しては、もう少し時間が必要なようです。状況は悲観的ではありませんが、時間を必要としているのです。もともとこの道はゴールまでの道のりが果てしなく遠いものだったので、先々のことを考えたり先走ったりするのはあまり意味のないことでした。とは言え、結果は必ず出るよと告げられていますので、今は忍耐の時と割り切って、焦らず状況を楽しむくらいの感覚でいてください。芽が出たら花が咲く時が必ずやって来ます。\n\n【誕生数８】\n今の状態をあるがままに受け入れてください。抵抗せず、そのままを受け入れてください。どうしても認め難く変えたいと思うものは、一旦受け入れた後であなたの良いように変えてゆけばよいのです。状況はこれからとても良くなっていく可能性を秘めていますが、それはあなたの受容性の強化にかかっています。変化とはある程度の時間を要する事もありますから、タイミングが来るまでは意識的に「静かな受容」でいることに徹しましょう。\n\n【誕生数９】\nもしも今あなたが生き辛さや拘束感を感じて、息が詰まりそうな状態なら、それは自分で自分を縛っているからかも知れません。「９」のあなたは誠実で正直で、与えられたことは必ずやり遂げる意志の強さを持っています。けれどもあまりにも「こうあるべき」が強すぎてはいませんか？時には手抜きも息抜きも必要です。それは怠ける事ではなく、「建設的な柔軟さ」です。誰かの目や評価、ご機嫌など気にせず、あなたのやりやすい方法で生きてみてはいかがでしょうか♬\n\n\n占い＆タイ式リラクゼーション グラターイ\n俵 ひとみ","【誕生数１】\n今あなたは「忍耐」という試練の中にいるでしょうか。それは時さえ過ぎれば叶うものなのですが、今この瞬間は忍耐強く待つことが求められているようです。このような渦中の時には、不安がよぎり全てを否定的に捉えてしまいがちですが、あなたは必ず乗り切ることができます。ジタバタせずに、クリエイティブでポジティブな思考でいることを心がけていてくださいね♬\n\n【誕生数２】\n旅の準備は整っているのに、最初の一歩を踏み出す事を戸惑っていたり、どうやって踏み出すかが分からなかったり、そんな様子が出ています。旅や冒険は色々条件が整わないと出発することが不安になりますが、扉のカギはもう開いているので、自分で扉を開いて行けばよいのです。それだけでよいのです。心細さや不安、怖れなどは進むうちに薄らいでくるものです。\n\n【誕生数３】\n長い闇夜、暗いトンネル、そんな場所に居たような日々でしたね。でももう大丈夫。今はまだ暗闇の中で何もはっきりとは見えて来ないけれど、もうすぐ新しい日の夜明けがやって来ます。そしてあなたの周囲を明るく照らす太陽が昇ります。この夜明けから、あなたのあらゆる可能性が全て開かれ、あなたの必要なものが全て整います。最上の人生になる事を確信しましょう✨\n\n【誕生数４】\nあなたは余りにも一人ぼっちだと思い込み過ぎていませんか？もしくはあなたの方から人を遠ざけていますか？あなたに手を貸したい人や、あなたに付いていきたい人は何人もいるのに、あなたは心を開かずに頑なな様子が浮かびます。あなたはちゃんと自立していて、誰の力を借りなくても前に進める人ですが、今は人の声に耳を傾け、受容モードになる事を勧められていますよ。\n\n【誕生数５】\nあなたの中で、明と暗のような強いコントラストの対立が起きていましたか？あなたが進もうとする道に反対する内なる敵や対立によって、前進することを阻まれていたかも知れませんね。でも今あなたには、チェンジ、変化の波がやって来ているようです。それもこれまでのあなたからもう一つステップアップするような、良い変化の波です。この波にうまく乗って、障害を乗り越えていきましょう！\n\n【誕生数６】\n今、あなたはこの地を離れることを望んでいるか、人間関係において距離を置きたい人がいるでしょうか。心の中では望んでいるのに、人からどう見られるか、何と言われるかということが気になり過ぎていませんか？でもあなたの人生はあなたのもので、やりたい事を我慢しても誰も責任は取ってくれません。あなたの本当の声を聴き、自分の人生を自分で導きましょう。\n\n【誕生数７】\n「今だよ」と合図をされているのが聞こえますか？すべての準備が整って、進む時が来ました。きっとあなたの思考も感情も何らかの否定や不安を感じることなく、何の障害を感じる事もなく、整った感覚があるのではないでしょうか。その感覚や理由を言葉で説明できなくても、あなたがそう感じるなら今がその時なのです。あなたが選択した道に、さあ進みましょう！\n\n【誕生数８】\nあなたの中で「再誕生」が始まっているようです。これまでの人生では、自ら動かずに人任せな時期や、反対に自分で何とかしようと息巻いて激しく突き進んだ時期もあったことでしょう。そのような時期を経て、これからは本来のあなたらしさ、自然のままのあなたを出していける無垢な時期に入ります。あなたが培ってきた強さやエネルギーが助けとなるでしょう♡\n\n【誕生数９】\nあなたは究極の選択を迫られている渦中でしょうか。右と左どちらを選ぶか。どちらを選んでも良い結果にはなりそうもない。でも選ばなければならない。にっちもさっちもいかない状況ですね💦でもよく目を凝らして見てみてください。あなたの前にある道は二つだけではありません。たくさんの道がさぁどうぞと拓けています。さぁしっかり選び自信をもって進んでくださいね。\n\n今週は私の週間占い初期の頃に使用していた、ソニアショケットさんのオラクルカード『アスク・ユア・ガイド』よりお届けいたします。\n\n\n占い＆タイ式リラクゼーション グラターイ\n俵 ひとみ","【誕生数１】\nあなたは今、リーダーとしての役割を意識的に全面的に受け入れる時です。あなたの集中力、専心、安定感、鍛錬を通して、あなたは裏方から登場し、能力と知恵の両方で人々に認められるようになります。そして他の人は自然とあなたのカリスマ的波動に引き付けられあなたを信頼できると感じ、あなたの指導力に従うでしょう。あなたは自分の明るい光を世の中に放ち、あなたが他の人々を高みに導いていく際、その情熱や自信について語らなくてよいのです。\nただし自分に無理を課したり、燃え尽きてしまうことには注意してください。\n「自信を持ってリードしていきなさい」\n\n【誕生数２】\nあなたを苦しめた全ての攻撃、裏切りによって、瞬間的に傷ついたあなたの魂が癒される時です。\n今このときは、自分自身を信頼することは難しいかも知れませんが、信頼をしなければなりません。起こってしまったことに対して、自分自身や他人を責めるのをやめ、全てを全面的に許しましょう。人間はみな、深刻で時には酷い誤りを犯すものです。あなたは侵害されたと感じても、それは自分の経験から学ぶべき教訓なのです。\nもしもあなたが否定の泥沼に留まるなら、それはあなたを不利な立場に陥れるだけです。あなたはこれらの不愉快な経験から学び、どのように再発防止ができるのかを考えてみましょう。\n「危機は去りました。あなたは安全です。今こそ癒され、そしてあなたの経験から学ぶ時です」\n\n【誕生数３】\nあなたが人生に望む物は何でも作り出すことができますが、それはあなたが必要な仕事を自ら進んでしようとする時のみにできることです。そこには、近道も迂回路も無料のランチもないということです。\n成功するための唯一の道は、鍛錬し、やり続けるということです。あなたの目的を果たすために必要なことは何でも、自ら進んで行ってください。もし、自分がしなければならないことが何か分からない時は、それが何であるかを学びましょう。ハートと頭をオープンにして、あなたの基準を高く掲げてください。\n「いかなる分野においても、習熟するということは、あなた自身の中から最善だと思うものを求めることに他なりません」\n\n【誕生数４】\n今この時期は、緊急性があるという想像に基づいて行動を取るときではありません。感情があなたと共に流れ出るのを止めてください。あなたの理性の力をしっかりと持ち、目の前のドラマやこの瞬間の激しさから遠ざかりたいという気持ちを信頼しましょう。あなたのハイヤー・セルフが、あなたを正しい結論へ誘導してくれるのに任せましょう。\nその結論を心に抱いて眠りにつき、さらには、その結論を心に抱いて三夜眠り、ハイヤー・セルフのメッセージを心に留めましょう。\n「今は、ハイヤー・セルフにそれを任せてください」\n（ハイヤー・セルフとは、あなたの中に在る本当のあなた、なにが真実かを知っているあなたのことです）\n\n【誕生数５】\nあなたを優雅さと気楽さが満たそうとしています。あなたは自分の目的と繋がり、あなたが鍛錬を積んで注力してきたことが実を結びます。単なる幸運を超えたかたちで。\n自分の瞬間的な衝動を信頼し、躊躇することなくそれに乗って行動しましょう。あなたの最大の課題は、この楽しく自然で健康的な自尊心をしっかりと保ち、他人に横槍をいれさせないことです。\nあなたの夢、あなたのスピリット、あなた自身を信じましょう。\n「優雅に歩きなさい。万事上手くいきます」\n\n【誕生数６】\nあなたは、偉大な発展と祝福の時期に入りました。あなたは、豊穣、祝福、歓待の季節にいざなわれています。今こそ、人生があなたにその実りで報いる時期なのです。あなたは婚約したり、結婚したり、昇格したり、何かを獲得したり、あるいは長く待たれたラッキーな休暇を得るかも知れません。\nあなたが何を望もうとも、確実にそれが来ているので準備をしましょう。人生の潮の流れがあなたの方へ向いてきており、それはあなたがしっかりと努力をしてきたことや、あなたが夢や目標に誓いを立て、コミットしてきたことへの当然の結果なのです。\n「パーティーの計画を立てなさい。すぐに、その祝福の理由が分かります」\n\n【誕生数７】\nあなたは今、あなたの人間関係の中で、ギブ・アンド・テイクのバランスをいかにして保つかを学ぶ過程にいて、あなたのやり方を評価する時期です。あなたは与えすぎて、自分に憤りや怒りが残っていませんか？\nあるいは、もっと与えることが出来るのに掴んで離さず、自分はそのことに対して罪の意識や自己防衛の意識に悩まされていませんか？ギブ・アンド・テイクのレッスンは習得するのが一番難しい\n技能ではありますが、全ての人間関係において、いかに与え受け取るべきか、もっと気づくことが出来るようになりましょう。\n「愛を与えることと愛を受け取ることに違いはありません」\n\n【誕生数８】\nあなたは間違った選択か習慣的な行動のせいで、自分を自己批判し恥じ入る場面に遭遇するかも知れません。\nけれど、あなたは進化するためにここにいて、その道のりの中で多くの過ちも犯すでしょう。それはあなたの学習過程の一部であり、あなたの成長のために必要なことだという事を忘れないでください。\n結局のところ、とても深刻で重大であるがために、許しようがない過ちや失敗などないのです。周りの人たちも、たとえあなたがひどい過ちを犯しても、あなたを愛することを止めはしません。\n「生きて学びなさい」\n\n【誕生数９】\nあなたが近頃何にも楽しみを感じられず、自分の歓びから切り離されていることについて治療をしましょう。\nリラックスして、楽しんで、楽しい時が流れるままにしてください。人生は楽しむもので、我慢するものではありません。美味しい食べ物や良い音楽、親しい友人、楽しい娯楽などであなたの魂を歓ばせてあげてください。自分を甘やかしすぎるとか、心を奪われる事に躊躇しないで。\n「どれだけ、この歓びに抵抗できますか？」\n\n\n占い＆タイ式リラクゼーション グラターイ\n俵 ひとみ"]
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
