# 读取指定文件随机生成邮件内容
import csv
import random

def randCont():
    csv_file = csv.reader(open('./Resource/contents.csv'))
    columnNa = []
    columnSu = []
    columnCon = []
    for row in csv_file:
        columnNa.append(row[0])
        columnSu.append(row[1])
        columnCon.append(row[2])
    colNameS = random.choice(columnNa)
    colNameR = random.choice(columnNa)
    colSubj = random.choice(columnSu)
    #
    # print(columnSu)
    # print(colSubj)

    # _content = "赶-紧-开-启-你-的-财-富-旅-程-吧::  5 8 7 1 9 8.cn~"     <img src="http://587198.cn/img/bod.png" />
    #   <img src="https://mail.126.com/js6/s?func=mbox:getMessageData&mid=232:1tbi6AzUPlpEAB2eYgACsz&part=3" />
    _content0 = """\
    <html>
     <style> .title{font-weight:bold;font-size:18px;}</style>
     <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
     <body>
      <p>
       <span class="title">赶-紧-开-启-你-的-财-富-旅-程-吧Super Profit</span>
       <br>
       灛<span class="cont">5</span>灜<span class="cont">8</span>灏<span class="cont">7</span>灞<span class="cont">1</span>灟<span class="cont">9</span>灠<span class="cont">8</span>叇亝<span class="cont">.cn</span>灢叅叆
       <br>
       <br>
    
       <br><br>
       <br><br>
      </p>
     </body>
    </html>
    """
    _content1 = """\
    <html>
     <style> .title{font-weight:bold;font-size:18px;}</style>
     <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
     <body>
      <p>
       <span class="title">Super Profit</span>2020新年flag
       <br>
       咪咫咬<span class="cont">5</span>咭咮咯<span class="cont">8</span>咲咳咴<span class="cont">7</span>唝哵哶<span class="cont">1</span>唬唭<span class="cont">9</span>啦啧啨啩<span class="cont">8</span>唒唓<span class="cont">.cn</span>咢咣
       <br>
       <br>

       <br><br>
       <br><br>
      </p>
     </body>
    </html>
    """
    _content2 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <span class="title">Super Profit</span>新年愿望
           <br>
           堨堩堫堬<span class="cont">5</span>堀堁<span class="cont">8</span>堃堄<span class="cont">7</span>坚堆<span class="cont">1</span>堇堈<span class="cont">9</span>堉垩堋<span class="cont">8</span>堉垩堋<span class="cont">.cn</span>囘囙囜囝回囟囡団囤囥囦囧囨囩囱囫囬囮
           <br>
           <br>

           <br><br>
           <br><br>
          </p>
         </body>
        </html>
        """
    _content3 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <span class="title">Super Profit</span>未来可期
           <br>
           嚑嚒嚓嚔噜<span class="cont">5</span>嚖嚗嚘<span class="cont">8</span>啮嚚<span class="cont">7</span>嚛嚜嚝嚞<span class="cont">1</span>嚟嚠嚡嚢<span class="cont">9</span>嚣嚤呖<span class="cont">8</span>嚧咙<span class="cont">.cn</span>嚩咙嚧嚪嚫嚬
           <br>
           <br>

           <br><br>
           <br><br>
          </p>
         </body>
        </html>
        """
    _content4 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <br>
           <div style="width:950px; height:580px; ">
           <textarea id="descript" name="descript" placeholder="尊贵的特邀会员，我司真诚的感谢您付出1分钟时间阅读此邮件" style="border:0px,none,#080808;width:950px;height:30px;background:#FFD39B;font-size: 23px;font-color:yellow;text-align:center"></textarea>
           <textarea id="descript" name="descript" placeholder="顶级休闲娱乐场所。线上587198.cn平台，安全稳定。" style="border:0px,none,#080808;width:950px;height:30px;background:#FFD39B;font-size: 23px;font-color:yellow;text-align:center"></textarea>
           <textarea id="descript" name="descript" placeholder="内有百家乐、龙虎斗、捕鱼、扎金花、时时彩、pk10、VR彩票等上百种游戏。" style="border:0px,none,#080808;width:950px;height:30px;background:#FFD39B;font-size: 23px;font-color:yellow;text-align:center"></textarea>
           <textarea id="descript" name="descript" placeholder="专属一对一客服" style="border:0px,none,#080808;width:950px;height:30px;background:#FFD39B;font-size: 23px;font-color:yellow;text-align:center"></textarea></div>
           <br>
          </p>
         </body>
        </html>
        """
    _content5 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <span class="title">Super Profit</span>鏃犳硶鏄剧ず椤甸潰锛屽洜涓哄彂鐢熷唴閮ㄦ湇鍔″櫒閿
           <br>
           灛<span class="cont">5</span>灜<span class="cont">8</span>灏<span class="cont">7</span>灞<span class="cont">1</span>灟<span class="cont">9</span>灠<span class="cont">8</span>叇亝<span class="cont">.cn</span>灢叅叆
           <br>
           <br>

           <br><br>
           <br><br>
          </p>
         </body>
        </html>
        """
    _content6 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <span class="title">Super Profit</span>
           <br>
           s<span class="cont">5</span>u<span class="cont">8</span>per<span class="cont">7</span>pro<span class="cont">1</span>f<span class="cont">9</span>i<span class="cont">8</span>t<span class="cont">.cn</span>
           <br>
           <img src="http://587198.cn/img/bod.png" />
           <br>

           <br><br>
           <br><br>
          </p>
         </body>
        </html>
        """
    _content7 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <br>
           <div style="width:950px; height:580px; ">
           <textarea id="descript" name="descript" placeholder="百万玩家 真人对战" style="border:0px,none,#080808;width:950px;height:30px;background:#FFD39B;font-size: 23px;font-color:yellow;text-align:center"></textarea>
           <textarea id="descript" name="descript" placeholder="下载app即送168元，充值100送100👉587198.cn" style="border:0px,none,#080808;width:950px;height:30px;background:#FFD39B;font-size: 23px;font-color:yellow;text-align:center"></textarea>
           <textarea id="descript" name="descript" placeholder="内有百家乐、龙虎斗、捕鱼、扎金花、时时彩、pk10、VR彩票等上百种游戏。" style="border:0px,none,#080808;width:950px;height:30px;background:#FFD39B;font-size: 23px;font-color:yellow;text-align:center"></textarea>
           <textarea id="descript" name="descript" placeholder="更有24小时专属客服" style="border:0px,none,#080808;width:950px;height:30px;background:#FFD39B;font-size: 23px;font-color:yellow;text-align:center"></textarea></div>
           <br>
          </p>
         </body>
        </html>
        """
    _content8 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <br>
           <div style="width:950px; height:580px; ">
           <textarea id="descript" name="descript" placeholder="百家乐、龙虎斗、捕🐟、扎金花、时时彩、pk10、VR彩票等上百种游戏。" style="border:0px,none,#080808;width:950px;height:30px;background:#FFD39B;font-size: 23px;font-color:yellow;text-align:center"></textarea>
           <textarea id="descript" name="descript" placeholder="下载app即送168元，充值100送100 👉 587198.cn" style="border:0px,none,#080808;width:950px;height:30px;background:#FFD39B;font-size: 23px;font-color:yellow;text-align:center"></textarea>
            <br>
          </p>
         </body>
        </html>
        """
    _content9 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <span class="title">Super Profit</span>
           <br>
           灛<span class="cont">5</span>灜<span class="cont">8</span>灏<span class="cont">7</span>灞<span class="cont">1</span>灟<span class="cont">9</span>灠<span class="cont">8</span>叇亝<span class="cont">.cn</span>灢叅叆
           <br>
           <br>

           <br><br>
           <br><br>
          </p>
         </body>
        </html>
        """
    _content10 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <span class="title">Super Profit</span>
           <br>
           灛<span class="cont">5</span>灜<span class="cont">8</span>灏<span class="cont">7</span>灞<span class="cont">1</span>灟<span class="cont">9</span>灠<span class="cont">8</span>叇亝<span class="cont">.cn</span>灢叅叆
           <br>
           <br>

           <br><br>
           <br><br>
          </p>
         </body>
        </html>
        """
    _content11 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <span class="title">Super Profit</span>
           <br>
           灛<span class="cont">5</span>灜<span class="cont">8</span>灏<span class="cont">7</span>灞<span class="cont">1</span>灟<span class="cont">9</span>灠<span class="cont">8</span>叇亝<span class="cont">.cn</span>灢叅叆
           <br>
           <br>

           <br><br>
           <br><br>
          </p>
         </body>
        </html>
        """
    _content12 = """\
        <html>
         <style> .title{font-weight:bold;font-size:18px;}</style>
         <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
         <body>
          <p>
           <br>
           <span class="cont">5 8 7 1 9 8 . c n </span>
           <br>
           <br>
          </p>
         </body>
        </html>
        """
    _content13 = "<587198.cn>"
    _content14 = "Visit： 587198.cn "
    _content15 = "👉 587198.cn "

    _content = [_content0,_content1,_content2, _content3, _content4, _content5, _content6, _content7, _content8, _content12]
    # _content = [_content12, _content13, _content14, _content15]

    colCont = random.choice(_content)

    return colNameS, colNameR, colSubj, colCont

if __name__ == "__main__":
    randCont()