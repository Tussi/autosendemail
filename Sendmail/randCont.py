import csv
import random

def randCont():
    csv_file = csv.reader(open('D:/Downloads/Scripts/AutoSendEmail_script/Resource/contents.csv'))
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
    _content1 = """\
    <html>
     <style> .title{font-weight:bold;font-size:18px;}</style>
     <style> .cont{color:#f00;font-weight:bold;font-size:48px;}</style>
     <body>
      <p>
       <span class="title">Super Profit</span>叧叨叭叱叴叵叺叻叼叽叾卟叿吀吁吂吅吆吇吋吒吔吖吘吙吚吜吡吢
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
           <span class="title">Super Profit</span>圔圕图圗团圙圚圛圜圝圞
           <br>
           堨堩堫堬<span class="cont">5</span>堀堁<span class="cont">8</span>堃堄<span class="cont">7</span>坚堆<span class="cont">1</span>堇堈<span class="cont">9</span>堉垩堋<span class="cont">8</span>堉垩堋<span class="cont">.cn</span>
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
           <span class="title">Super Profit</span>嚑嚒嚓嚔噜嚖嚗嚘啮嚚嚛嚜嚝嚞嚟嚠嚡嚢嚣嚤呖嚧咙嚩咙嚧嚪嚫嚬
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
           灛<span class="cont">5</span>灜<span class="cont">8</span>灏<span class="cont">7</span>灞<span class="cont">1</span>灟<span class="cont">9</span>灠<span class="cont">8</span>叇亝<span class="cont">.cn</span>灢叅叆
           <br>
           <img src="https://mail.126.com/js6/s?func=mbox:getMessageData&mid=232:1tbi6AzUPlpEAB2eYgACsz&part=3" />
           <br>

           <br><br>
           <br><br>
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
    _content6 = """\
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
    _content7 = """\
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
    _content8 = """\
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
    _content13 = """\
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
    _content14 = """\
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
    _content15 = """\
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

    _content = [_content0,_content1,_content2, _content3]
    colCont = random.choice(_content)

    return colNameS, colNameR, colSubj, colCont

if __name__ == "__main__":
    randCont()