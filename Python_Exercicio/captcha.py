from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 280, heigth = 90)
captcha_text = 'aleatorio'
data = image.generate(captcha_text)
image.write(captcha_text, 'CAPTCHA.png')