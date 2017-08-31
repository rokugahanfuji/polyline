{\rtf1\ansi\ansicpg932\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 1. Put kmz files into kmz folder.\
2. Execute unzipkmz.py to unzip kml.\
3. You will see that kml files are created into kml folder.\
4. Execute encodekml.py to create to create encoded txt.\
5. You will see that txt files are created into txt folder.\
\
\uc0\u8251 NOTICE\
Encoded txt often include \'91\\\'92. In JavaScript,\'92\\\'92 is escape character. So if you want to write encoded txt into JavaScript codes directly, You have to use String.raw`` method like below.\
\
var string = String.raw`mer_GdlabQ?jFkF??jFkF??kFkF??jFkF??vMkF??jFkF??vMwM??wMwM??kFjF??kFjF??o\\jF??kFjF??jFvM??jFn\\?`;\
\
}