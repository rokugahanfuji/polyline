1. Put kmz files into kmz folder.
2. Execute unzipkmz.py to unzip kml.
3. You will see that kml files are created into kml folder.
4. Execute encodekml.py to create to create encoded txt.
5. You will see that txt files are created into txt folder.

※NOTICE
Encoded txt often include ‘\’. In JavaScript,’\’ is escape character. So if you want to write encoded txt into JavaScript codes directly, You have to use String.raw`` method like below.

var string = String.raw`mer_GdlabQ?jFkF??jFkF??kFkF??jFkF??vMkF??jFkF??vMwM??wMwM??kFjF??kFjF??o\jF??kFjF??jFvM??jFn\?`;

