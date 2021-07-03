title FSJunction
set inD=.\Body
dir /ad /b %inD% > temp
python "D:\Developed\Automation\python\randomizeFile.py" temp
call "D:\Developed\Automation\Batch\GettingVariableFromFile.bat" temp

set slut="%inD%\%temp%"

set pavitra=".\Chehre"
REM set pavitra=".\FullHead"
set resultFolder="D:\Developed\FaceSwapExperimental\TestResult"

"C:\Users\HP\Miniconda3\scripts\activate.bat" && conda activate "faceswap" && python "D:\Developed\FaceSwapExperimental\FSBodyMajor.py" %slut% %pavitra% %resultFolder% 5 && rmdir %slut% &&  %0