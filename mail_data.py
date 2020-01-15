# -*- coding: utf-8 -*-

import pandas as pd
import numpy
import csv
from datetime import datetime
import operator
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.mime.base import MIMEBase
from email import encoders
from os import listdir
import os
import smtplib,email,email.encoders,email.mime.text,email.mime.base
from pandas import merge
from number_extractor import bifurcated_data
from date_picker import date_req

def mailer():
    date = date_req()

    frame = bifurcated_data()

    #mailer start
    your_email = raw_input("Enter Your Email_ID with domain as '@infoedge.com'\n")
    password = raw_input("Enter your Email_ID password\n")
    recepient = "ankit.mukherjee@naukri.com"
    #recepient = ["ankit.mukherjee@naukri.com","rohit.kumar1@naukri.com","raj.ravi@naukri.com","pooja.sikka@naukri.com","saurabh.a@naukri.com","bhanu.seth@naukri.com"]
    #cc = "saurabh.a@naukri.com"
    subject = "Status of Seamless Apply for "+date
    server  = smtplib.SMTP('smtp.office365.com',587)
    server.ehlo()
    server.starttls()
    server.login(your_email, password)

    body_content = """
    <div class="BodyFragment" style=""><font size="2" style=""><span style="font-size:10pt">
<div class="PlainText" style="font-family:Tahoma"><span style="font-size:11pt">Hi,</span></div>
<span style="font-size:11pt"></span>
<div class="PlainText" style="font-family:Tahoma"><br>
<span style="font-size:11pt"></span></div><div class="PlainText" style="font-family:Tahoma">PFB Status for Seamless Apply,</div><div class="PlainText" style="font-family:Tahoma"><br></div><div class="PlainText" style="font-family:Tahoma">












<table>
	<colgroup span="7" width="85"></colgroup>
	<tbody><tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="32" align="center"><b><font face="Calibri">"""+frame[0]+"""</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><b><font face="Calibri">Clients</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><b><font face="Calibri">Jobs</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><b><font face="Calibri">Applies</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><b><font face="Calibri">% of Clients</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><b><font face="Calibri">% of Jobs</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><b><font face="Calibri">% of Applies</font></b></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="32" align="center"><b><font face="Calibri">Searchable Count</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[1])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[2])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[3])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">NA</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">NA</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">NA</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="32" align="center"><b><font face="Calibri">Total Seamless</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[4])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[5])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[6])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[7])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[8])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[9])+"""</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="32" align="center"><b><font face="Calibri">Web Seamless</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[10])+""" ("""+str(frame[52])+""")</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[11])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[12])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[13])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[14])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[15])+"""</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="32" align="center"><b><font face="Calibri">CSM Seamless</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[16])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[17])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[18])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[19])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[20])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[21])+"""</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="17" align="center"><b><font face="Calibri">TECH</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[22])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[23])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[24])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[25])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[26])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[27])+"""</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="17" align="center"><b><font face="Calibri">QC</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[28])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[29])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[30])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[31])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[32])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[33])+"""</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="17" align="center"><b><font face="Calibri">Escalation</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[34])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[35])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[36])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[37])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[38])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[39])+"""</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="32" align="center"><b><font face="Calibri">Non-Workable</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[40])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[41])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[42])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[43])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[44])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[45])+"""</font></td>
	</tr>
	<tr>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" height="17" align="center"><b><font face="Calibri">Pipeline</font></b></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[46])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[47])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[48])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[49])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[50])+"""</font></td>
		<td style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center"><font face="Calibri">"""+str(frame[51])+"""</font></td>
	</tr></tbody></table><br></div>
<span style="font-size:11pt"></span>
<div class="PlainText" style="font-family:Tahoma"><br>
<span style="font-size:11pt"></span></div>
<span style="font-size:11pt"></span>
<div class="PlainText" style="font-family:Tahoma"><br>
<span style="font-size:11pt"></span></div>
<span style="font-size:11pt"></span>
<div class="PlainText" style=""><font face="Tahoma"><span style="font-size:11pt">Regards,</span></font><br>
<p class="x_MsoNormal" style="margin-top: 0px; margin-bottom: 0px;margin:0in 0in 0.0001pt; font-size:11pt"><font color="#1f497d" face="Calibri Light, sans-serif"><b>Ankit Mukherjee</b></font></p>
<p class="x_MsoNormal" style="margin-top: 0px; margin-bottom: 0px;font-family:Calibri,sans-serif; margin:0in 0in 0.0001pt; font-size:11pt; color:rgb(32,31,30)">
<span style="margin:0px; padding:0px; border:0px; font-style:inherit; font-variant:inherit; font-weight:inherit; font-stretch:inherit; font-size:inherit; line-height:inherit; font-family:&quot;Calibri Light&quot;,sans-serif; vertical-align:baseline; color:rgb(0,176,240)">Software
 Engineer (ARAY) Operations - Naukri.com</span></p>
<p class="x_MsoNormal" style="margin-top: 0px; margin-bottom: 0px;font-family:Calibri,sans-serif; margin:0in 0in 0.0001pt; font-size:11pt; color:rgb(32,31,30)">
<span style="margin:0px; padding:0px; border:0px; font-style:inherit; font-variant:inherit; font-weight:inherit; font-stretch:inherit; font-size:inherit; line-height:inherit; font-family:&quot;Calibri Light&quot;,sans-serif; vertical-align:baseline; color:rgb(47,84,150)">Direct:&nbsp;<b>0120-3310105</b>&nbsp;|
 Extension:<b>&nbsp;105</b></span></p>
<p class="x_MsoNormal" style="margin-top: 0px; margin-bottom: 0px;font-family:Calibri,sans-serif; margin:0in 0in 0.0001pt; font-size:11pt; color:rgb(32,31,30)">
<b><span style="margin:0px; padding:0px; border:0px; font-style:inherit; font-variant:inherit; font-weight:inherit; font-stretch:inherit; font-size:inherit; line-height:inherit; font-family:&quot;Calibri Light&quot;,sans-serif; vertical-align:baseline; color:rgb(47,84,150)">#7270857735</span></b></p>
</div>
</span></font></div>"""

    text = body_content

    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = recepient
    #msg['To'] = ",".join(recepient)
    #msg['cc'] = cc
    msg['Subject'] = subject
#msg['cc'] = cc
    body = text
    msg.attach(MIMEText(body,'html'))

    # part = MIMEBase('application', "octet-stream")
    # part.set_payload(open(d+"_main_frame.xlsx", "rb").read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= "+d+"_main_frame.xlsx")
    # msg.attach(part)


    composed = msg.as_string()

    fp = open('msgtest.txt', 'w')
    fp.write(composed)


    server.sendmail(your_email, recepient, composed)
    server.quit()
    fp.close()


if __name__ == '__main__':
    mailer()
