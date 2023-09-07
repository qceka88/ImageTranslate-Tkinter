            TEXT FROM IMAGE TRANSLATOR

               SMALL THKINTER PROJECT
            
This program is using ot translate text from images.
User can use directly picture of text or picture of whole paper sheet.
If photo is taken from some angle, user can use TRANSFORM function to "straight" the image.


EXAMPLES:

<img src="readme_images/examples/bulgarian_text.PNG" width="400" height="100">

<img src="readme_images/examples/test_img.png" width="400" height="100">

<img src="readme_images/examples/tilt_image.PNG" width="400" height="400">

<img src="readme_images/examples/english_text.PNG" width="400" height="100">

Main window of the program. It have a buttons for UPLOAD, TRANSFORM, CHECK IMAGE,
INPUT fields for TARGET and SOURCE languages, also EXTRACT button, to extract the text from
For input languages program use abbreviations (iso 639-1 standard language codes).

![main_window.PNG](readme_images%2Fmain_window.PNG)

When user select to transform image. In the middle of process a pop-up window appear.
User can see is contour detection is good. If points are matching corners of paper sheet
(red dots are temporary marking using OpenCV). In case that program cant detect the corners of
paper sheet. Error message will be raised.
We can continue with transforming the picture when second windows is closed. 
If program does not raise error message. Transforming process is finished.

![transform_image.PNG](readme_images%2Ftransform_image.PNG)

When user use check button, can see the picture after transformation.
It turned in grayscale, because OCR module work better with gray images (EasyOCR in this case).
If transform function is not used in the case. User also can use the check button to see the image.

![check_image.PNG](readme_images%2Fcheck_image.PNG)

If language abbreviations have symbols that don`t corresponding to ISO 639-1 standard language codes.
Warning message will appear to screen. If user has forgot to upload image,
program will raise error again for missing image. 


![enter_language.PNG](readme_images%2Fenter_language.PNG)

When user click on extract button. After few seconds a second windows will appear.
Initially translated text is not shown. User can make corrections on extracted text and
after this to proceed with translation of text.

![original_text.PNG](readme_images%2Foriginal_text.PNG)

With translate function in the empty field will appear the translated text.
User can make corrections on translated text and after this can proceed with saving file.

![text_extract.PNG](readme_images%2Ftext_extract.PNG)

User have option to save text  in three types of files.
.txt .doc . docx. 

![save_options.PNG](readme_images%2Fsave_options.PNG)

Result in .docx file

![result.PNG](readme_images%2Fresult.PNG)